import { cubicIn, cubicOut } from "svelte/easing";

export function scale(
    node: HTMLElement,
    { duration = 200, offset = 0, delay = 0, isReversed = 0 }
) {
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