#!/usr/bin/env python2

import fileinput
import csv
import json
import sys

def flattenDict(dictionaryList, includeHeader = False):
  lines = []
  columnNameToColumn = {}
  currentColumn = 0

  for dictionary in dictionaryList:
    line = {}
    
    for k,v in dictionary.items():
      if k not in columnNameToColumn:
        columnNameToColumn[k] = currentColumn
        currentColumn += 1

      line[columnNameToColumn[k]] = v

    lines.append(line)

  columns = list(map(lambda t: t[0], sorted(columnNameToColumn.items(), key = lambda x: x[1]))) # extract column names, sorted by column id
  numColumns = len(columns)

  rows = []

  if includeHeader:
    rows.append(columns) # insert header

  for l in lines:
    row = [None] * numColumns

    for colId, value in l.items():
      row[colId] = value
    
    rows.append(row)


  return rows


def main():
  
  jsonData = json.loads("".join((fileinput.input())))

  listData = flattenDict(jsonData, includeHeader = True)

  out = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)
  for row in listData:
    out.writerow(row)

if __name__ == '__main__':
  main()
