import { cubicIn, cubicOut } from "svelte/easing";

export function scale(
	_node: HTMLElement,
	{ duration = 200, offset = 0, delay = 0, factor = 0.1, isReversed = 0 },
) {
	return {
		duration,
		delay,
		css: (t: number) => {
			let eased = 1 - t;
			if (isReversed) eased = cubicOut(1 - eased);
			else eased = cubicIn(eased);

			const computedScale = eased * factor - (offset - 1);
			// console.log(`ComputedScale for ${node.tagName} for t ${t} is ${computedScale}`);
			return `opacity: ${t}; transform: scale(${computedScale})`;
		},
	};
}
