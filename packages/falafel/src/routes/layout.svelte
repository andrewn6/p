<script lang="ts">
  import { scale } from "../animations";
  export const ssr = false;
  export const prerender = true;

  export let back = false;

  const SCALE_ANIMATION = {
    duration: 300,
    factor: 0.05,
    isReversed: back ? 1 : 0,
    offset: back ? 0.05 : 0,
  };
</script>

<div class="app">
  <div
    in:scale={{ ...SCALE_ANIMATION, delay: 200 }}
    out:scale={SCALE_ANIMATION}
    class="container"
  >
    {#if back}
      <h2 class="subheading"><a href="/" class="link-back">Back</a></h2>
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

<style>
  .link-back {
    transition: 0.2s;
  }
  .link-back:hover {
    color: var(--fg-l1);
  }
  .link-back::before {
    display: inline-block;
    content: "←";
    margin-right: 0.3em;
    transition: 0.2s translate;
  }
  .link-back:hover::before {
    translate: -4px 0;
  }
</style>
