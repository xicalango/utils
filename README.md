utils
=====

Some useful utility scripts.

jsonql.py
---------

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

```bash
# print whole file:
$ jsonql.py example.json

# print value of menu.id:
$ jsonql.py example.json menu.id

# print second menuitem:
$ jsonql.py example.json menu.popup.menuitem[1]
```

flattenDict.py
--------------

A method to convert a list of dictionaries to a list of lists in a csv style.

### Usage as method:

```python
listOfDicts = [
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

listOfLists = flattenDict(listOfDicts, includeHeaders=True)
```

Value of listOfLists:

```python
[
  ['onclick', 'value'], #headers
  ['CreateNewDoc()', 'New'], 
  ['OpenDoc()', 'Open'],
  ['CloseDoc()', 'Close']
]
```

### Usage as command:

Suppose you have a file "listOfDicts.json" which contains the listOfDicts structure from the example above.

```bash
$ flattenDict.py listOfDicts.json

"onclick","value"
"CreateNewDoc()","New"
"OpenDoc()","Open"
"CloseDoc()","Close"
```
