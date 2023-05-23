# p

small tool that takes a PDF file, summarizes it

made this because some of my classes can have super long power points that I don't really wanna go through, and i like automating things.

hosted on p.nijmeh.world if you wanna try it out! (soon)

## tech
- python for backend
- svelte for the UI
- spaCy for NLP

## folder breakdown
- `kibbeh` summarizes the pdfs and outputs them, it is served as a Sanic API
- `falafel` svelte frontend for `kibbeh`'s functionality

## api design
### `POST /summarize`
append a PDF file to FormData under the field `pdf_file`

returns `{ id: "[PDF-ID]" }` which you can then use to download the pdf from `/pdf/[id]`

example using curl:
- `curl -X POST -F "pdf_file=@test.pdf" http://localhost:8080/upload`

### `GET /pdf/[id]`
- `curl -0 -J -L http://localhost:8080/pdf/[id]`

returns the pdf with the corresponding id
