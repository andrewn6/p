import adapter from "@sveltejs/adapter-auto";
import preprocess from "svelte-preprocess";

/** @type {import('@sveltejs/kit').Config} */
const config = {
	preprocess: preprocess(),
	kit: {
		adapter: adapter({
			pages: "build",
			assets: "build",
		}),
		alias: {
			"@components": "./src/components/*"
		}
	},
};

export default config;
