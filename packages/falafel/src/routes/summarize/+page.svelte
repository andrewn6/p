<script>
  import Button from "../../components/Button.svelte";
  import FileChooser from "../../components/FileChooser.svelte";
  import Layout from "../layout.svelte";
</script>

<Layout back>
  <svelte:fragment slot="heading">New PDF</svelte:fragment>
  <FileChooser/>
  <Button primary fullWidth>summarize ⚡️</Button>
</Layout>
