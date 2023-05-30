<script lang="ts">
  import { PopupType } from "./PopupManager";
  export let id: string;
  export let title: string | null = null;
  export let description: string;
  export let type: PopupType = PopupType.Info;
</script>

<div class={`${type} popup`} data-id={id}>
  {#if title}
    <p class="popup-title">{title}</p>
    <p class="popup-description smaller">{description}</p>
  {:else}
    <p class="popup-description">{description}</p>
  {/if}
</div>

<style>
  :global(.popup-container) {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    width: 100vw;
    display: flex;
    align-items: center;
    flex-direction: column;
    padding-bottom: 15px;
  }

  .popup {
    width: fit-content;
    min-width: 200px;
    margin: 4px;
    padding: 7px 14px;
    background: var(--bg-l1);
    border: 1px solid var(--border);
    border-radius: var(--radius-m);
    transform-origin: bottom center;
    transition: 0.2s;
    animation: popup-come-in 0.2s;
    backdrop-filter: blur(10px);
  }

  .popup.hidden {
    scale: 0.9;
    opacity: 0;
  }

  .popup.error {
    background: hsla(0, 100%, 39%, 0.2);
    border: 1px solid hsla(0, 100%, 39%, 0.6);
    box-shadow: 0 3px 40px hsla(0, 100%, 39%, 0.577);
    animation: popup-come-in 0.2s, popup-error-shadow both 4s;
  }
  @keyframes popup-error-shadow {
    from { box-shadow: 0 3px 20px 10px hsla(0, 100%, 39%, 0.577); }
    to { box-shadow: 0 3px 30px hsla(0, 100%, 39%, 0.377); }
  }

  .popup.success {
    background: hsla(114, 100%, 39%, 0.2);
    border: 1px solid hsla(114, 100%, 39%, 0.3);
  }

  .popup-title {
    font-size: 1.1em;
    font-weight: bold;
  }

  .popup-description.smaller {
    font: var(--font-quiet);
    color: var(--fg-2);
  }

  @keyframes popup-come-in {
    from {
      scale: 0.9;
      opacity: 0;
    }
  }
</style>
