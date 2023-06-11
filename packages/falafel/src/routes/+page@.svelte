<script>
  import Button from "@components/Button.svelte";
  import Layout from "./layout.svelte";
</script>

<Layout>
  <svelte:fragment slot="heading">File Summarizer</svelte:fragment>
  <nav class="flex" style="gap: 10px">
    <Button fullWidth link="/summarize" primary>summarize new file</Button>
    <Button fullWidth link="/history">browse history</Button>
  </nav>
</Layout>
