<script lang="ts">
  import { API_URL } from "../../../constants";
import Layout from "../../layout.svelte";

  export let data;
</script>

<Layout back>
  <svelte:fragment slot="heading">PDF: {data.id}</svelte:fragment>
  <iframe title="PDF" width="100%" height="100%" src={`${API_URL}/pdf/${data.id}`}></iframe>
</Layout>
