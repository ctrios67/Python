#! /usr/bin/env python3
#! stripViaRegex.py
import re
spaces = '        OH MAN       '
print(spaces)
stripSpaceBeg = re.compile(r'^(\s)+')
stripSpaceEnd = re.compile(r'(\s)+$')
newText = stripSpaceBeg.sub('', spaces)
newText = stripSpaceEnd.sub('', newText)
print(newText)
