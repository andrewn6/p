# p

small tool that takes a PDF file, summarizes it

made this because some of my classes can have super long power points that I don't really wanna go through, and i like automating things.

hosted on p.nijmeh.world if you wanna try it out! (soon)

## tech
- python for backend
- svelte for the UI
- spaCy for NLP

## folder breakdown
- `kibbeh` sanic API, has endpoints to summarize/get files
- `falafel` svelte frontend for `kibbeh`'s functionality

## api design

### `POST /summarize`

append a PDF/PPTX file to FormData under the field `file`

returns 
```jsonc
{ id: "[id]" }
```
... which you can then use to fetch the completed summarization from `/summarization/[id]`

example using curl
```
curl -X POST -F "file=@test.pdf" http://localhost:8080/upload
```

### `GET /summarization/[id]`

get a summarization. returns:
```jsonc
{
    "text": "text",         // bla bla bla
    "name": "filename",     // the original filename
    "ext": "pptx",          // the original extension
    "date": 1686509446940   // when the summarization was completed
}

example using curl
```
curl -0 -J -L http://localhost:8080/summarization/9a973399-deb1-4ec2-b536-83e03f527411`
```