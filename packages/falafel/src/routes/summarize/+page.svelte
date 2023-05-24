<script lang="ts">
  import { goto } from "$app/navigation";

  import Button from "@components/Button.svelte";
  import FileChooser from "@components/FileChooser.svelte";
  import Layout from "../layout.svelte";
  import { API_URL } from "../../constants";
  import type { PDFHistory } from "../history/+page.svelte";

  let selectedPDF: File | null = null;
  let loading: boolean = false;
  $: disabled = !(
    selectedPDF &&
    selectedPDF.type === "application/pdf" &&
    true
  );

  async function summarize(file: File | null) {
    if (!file) return;
    // check, again, if the file is a pdf
    // it's safe to not notify the user, only devs like you
    // will be able to bypass the checks above (somehow)...
    if (file.type !== "application/pdf")
      throw new Error("I told you already, only PDFs! 😭");

    loading = true;

    const formData = new FormData();
    formData.append("pdf_file", file);
    const req = await fetch(`${API_URL}/summarize`, {
      method: "POST",
      body: formData,
    });

    const json = await req.json();
    if (json.id) {
      let storedHistory = localStorage.getItem("history") || "[]";
      let history: PDFHistory = JSON.parse(storedHistory);
      history.push({
        name: file.name.replace(".pdf", ""),
        id: json.id,
        date: Date.now(),
      });
      localStorage.setItem("history", JSON.stringify(history));
      // once done summarizing the pdf, when the user
      // goes back in browser history, go back to the
      // menu instead of back to "summarize a pdf"
      goto(`/summarization/${json.id}`, { replaceState: true });
    } else {
      alert(
        `an error has occured!!!!!!!!! and idk what it is :O\nthis is a temporary alert until I have a nice error popup`
      );
    }
  }
</script>

<Layout back>
  <svelte:fragment slot="heading">New PDF</svelte:fragment>
  <FileChooser bind:selectedPDF />
  <Button
    on:click={() => summarize(selectedPDF)}
    disabled={disabled || null}
    primary
    inProgress={loading}
    fullWidth={true}
    >{loading ? "summarizing" : "summarize ⚡️"}
  </Button>
</Layout>
