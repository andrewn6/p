<script lang="ts">
  import { scale } from "../animations";
  export const ssr = false;
  export const prerender = true;

  export let back = false;
</script>

<div class="app">
  <div
    in:scale={{
      duration: 300,
      delay: 200,
      isReversed: back ? 1 : 0,
      offset: back ? 0.1 : 0,
    }}
    out:scale={{
      duration: 300,
      isReversed: back ? 1 : 0,
      offset: back ? 0.1 : 0,
    }}
    class="container"
  >
    {#if back}
      <h2 class="subheading"><a href="/">&larr; Back</a></h2>
    {/if}
    <h1 class="heading"><slot name="heading" /></h1>
    <slot />
  </div>
</div>

<footer>
  ©{new Date().getUTCFullYear()}
  <a class="link" href="https://nijmeh.world">Andrew</a>
  &
  <a class="link" href="https://pineapplerind.xyz">PineappleRind</a>
</footer>
