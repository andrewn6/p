import MessageComponent from "./Popup.svelte";

export enum PopupType {
	Info = "info",
	Success = "success",
	Error = "error",
}

let lastShown = Date.now();
let currentId = 0;

const wait = (ms: number) => new Promise((resolve) => setTimeout(resolve, ms));

/** A toast popup component used for info messages, successes, or errors. */
export class Popup {
	options: any;
	duration: number;
	element?: Element;
	Manager: PopupManager = PopupManager.instance;

	constructor(
		content: string,
		type: PopupType,
		duration: number,
		title?: string,
	) {
		// Create a message
		let id = `popup${(currentId++).toString(16)}`;
		let options: any = { id: id, description: content, type };
		if (title) options.title = title;

		this.options = options;
		this.duration = duration;
	}

	async show() {
		if (Date.now() - lastShown < 200) return; // no spam thanks
		lastShown = Date.now();
		await this.Manager.showMessage(this);
		return this;
	}
}

/**
 * Manages the message queue, and removes the oldest messages if the total message count overflows MAX_QUEUE_LENGTH.
 *
 * We don't export this as it's managed directly by {@link Popup}.
 */
class PopupManager {
	/** Where messages will appear */
	#container: HTMLDivElement;
	#queue: Popup[] = [];
	/** We don't want more than one MessageManager active at once */
	public static instance: PopupManager = new PopupManager();
	static readonly MAX_QUEUE_LENGTH = 5;
	static readonly MESSAGE_PADDING = 4;

	/** Create a message container, hopefully only once */
	private constructor() {
		const container: HTMLDivElement = document.createElement("div");
		container.classList.add("popup-container");
		document.body.append(container);
		this.#container = container;
	}

	async showMessage(message: Popup) {
		let messageElement = new MessageComponent({
			props: message.options,
			target: this.#container,
		}).$$.root.querySelector(`[data-id=${message.options.id}]`);

		if (!(messageElement instanceof Element))
			throw new Error("Popup is not an Element");
		message.element = messageElement;
		this.#queue.push(message);
		const overflow = this.#queue.length - PopupManager.MAX_QUEUE_LENGTH;
		for (let i = 0; i < overflow; i++) this.removeTopMessage();
		this.#container.append(message.element);
		this.animateContainerUp(message);
		await wait(message.duration);
		this.removeTopMessage();
	}

	async removeTopMessage() {
		const message = this.#queue.shift();
		if (!message) return;
		message.element?.classList.add("hidden");
		await wait(200); // Transition length
		message.element?.remove();
	}

	/** Animate all messages up when a message appears to make the UI smoother and less confusing */
	async animateContainerUp(message: Popup) {
		const newMessageHeight =
			PopupManager.MESSAGE_PADDING +
			(message.element?.getBoundingClientRect().height || 0);
		this.#container.style.bottom = `-${newMessageHeight}px`;
		// skip an event loop
		await wait(10);
		
		this.#container.style.transition = "0.2s";
		this.#container.style.bottom = "0px";
		await wait(200);
		this.#container.style.transition = "0s";
	}
}
