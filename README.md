# p

small tool that takes a PDF file, summarizes it

made this because some of my classes can have super long power points and I don't really wanna go through all of it, and i like automating things.

hosted on p.nijmeh.world if you wanna try it out!

## tech
- python for backend
- svelte for the UI
- spaCy for NLP

## folder breakdown
- `kibbeh` summarizes the pdfs and outputs them, it is served as a Sanic API
- `falafel` svelte frontend, depends on kibbeh

# api design
- /upload
  - `curl -X POST -F "pdf_file=@test.pdf" http://localhost:8080/upload` example using curl
- GET `/pdf/[id]
