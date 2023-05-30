<script lang="ts">
  import { scale } from "../animations";
  import { lastNavigationDelta } from "../stores";
  import { page } from "$app/stores";
  import { beforeNavigate } from "$app/navigation";
  import { pageStructure } from "../constants";

  export let back = false;

  const SCALE_AMT = 0.03;
  let baseScaleAnimation = {
    duration: 300,
    factor: SCALE_AMT,
    isReversed: $lastNavigationDelta === -1 ? 1 : 0,
    offset: $lastNavigationDelta === -1 ? SCALE_AMT : 0,
  };

  beforeNavigate(async (navigation) => {
    lastNavigationDelta.set(
      determineNavigationDelta(
        navigation.from?.route.id,
        navigation.to?.route.id
      )
    );
  });

  function arraysEqual(a: any[], b: any[]) {
    for (var i = 0; i < a.length; ++i) if (a[i] !== b[i]) return false;
    return true;
  }

  function determineNavigationDelta(
    from: string | undefined | null,
    to: string | undefined | null
  ): 1 | -1 {
    // Find all candidates for fromRoute and toRoute
    // example: if we are going `from` / `to` /history,
    // fromRoute = [["/", "/"], ["/summarize", "/"], ["/history", "/"]]
    let fromRoute = pageStructure.filter((arr) => arr.includes(from || "/"));
    // toRoute = [["/history", "/"], ["/summarization/[id]", "/history"]]
    let toRoute = pageStructure.filter((arr) => arr.includes(to || "/"));

    // highlight everything in fromRoute that toRoute also has
    let match = fromRoute.find((route) => toRoute.includes(route)) || [];

    // now determine direction
    if (arraysEqual([from, to], match)) return 1;
    else if (arraysEqual([to, from], match)) return -1;
    // If this navigation checks none of our boxes, assume we're going back
    else return -1;
  }

  function determinePreviousPage(): string {
    let previousPage = pageStructure.find(
      (arr) => arr[1] === $page.route.id
    ) || ["/"];
    return previousPage[0];
  }

</script>

<div class="app">
  <div
    in:scale={{
      ...baseScaleAnimation,
      delay: 150,
      isReversed: $lastNavigationDelta !== -1 ? 1 : 0,
      offset: $lastNavigationDelta !== -1 ? SCALE_AMT : 0,
    }}
    out:scale={{
      ...baseScaleAnimation,
      isReversed: $lastNavigationDelta === -1 ? 1 : 0,
      offset: $lastNavigationDelta === -1 ? SCALE_AMT : 0,
    }}
    class="container"
  >
    {#if back}
      <!-- TODO find a better way to do this -->
      <a href={determinePreviousPage()} class="link-back subheading">Back</a>
    {/if}
    <main>
      <h1 class="heading"><slot name="heading" /></h1>
      <slot />
    </main>
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

  button {
    padding: 0;
    background: 0;
    border: 0;
    cursor: pointer;
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

  .link-back:active {
    scale: 0.99;
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
