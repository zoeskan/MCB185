import re
import sys

if len(sys.argv) != 2: sys.exit(f'usage: {sys.argv[0]} file.py')

issues = {
	'tabs':  '^( +\w+)',
	'space': '(\w+\s+\()',
	'comma': '(\w+,\w+)',
	'mixed': '([a-z][A-Z])',
	'long':  '(^[^#].{81,}$)',
}

with open(sys.argv[1]) as fp:
	n = 0
	for line in fp:
		n += 1
		for infraction, pattern in issues.items():
			m = re.search(pattern, line)
			if m:
				found = m.group(1)
				print(f'{n}\t{infraction}\t"{found}"')
				break
