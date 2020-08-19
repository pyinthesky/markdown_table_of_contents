#!/usr/bin/python3

# Someone on stackoverflow had posted a ruby implementation of this, and I have translated it to python for kicks

import urllib.parse as parse
import sys
import os
import re

pound_forbidden_words = ['define', 'pragma', 'ifdef', 'endif']

def main():
  if len(sys.argv[1]) == 0:
    print("missing input file name")
    return
  if not os.path.exists(sys.argv[1]):
    print("bad input file path")
  
  pound_str     = '^#(%s)|table of contents|^# ' % '|'.join(pound_forbidden_words)
  pound_matcher = re.compile(pound_str, flags=re.I)
  
  with open(sys.argv[1]) as fin:
    inside_code_snippet = False
    for line in fin.readlines():
      if line.startswith('```'):
        inside_code_snippet = not inside_code_snippet
      if pound_matcher.search(line) or inside_code_snippet or not line.startswith('#'):
        continue
      title   = line.replace('#', '').strip()
      h       = title.replace(' ', '-').lower()
      href    = parse.quote(h)
      indent  = "    " * (len(re.search(r'^(#+)', line).group(1)) - 2)
      print(f"{indent}* [{title}](#{href})")
 
 if __name__ == "__main__":
  main()
