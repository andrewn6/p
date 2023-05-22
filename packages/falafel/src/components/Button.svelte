<script lang="ts">
  export let primary = false;
  export let link: string | false = false;
</script>

<svelte:element
  this={link ? "a" : "button"}
  {...{ href: link }}
  class="button"
  class:primary
>
  <slot />
</svelte:element>

<style>
  .button {
    border-radius: var(--radius-m);
    padding: 10px 20px;
    border: 0;
    font: var(--font-text);
    font-weight: 500;
    background: var(--bg-l2);
    margin: 5px;
    transition: 0.1s;
    cursor: pointer;
    text-decoration: none;
  }
  .button:hover {
    scale: 1.005;
    background: var(--bg-l3);
  }
  .button:active {
    scale: 0.995;
  }
  .primary {
    color: var(--bg-l0);
    background: var(--accent-gradient);
    background-size: 130%;
  }

  .primary:hover {
    background: var(--accent-gradient);
    background-position: 100% 10%;
  }
</style>
