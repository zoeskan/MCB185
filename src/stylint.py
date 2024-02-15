#!/usr/bin/env python3

import argparse
import re
import sys

parser = argparse.ArgumentParser(description='MCB185 style-checker')
parser.add_argument('file', help='path to python file(s)',
	nargs='+')
parser.add_argument('-r', '--report-level', type=int, default=2,
	metavar='[0-2]', help='reporting level [%(default)i]')
arg = parser.parse_args()

issues = {
	'indent': r'^( +\w+)',
	'space':  r'(\w+\s+\()',
	'white':  r'(\t | \t)',
	'comma':  r'(\w+,\w+)',
	'mixed':  r'([a-z]+[A-Z]+|[A-Z]+[a-z]+)',
	'caps' :  r'(def\s+[A-Z])'
}

explain = {
	'indent': 'not allowed to indent with spaces (check editor settings)',
	'space': 'there should be no space between a function name and opening (',
	'white': 'mixing spaces and tabs in whitespace can look weird',
	'comma': 'there should be a space after a comma',
	'mixed': 'use snake_case instead of mixedCase',
	'caps' : 'function names should be lowercase',
	'max80': 'line length exceeds 80 characters',
}

keywords = (
	'None', 'False', 'True',
	'and', 'or', 'not',
	'for', 'while', 'break', 'continue', 'in',
	'if', 'elif', 'else',
	'try', 'except', 'raise',
	'return', 'yield',
)

def in_string(found, line):
	p1 = line.find("'")
	p2 = line.find(found, p1)
	p3 = line.find("'", p2)
	if p1 < p2 and p2 < p3: return True
	return False

def style_issues(file):
	problems = []
	with open(file) as fp:
		n = 0
		for line in fp:
			n += 1

			# comments: only check for length
			if line.startswith('#'):
				if len(line) > 80: problems.append( (n, 'max80', line) )
				continue

			# long comments: also only length
			if line.startswith('"""') or line.startswith("'''"):
				for line in fp:
					n += 1
					if len(line) > 80: problems.append( (n, 'max80', line) )
					if line.startswith('"""') or line.startswith("'''"): break
				continue

			# style issues
			if len(line) > 80: problems.append( (n, 'max80', line) )
			for problem, pattern in issues.items():
				m = re.search(pattern, line)
				if m:
					found = m.group(1)
					if problem == 'space':
						kwfound = False
						for kw in keywords:
							if found.startswith(kw):
								kwfound = True
								break
						if kwfound: continue
					if problem == 'space' and in_string(found, line): continue
					if problem == 'mixed' and found in keywords: continue
					if problem == 'mixed' and '#' in line: continue
					if problem == 'mixed' and '"' in line: continue
					if problem == 'mixed' and "'" in line: continue
					line = line.rstrip()
					problems.append( (n, problem, line) )
	return problems

tell = {}
for file in arg.file:
	if not file.endswith('.py'):
		print(f'skipping non-python file: {file}', file=sys.stderr)
		continue

	probs = style_issues(file)

	if len(probs) == 0:
		print(file, 'is clean')
		continue
	else:
		print(file, 'has style issues')
	if arg.report_level == 0: continue

	print('Line Report')
	for n, prob, code in probs:
		tell[prob] = True
		print(f'  Line {n} ({prob}): {code[:50]}')

if arg.report_level == 2 and tell:
	print('Detailed Explanations')
	for prob in tell:
		print(f'  {prob}: {explain[prob]}')
