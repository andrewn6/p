<script lang="ts">
  import { scale } from "../animations";
  import { allowedFileTypes } from "../constants";
  import { Popup, PopupType } from "./PopupManager";
  import Truncator from "./Truncator.svelte";

  export let allowed: string[] = allowedFileTypes;
  export let selectedFile: File | null,
    active: boolean = false;

  function handleDragEnter() {
    active = true;
  }
  function handleDragLeave() {
    active = false;
  }
  function handleDrop(e: DragEvent) {
    e.preventDefault();
    active = false;
    if (e.dataTransfer?.items) {
      // Use DataTransferItemList interface to access the file(s)
      [...e.dataTransfer.items].forEach((item, i) => {
        // If dropped items aren't files, reject them
        if (item.kind !== "file") return;
        const file = item.getAsFile();
        if (!file) return;
        updateSelectedFile([file]);
      });
    } else {
      // Use DataTransfer interface to access the file(s)
      [...e.dataTransfer!.files].forEach((file, i) => {
        updateSelectedFile([file]);
      });
    }
  }
  function updateSelectedFile(files: File[] | null) {
    const file = files && files[0];
    if (file && !allowed.includes(file.type))
      return new Popup("Currently, only PDFs and PowerPoints are supported", PopupType.Error, 7000, "Error uploading file").show();

    selectedFile = file!;
  }
</script>

<div
  on:dragenter={handleDragEnter}
  on:dragleave={handleDragLeave}
  on:drop={handleDrop}
  on:dragover={(e) => e.preventDefault()}
  class="file-choose transition-enforcement"
  class:active
>
  {#if selectedFile}
    <div
      in:scale={{ duration: 300, delay: 150, offset: 0 }}
      out:scale={{ duration: 300, isReversed: 1, offset: 0.1 }}
      class="selected-file"
    >
      <Truncator breakpoint={400}>{selectedFile.name.split(".").slice(0, -1)}</Truncator><p>.{selectedFile.name.split(".").slice(-1)}</p>
    </div>
  {:else}
    <p
      out:scale={{ duration: 300, isReversed: 1, offset: 0.1 }}
      class="file-choose-placeholder"
      style="margin: 0 10px"
    >
      drop a file here, or <label for="fileUpload" class="link"
          >browse your computer</label
        >
    </p>
  {/if}
  <input
    type="file"
    id="fileUpload"
    accept={allowed.join(", ")}
    on:input={(e) => {
      // Ignore these because svelte does not have TypeScript support in markup template
      // https://github.com/sveltejs/svelte/issues/4701
      // @ts-ignore
      if (!e.target.files) return;
      // @ts-ignore
      updateSelectedFile(Array.from(e.target.files));
    }}
    style="position: fixed; opacity: 0; pointer-events: none"
  />
</div>

<style>
  .file-choose {
    padding: 8px;
    margin: 8px 0;
    width: 100%;
    min-height: 60px;
    border: 2px dashed var(--border);
    border-radius: var(--radius-m);
    box-shadow: var(--shadow);
    display: flex;
    align-items: center;
    flex-direction: column;
    background: var(--bg-l1);
  }

  .file-choose.active {
    border: 2px dashed var(--accent-1);
  }
  .file-choose.active * {
    pointer-events: none;
  }

  .file-choose-placeholder {
    font: var(--font-quiet);
    color: var(--fg-l2);
    font-style: italic;
    text-align: center;
  }

  .selected-file {
    padding: 10px;
    width: 100%;
    max-width: 500px;
    background: var(--bg-l2);
    border-radius: var(--radius-m);
    display: flex;
  }
</style>
