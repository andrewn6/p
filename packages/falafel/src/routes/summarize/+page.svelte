<script lang="ts">
  import { goto } from "$app/navigation";

  import Button from "@components/Button.svelte";
  import FileChooser from "@components/FileChooser.svelte";
  import Layout from "../layout.svelte";

  let selectedPDF: File | null = null;
  $: disabled = !(
    selectedPDF &&
    selectedPDF.type === "applicatation/pdf" &&
    true
  );

  async function summarize(file: File) {
    // check, again, if the file is a pdf
    // it's safe to not notify the user, only devs like you
    // will be able to bypass the checks above (somehow)...
    if (file.type !== "application/pdf")
      throw new Error("I told you already, only PDFs! 😭");

    const formData = new FormData();
    formData.append("pdf_file", file);
    const req = await fetch(`${apiURL}/summarize`, {
      method: "POST",
      body: formData,
    });
    const json = await req.json();
    if (json.id) {
      // once done summarizing the pdf, when the user
      // goes back in browser history, go back to the
      // menu instead of back to "summarize a pdf"
      goto(`/pdf/${json.id}`, { replaceState: true });
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
    on:click={() => /*summarize(selectedPDF)*/ null}
    disabled={disabled || null}
    primary
    fullWidth>summarize ⚡️</Button
  >
</Layout>
