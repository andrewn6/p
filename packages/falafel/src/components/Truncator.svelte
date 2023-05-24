<script lang="ts">
  export let breakpoint: number = 300;
  const LENIENCE = 20;

  function setTruncationStatus(node: HTMLSpanElement) {
    const bcr = node.getBoundingClientRect();
    const truncate = shouldBeTruncated(bcr.width, breakpoint);
    if (truncate) {
      node.classList.add("truncate");
      node.style.setProperty(
        "--truncate-width",
        `${breakpoint.toString()}px`
      );
      node.style.setProperty(
        "--width-not-shown",
        (bcr.width - breakpoint).toString()
      )
    }
  }
  function shouldBeTruncated(
    elementWidth: number,
    breakpoint: number
  ): boolean {
    // if it's innocent, drop all the charges against it
    if (elementWidth < breakpoint) return false;
    // however, if it's guilty, determine by how much
    const diff = elementWidth - breakpoint;
    // if it's not that bad, let it off
    if (diff < LENIENCE) return false;
    // if it's pretty bad, don't let it go unpunished
    else return true;
  }
</script>

<span use:setTruncationStatus><slot /></span>

<style>
  span {
    white-space: nowrap;
  }
  :global(.truncate) {
    --truncate-width: 200px;
    width: var(--truncate-width);
    display: inline-block;
    white-space: pre;
    overflow: hidden;
    vertical-align: text-bottom;
    position: relative;
    -webkit-mask-image: linear-gradient(to right, white 80%, transparent 100%);
    mask-image: linear-gradient(to right, white 80%, transparent 100%);
    text-indent: 0px;
    transition: text-indent 0.3s ease-in-out;
  }

  :global(.truncate:hover) {
    transition: text-indent linear;
    transition-duration: calc(calc(var(--width-not-shown) / 40) * 1s);
    text-indent: calc(var(--width-not-shown) * -1px);
    -webkit-mask-image: none;
    mask-image: none;
  }
</style>
