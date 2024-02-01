import re
import sys

if len(sys.argv) != 2: sys.exit(f'usage: {sys.argv[0]} file.py')

issues = {
	'indent': r'^( +\w+)',
	'space':  r'(\w+)\s+\(',
	'comma':  r'(\w+,\w+)',
	'mixed':  r'([a-z]+[A-Z]+|[A-Z]+[a-z]+)',
	'length': r'(^[^#].{81,}$)',
}

keywords = (
	'None', 'False', 'True',
	'and', 'or', 'not', 
	'for', 'while', 'break', 'continue', 'in',
	'if', 'elif', 'else',
	'try', 'except', 'raise',
	'return', 'yield',
)

clean = True
with open(sys.argv[1]) as fp:
	n = 0
	for line in fp:
		n += 1
		if line.startswith('#'): continue
		if line.startswith('"""') or line.startswith("'''"):
			for line in fp:
				n += 1
				if line.startswith('"""') or line.startswith("'''"): break
		
		for problem, pattern in issues.items():
			m = re.search(pattern, line)
			if m:
				found = m.group(1)
				if problem == 'space' and found in keywords: continue
				if problem == 'mixed' and found in keywords: continue
				if problem == 'mixed' and '#' in line: continue
				if problem == 'mixed' and '"' in line: continue
				if problem == 'mixed' and "'" in line: continue
				print(f'{n}\t{problem}\t"{line[:-1]}"')
				clean = False

if clean: print(sys.argv[1], 'is clean')
