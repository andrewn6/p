# kibbeh

`api`

## endpoints

### `POST /summarize`

append a PDF/PPTX file to FormData under the field `file`

### `GET /summarization/[id]`

get a summarization. returns:
```jsonc
{
    "text": "text",         // bla bla bla
    "name": "filename",     // the original filename
    "ext": "pptx",          // the original extension
    "date": 1686509446940   // when the summarization was completed
}
```
---

![image of kibbeh](https://upload.wikimedia.org/wikipedia/commons/8/88/Kibbeh3.jpg)
