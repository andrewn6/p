<script lang="ts">
  export const ssr = false;
  export const prerender = true;

  export let back = false;
</script>

<div class="app">
  <div class="container">
    {#if back}
      <h2 class="subheading"><a href="/">&larr; Back</a></h2>
    {/if}
    <h1 class="heading"><slot name="heading" /></h1>
    <slot />
  </div>
</div>

<footer>
  ©{new Date().getUTCFullYear()} <a class="link" href="https://nijmeh.world">Andrew</a> &
  <a class="link" href="https://pineapplerind.xyz">PineappleRind</a>
</footer>
