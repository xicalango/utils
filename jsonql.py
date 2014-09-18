#!/usr/bin/env python3

import json
from argparse import ArgumentParser
import re


parser = ArgumentParser()

parser.add_argument('file')
parser.add_argument('query', nargs='?')

args = parser.parse_args()


jsonFile = None

with open(args.file, "r") as f:
  jsonFile = json.load(f)

splitQuery = []

if args.query != None:
  splitQuery = args.query.split(".")

qRegex = r"^(?P<prop>.*?)($|\[(?P<idx>[0-9]+)\])"

cur = jsonFile

for q in splitQuery:
  m = re.search(qRegex, q)

  prop = m.group('prop')
  idx = int(m.group('idx')) if m.group('idx') != None else None

  if idx != None:
    cur = cur[prop][idx]
  else:
    cur = cur[prop]



print(json.dumps(cur, indent=2, sort_keys=True))
