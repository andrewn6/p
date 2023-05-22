<script lang="ts">
  import { cubicIn, cubicOut } from "svelte/easing";

  let dropZone: HTMLDivElement, fileInput: HTMLInputElement;
  let selectedPDF: File, active: boolean = false;
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
    if (file && file.type !== "application/pdf")
      return alert("Please only drop PDFs");

    selectedPDF = file!;
  }

  function scale(node: HTMLElement, { duration = 200, offset = 0, delay = 0, isReversed = 0 }) {
    return {
      duration,
      delay,
      css: (t: number) => {
        let eased = t;
        if (isReversed) eased = cubicIn(1 - eased);
        else eased = cubicOut(eased);

        const computedScale = (1 - eased) * 0.1 - (offset - 1);
        console.log(
          `ComputedScale for ${node.tagName} for t ${t} is ${computedScale}`
        );
        return `opacity: ${t}; transform: scale(${computedScale})`;
      },
    };
  }
</script>

<div
  on:dragenter={handleDragEnter}
  on:dragleave={handleDragLeave}
  on:drop={handleDrop}
  on:dragover={(e) => e.preventDefault()}
  bind:this={dropZone}
  class="file-choose transition-enforcement"
  class:active
>
  {#if selectedPDF}
    <div
      in:scale={{ duration: 300, delay: 200, offset: 0 }}
      class="selected-file"
    >
      {selectedPDF.name}
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
    on:input={(e) => updateSelectedFile(Array.from(e.target.files))}
    style="display: none"
    bind:this={fileInput}
  />
</div>

<style>
  .file-choose {
    padding: 8px;
    margin: 5px 0;
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
  }

  .selected-file {
    padding: 10px;
    width: 100%;
    background: var(--bg-l2);
    border-radius: var(--radius-m);
  }
</style>
