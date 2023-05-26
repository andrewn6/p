<script lang="ts">
  import { scale } from "../animations";
  import { beforeNavigate } from "$app/navigation";
  
  export let back = false;

  let scaleAnimation = {
    duration: 300,
    factor: 0.05,
    // these two properties are set blindly, which causes issues when
    // moving backwards in browser history, i.e. when delta is negative
    isReversed: back ? 1 : 0,
    offset: back ? 0.05 : 0,
  };

  beforeNavigate(async (navigation) => {
    scaleAnimation.isReversed = navigation.delta === -1 ? 1 : 0;
    scaleAnimation.offset = navigation.delta === -1 ? 0.05 : 0;
  });
</script>

<div class="app">
  <div
    in:scale={{ ...scaleAnimation, delay: scaleAnimation.duration / 2 }}
    out:scale={scaleAnimation}
    class="container"
  >
    {#if back}
      <h2 class="subheading">
        <a href="javascript:history.back()" class="link-back">Back</a>
      </h2>
    {/if}
    <h1 class="heading"><slot name="heading" /></h1>
    <main><slot /></main>
  </div>
</div>

<footer>
  ©{new Date().getUTCFullYear()}
  <a class="link" href="https://nijmeh.world">Andrew</a>
  &
  <a class="link" href="https://pineapplerind.xyz">PineappleRind</a>
</footer>

<style global>
  * {
    margin: 0;
    box-sizing: border-box;
  }

  body {
    font: var(--font-text);
    line-height: 1.3;
  }

  .app {
    height: 100dvh;
    width: 100dvw;
    display: grid;
    grid-template-rows: 1fr;
    grid-template-columns: 1fr;
    place-items: center;
    overflow: hidden;
  }

  .app > .container {
    grid-row: 1;
    grid-column: 1;
    min-width: min(clamp(200px, 40ch, 600px), 100%);
  }

  .flex {
    display: flex;
  }

  .heading {
    font: var(--font-heading);
    white-space: nowrap;
  }

  .subheading,
  .subheading a {
    font: var(--font-subheading);
    color: var(--fg-l2);
    text-decoration: none;
  }

  footer {
    font: var(--font-footer);
    color: var(--fg-l2);
    position: absolute;
    bottom: 10px;
    width: 100vw;
    width: 100dvw;
    text-align: center;
  }

  .transition-enforcement {
    display: grid !important;
    align-items: start;
  }

  .transition-enforcement > * {
    grid-column: 1/2;
    grid-row: 1/2;
  }

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

  .link {
    text-underline-offset: 2px;
    text-decoration: underline;
    cursor: pointer;
    color: var(--fg-l1);
  }

  .link:hover {
    text-underline-offset: 3px;
  }
</style>
