utils
=====

Some useful utility scripts.

jsonql.py
=========

A small query language for quick analyses of json files.

Suppose you have a file called "[example.json](http://json.org/example)":

```json
{
  "menu": {
    "id": "file",
    "popup": {
      "menuitem": [
        {
          "onclick": "CreateNewDoc()",
          "value": "New"
        },
        {
          "onclick": "OpenDoc()",
          "value": "Open"
        },
        {
          "onclick": "CloseDoc()",
          "value": "Close"
        }
      ]
    },
    "value": "File"
  }
}
```

Then you can access members like this:

```
# print whole file:
jsonql.py example.json

# print value of menu.id:
jsonql.py example.json menu.id

# print second menuitem:
jsonql.py example.json menu.popup.menuitem[1]
```
