<script>
  export const ssr = false;
  export const prerender = true;

  import { page } from "$app/stores";
</script>

<div class="app">
  {#if $page.url.pathname !== "/"}
    <h2 class="subheading"><a href="/">&larr; Back</a></h2>
  {/if}
  <h1 class="heading"><slot name="heading" /></h1>
  <slot />
</div>
<footer>
  ©{new Date().getUTCFullYear()} <a href="https://nijmeh.world">Andrew</a> &
  <a href="https://pineapplerind.xyz">PineappleRind</a>
</footer>

<style>
  
</style>
