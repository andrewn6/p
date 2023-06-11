export const API_URL = "http://localhost:3000";

/**
 * These are the default routes. 
 * If `1` is the current route, `0` is the route's 
 * previous page.
 */
export const pageStructure = [
    ["/", "/"],
    ["/", "/summarize",],
    ["/history", "/summarization/[id]",],
    ["/", "/history",],
]

export const allowedFileTypes = ["application/pdf", "application/vnd.openxmlformats-officedocument.presentationml.presentation"]