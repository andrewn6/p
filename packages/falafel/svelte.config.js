import adapter from "@sveltejs/adapter-static";
import preprocess from "svelte-preprocess";

/** @type {import('@sveltejs/kit').Config} */
const config = {
	preprocess: preprocess(),
	kit: {
		adapter: adapter({
			pages: "build",
			assets: "build",
			strict: true,
		}),
		alias: {
			"@components": "./src/components/*"
		}
	},
};

export default config;
