utils
=====

Some useful utility scripts.

jsonql.py
=========

A small query language for quick analyses of json files.

Suppose you have a file called "example.json":

```json
{"menu": {
  "id": "file",
  "value": "File",
  "popup": {
    "menuitem": [
      {"value": "New", "onclick": "CreateNewDoc()"},
      {"value": "Open", "onclick": "OpenDoc()"},
      {"value": "Close", "onclick": "CloseDoc()"}
    ]
  }
}}
```

Then you can access members like this:

```
# print whole file:
jsonql example.json

# print value of menu.id:
jsonql example.json menu.id

# print second menuitem:
jsonql example.json menu.popup.menuitem[1]
```
