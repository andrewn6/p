import { writable } from "svelte/store";

export let direction = writable(1);
export let currentAnimationDirection = writable(1);