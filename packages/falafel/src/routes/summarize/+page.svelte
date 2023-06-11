<script lang="ts">
  import { goto } from "$app/navigation";

  import Button from "@components/Button.svelte";
  import FileChooser from "@components/FileChooser.svelte";
  import Layout from "../layout.svelte";
  import { API_URL, allowedFileTypes } from "../../constants";
  import type { SummarizationHistory as SummarizationHistory } from "../history/+page.svelte";
  import { Popup, PopupType } from "@components/PopupManager";

  let selectedFile: File | null = null;
  let loading: boolean = false;
  $: disabled = !(
    selectedFile &&
    allowedFileTypes.includes(selectedFile.type) &&
    true
  );

  async function summarize(file: File | null) {
    if (!file) return;
    // check, again, if the file is valid
    // it's safe to not notify the user, only devs like you
    // will be able to bypass the checks above (somehow)...
    if (!allowedFileTypes.includes(file.type))
      throw new Error("I told you already, only PDFs/PPTXs! 😭");

    loading = true;

    const formData = new FormData();
    formData.append("file", file);
    const json = await trySummarize(formData);
    if (json.id) {
      let storedHistory = localStorage.getItem("history") || "[]";
      let history: SummarizationHistory = JSON.parse(storedHistory);
      let splitFilename = file.name.split(".");
      history.push({
        name: splitFilename.slice(0, -1).join("."),
        id: json.id,
        date: Date.now(),
        ext: splitFilename.at(-1) || ""
      });
      localStorage.setItem("history", JSON.stringify(history));
      // once done summarizing the pdf, when the user
      // goes back in browser history, go back to the
      // menu instead of back to "summarize a pdf"
      goto(`/summarization/${json.id}`, { replaceState: true });
    } else {
      loading = false;
      new Popup("Client-side error or API did not respond", PopupType.Error, 6000, "Error").show();
    }
  }

  async function trySummarize(formData: FormData) {
    try {
      const req = await fetch(`${API_URL}/summarize`, {
        method: "POST",
        body: formData,
      });
      const json = await req.json();
      return json;
    } catch (err: any) {
      loading = false;
      if (!(err instanceof Error)) {
        err = new Error(err.toString());
      }
      new Popup(err.message, PopupType.Error, 6000, "API error").show();
      return {};
    }
  }
</script>

<Layout back>
  <svelte:fragment slot="heading">New PDF</svelte:fragment>
  <FileChooser bind:selectedFile={selectedFile} />
  <Button
    on:click={() => summarize(selectedFile)}
    disabled={disabled || null}
    primary
    inProgress={loading}
    fullWidth={true}
    >{loading ? "summarizing" : "summarize ⚡️"}
  </Button>
</Layout>
