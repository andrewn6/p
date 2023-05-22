<script>
  import Button from "../components/Button.svelte";
  import Layout from "./layout.svelte";
</script>

<Layout>
  <svelte:fragment slot="heading">PDF Summarizer</svelte:fragment>
  <div class="flex">
    <Button link="/summarize" primary>summarize new pdf</Button>
    <Button>browse history</Button>
  </div>
</Layout>
