<script lang="ts" async>
  import Truncator from "@components/Truncator.svelte";
  import { API_URL } from "../../../constants";
  import type { PDFHistory, PDFHistoryItem } from "../../history/+page.svelte";
  import Layout from "../../layout.svelte";

  export let data;

  let summarization: { text: string; name: string; date: number };
  (async () => {
    const history = JSON.parse(localStorage.getItem("history") || "[]");
    let correspondingPDF = history.find(
      (pdf: { id: string }) => data.id === pdf.id
    );
    correspondingPDF = await fetchSummarizationMetadata();
    if (!correspondingPDF) throw new Error("The file could not be found"); // todo: error component

    summarization = correspondingPDF;
  })();

  async function fetchSummarizationMetadata() {
    const req = await fetch(`${API_URL}/summarization/${data.id}`);
    const text = await req.json();
    if (text.text) return text;
    else throw new Error("no summarization found");
  }
</script>

<Layout back>
  <svelte:fragment slot="heading">Summarization</svelte:fragment>
  {#if summarization}
    <small class="pdf-metadata">
      <Truncator breakpoint={200}>{summarization.name}</Truncator>.pdf •
      summarized {new Date(summarization.date)
        .toISOString()
        .split("T")[0]}</small
    >
    <div class="summarization-viewer">{summarization.text}</div>
  {/if}
</Layout>

<style>
  .pdf-metadata {
    font: var(--font-quiet);
    color: var(--fg-l2);
    margin-bottom: 20px;
    display: block;
  }
  .summarization-viewer {
    width: 500px;
    padding: 20px;
    border: 1px solid var(--border);
    border-radius: var(--radius-m);
    line-height: 1.7;
    min-height: 400px;
    color: var(--fg-l1);
  }
</style>
