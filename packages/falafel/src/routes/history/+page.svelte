<script lang="ts">
  import Layout from "../layout.svelte";
  type PDFHistory = { name: string; id: string; date: number }[];

  let history = localStorage.getItem("history");
  let items: PDFHistory | false = history && JSON.parse(history);
</script>

<Layout back>
  <svelte:fragment slot="heading">History</svelte:fragment>
  <div class="history-container">
    {#if items}
      {#each items as item}
        <a href={`/pdf/${item.id}`} class="history-item">
          <p class="history-item-name">{item.name}<small>.pdf</small></p>
          <p class="history-item-date">
            {new Date(item.date).toISOString().split("T")[0]}
          </p>
        </a>
      {/each}
    {:else}
      <p class="no-history">
        you haven't summarized any PDFs — <a class="link" href="/summarize"
          >yet...</a
        >
      </p>
    {/if}
  </div>
</Layout>

<style>
  .history-container {
    padding: 8px;
    border: 1px solid var(--border);
    background: var(--bg-l1);
    border-radius: var(--radius-l);
    width: 100%;
    margin: 10px 0;
    min-height: 300px;
    box-shadow: var(--shadow);
  }
  .history-item {
    padding: 14px 20px;
    border-radius: var(--radius-l);
    border: 1px solid var(--border);
    transition: 0.1s;
    cursor: pointer;
    display: block;
    text-decoration: none;
  }
  .history-item:not(:first-child) {
    margin: 5px 0;
  }
  .history-item-name {
    font-weight: 600;
    color: var(--fg-l1);
  }
  .history-item-name small {
    font: var(--font-quiet);
    font-size: 0.8rem;
    color: var(--fg-l2);
  }
  .history-item-date {
    font: var(--font-quiet);
    color: var(--fg-l2);
  }
  .history-item:hover {
    background: var(--bg-l2);
    border: 1px solid var(--border-focus);
    box-shadow: var(--shadow);
  }
  .no-history {
    margin-top: 15px;
    text-align: center;
    font: var(--font-quiet);

    color: var(--fg-l2);
  }

  .no-history .link {
    color: var(--fg-l1);
  }
</style>
