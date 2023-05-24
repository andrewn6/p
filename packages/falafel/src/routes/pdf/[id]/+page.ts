import type { Load } from "@sveltejs/kit"

// Expose the current ID the user's on
// to the main pdf viewer frontend
export const load: Load = (data) => {
    return {
        id: data.params.id
    }
}