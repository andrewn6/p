<script lang="ts">
  export let name: string;
  export let color: string = "black";
</script>

<div style={`--icon: url(/icons/${name}.svg); background-color: ${color || "black"}`} />

<style>
  div {
    height: 20px;
    width: 20px;
    vertical-align: text-bottom;
    color: var(--fg-l2) !important;
    -webkit-mask: var(--icon) no-repeat center;
    mask: var(--icon) no-repeat center;
    background-color: black;
  }
</style>
