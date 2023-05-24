<script context="module" lang="ts">
  export type PDFHistoryItem = { name: string; id: string; date: number };
  export type PDFHistory = PDFHistoryItem[];
</script>

<script lang="ts">
  import { onMount } from "svelte";
  import Layout from "../layout.svelte";

  let time = new Date();
  $: now = time.getTime();

  let history = localStorage.getItem("history");
  let items: PDFHistory | false = history && JSON.parse(history);
  if (items) items.sort((a, b) => (a.date < b.date ? 1 : -1));

  const units = {
    year: 86_400_000 * 365, // 365 days
    month: 31_536_000_000 / 12, // 1/12 year
    day: 3_600_000 * 24, // 24 hours
    hour: 60_000 * 60, // 60 minutes
    minute: 1000 * 60, // 60 seconds
    second: 1000, // 1000 ms
  };

  const formatter = new Intl.RelativeTimeFormat("en", { numeric: "auto" });

  const getRelativeTime = (d1: Date, d2 = new Date()): string => {
    const elapsed = d1.getTime() - d2.getTime();

    for (const u in units) {
      if (Math.abs(elapsed) > units[u as keyof typeof units] || u == "second") {
        return formatter.format(
          Math.round(elapsed / units[u as keyof typeof units]),
          u as Intl.RelativeTimeFormatUnit
        );
      }
    }
    return ""; // if it somehow failed
  };

  onMount(() => {
    const interval = setInterval(() => {
      time = new Date();
    }, 10000);

    return () => {
      clearInterval(interval);
    };
  });
</script>

<Layout back>
  <svelte:fragment slot="heading">History</svelte:fragment>
  <ul class="history-container">
    {#if items}
      {#each items as item}
        <li class="history-item">
          <a href={`/pdf/${item.id}`}>
            <span class="history-item-name">{item.name}<small>.pdf</small></span
            >
            <span class="history-item-date">
              {getRelativeTime(new Date(item.date), new Date(now))} • {new Date(
                item.date
              )
                .toISOString()
                .split("T")[0]}
            </span>
          </a>
        </li>
      {/each}
    {:else}
      <p class="no-history">
        you haven't summarized any PDFs — <a class="link" href="/summarize"
          >yet...</a
        >
      </p>
    {/if}
  </ul>
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
  }
  .history-item:not(:first-child) {
    margin: 5px 0;
  }
  .history-item a {
    text-decoration: none;
  }
  .history-item-name {
    font-weight: 600;
    color: var(--fg-l1);
    display: block;
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
