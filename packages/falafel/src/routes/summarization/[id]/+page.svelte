<script lang="ts" async>
  import Truncator from "@components/Truncator.svelte";
  import { API_URL } from "../../../constants";
  import type { SummarizationHistory, SummarizationHistoryItem } from "../../history/+page.svelte";
  import Layout from "../../layout.svelte";
  import Icon from "@components/Icon.svelte";
  import { PopupType, Popup } from "@components/PopupManager";

  export let data;

  let summarization: { text: string; name: string; date: number; ext: string };
  (async () => {
    const history = JSON.parse(localStorage.getItem("history") || "[]");
    let correspondingHistoryItem = history.find(
      (candidate: { id: string }) => data.id === candidate.id
    );
    correspondingHistoryItem = await fetchSummarizationMetadata();
    summarization = correspondingHistoryItem;
  })();

  async function fetchSummarizationMetadata() {
    try {
      const req = await fetch(`${API_URL}/summarization/${data.id}`);
      const text = await req.json();
      if (text.text) return text;
    } catch (err) {
      console.warn(err);
    }
  }
  let copyIcon = "copy";

  async function copySummarization() {
    try {
      await navigator.clipboard.writeText(summarization.text);
      copyIcon = "check";
      await new Popup("Copied summarization to clipboard", PopupType.Success, 6000, "Success").show();
      copyIcon = "copy";
    } catch(err) {
      console.error(err);
      new Popup("Could not copy to clipboard", PopupType.Error, 6000, "Error").show();
    }
  }
</script>

<Layout back>
  <svelte:fragment slot="heading">Summarization</svelte:fragment>
  {#if summarization}
    <small class="metadata">
      <Truncator breakpoint={200}>{summarization.name}</Truncator>.{summarization.ext} •
      summarized {new Date(summarization.date)
        .toISOString()
        .split("T")[0]}</small
    >
    <div class="summarization-viewer">
      <div class="controls">
        <button on:click={copySummarization} aria-label="Copy summarization to clipboard"><Icon color="var(--border)" name={copyIcon}/></button>
      </div>
      {summarization.text}</div>
  {:else}
    <p class="not-found">
      <Icon color="var(--fg-error)" name="warning" /> Could not find summarization
    </p>
  {/if}
</Layout>

<style>
  .metadata {
    font: var(--font-quiet);
    color: var(--fg-l2);
    margin-bottom: 20px;
    display: block;
  }
  .summarization-viewer {
    width: 500px;
    min-height: 400px;
    max-height: 70vh;
    overflow-y: auto;
    padding: 20px 25px;
    border: 1px solid var(--border);
    border-radius: var(--radius-m);
    line-height: 1.7;
    color: var(--fg-l1);
    position: relative;
  }
  .not-found {
    display: flex;
    gap: 5px;
    color: var(--fg-error);
    font-style: italic;
  }
  .controls {
    position: absolute;
    right: 10px;
    top: 10px;
    background: white;
    box-shadow: 0 0 5px white;
  }

  :global(.controls button:hover div) {
    background-color: var(--fg-l2) !important;
  }
</style>
