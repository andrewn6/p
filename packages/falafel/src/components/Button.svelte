<script lang="ts">
  import Loader from "@components/Loader.svelte";

  export let primary: boolean = false;
  export let inProgress: boolean = false;
  export let fullWidth: boolean = false;
  export let link: string | null = null;
</script>

<svelte:element
  this={link ? "a" : "button"}
  {...{ href: link }}
  class="button"
  class:primary
  class:inProgress
  class:fullWidth
  on:click
  {...$$restProps}
>
  <slot />
  {#if inProgress}
    <Loader />
  {/if}
</svelte:element>

<style>
  .button {
    border-radius: var(--radius-m);
    padding: 10px 20px;
    border: 0;
    font: var(--font-text);
    font-weight: 500;
    background: var(--bg-l2);
    margin: 8px 0;
    transition: 0.1s;
    cursor: pointer;
    text-decoration: none;
    text-align: center;
    display: block;
    line-height: inherit;
  }
  .button:not([disabled], .inProgress):hover {
    scale: 1.005;
    background: var(--bg-l3);
  }
  .button:not([disabled], .inProgress):active {
    scale: 0.995;
  }
  .primary {
    color: var(--bg-l0);
    background: var(--accent-gradient);
    background-size: 130%;
    box-shadow: var(--shadow);
  }
  .primary:not([disabled], .inProgress):hover {
    background: var(--accent-gradient);
    background-position: 100% 10%;
  }
  .fullWidth {
    width: 100%;
  }
  .button[disabled] {
    opacity: 0.3;
    cursor: not-allowed;
    box-shadow: 0 0 0 0 transparent;
  }
  .button.inProgress {
    position: relative;
    z-index: 1;
    background: var(--bg-l2);
    color: var(--fg-l2);
    cursor: progress;
  }
</style>
