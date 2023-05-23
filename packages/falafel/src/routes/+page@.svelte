<script>
  import Button from "@components/Button.svelte";
  import Layout from "./layout.svelte";
</script>

<Layout>
  <svelte:fragment slot="heading">PDF Summarizer</svelte:fragment>
  <div class="flex" style="gap: 10px">
    <Button fullWidth link="/summarize" primary>summarize new pdf</Button>
    <Button fullWidth link="/history">browse history</Button>
  </div>
</Layout>
