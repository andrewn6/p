<script lang="ts" async>
  import { API_URL } from "../../../constants";
  import type { PDFHistory, PDFHistoryItem } from "../../history/+page.svelte";
  import Layout from "../../layout.svelte";

  export let data;

  let pdf: PDFHistoryItem | undefined;
  (async () => {
    const history: PDFHistory = JSON.parse(
      localStorage.getItem("history") || "[]"
    );
    let foundPdf: PDFHistoryItem | undefined = history.find(
      (pdf) => data.id === pdf.id
    );
    if (!foundPdf) foundPdf = await fetchEntryInformation(data.id || "");
    if (!foundPdf) throw new Error("The pdf could not be found"); // todo: error component

    pdf = foundPdf;
  })();
  async function fetchEntryInformation(id: string) {
    const req = await fetch(`${API_URL}/pdf-info/${id}`);
    const json = await req.json();
    if (!json.name) return undefined;
    else return json;
  }
</script>

<Layout back>
  <svelte:fragment slot="heading">View PDF</svelte:fragment>
  {#if pdf}
    <small class="pdf-metadata">
      {pdf.name}.pdf • summarized {new Date(pdf.date)
        .toISOString()
        .split("T")[0]}</small
    >
    <iframe title="PDF" class="pdf-iframe" src={`${API_URL}/pdf/${pdf.id}`} />
  {/if}
</Layout>

<style>
  .pdf-metadata {
    font: var(--font-quiet);
    color: var(--fg-l2);
    margin-bottom: 20px;
    display: block;
  }
  .pdf-iframe {
    max-width: 100%;
    min-width: 400px;
    min-height: 400px;
  }
</style>
