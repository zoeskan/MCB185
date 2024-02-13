import random

"""
3D6     10.4535
3D6r1   11.9691
3D6x2   13.4517
3D6d1   12.1878

DC      norm    adv     dis
5       0.795   0.960   0.638
10      0.549   0.799   0.307
15      0.295   0.502   0.084

die: 0.407
stabilize: 0.406
revive: 0.186
"""


"""
# 43
nts = 0
seq = 101                         # number of sequences
for i in range(1, seq):                  # how to delete space?
	print()
	print(f'>seq-{i}')
	r = random.randint(50, 60)
	for nts in range(r):
		print(random.choice('ACGT'), end='')
print()
"""

"""
# 45a
rolls = 1000
total = 0
for i in range(rolls):
	for j in range(3):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		d3 = random.randint(1, 6)
		if d1 == 1: d1 = random.randint(1, 6)
		if d2 == 1: d2 = random.randint(1, 6)
		if d3 == 1: d3 = random.randint(1, 6)
		stat = d1 + d2 + d3
	total += stat
print(total / rolls)
"""

"""
# 45b
games = 1000
stat = 0
min = 0
for i in range(games):
	x = random.randint(1, 6)
	y = random.randint(1, 6)
	z = random.randint(1, 6)
	w = random.randint(1, 6)
	min = x
	if x > y: y = min
	if min > z: z = min
	if min > w: w = min
	stat = stat + x + y + z + w - min
print('3D6dl =', stat / games)
"""

"""
# 46a
trial = 1000
for dc in range(5, 16, 5):
	n = 0
	a = 0
	d = 0
	for i in range(trial):
		r1 = random.randint(1, 20)
		r2 = random.randint(1, 20)
		if r1 >= dc:
			n += 1
		else:
			if r2 >= dc:
				a += 1
			if r1 >= dc:
				d += 1
	print(f'{dc}\t{n/trial:.3f}\t{a/trial:.3f}\t{d/trial:.3f}')
"""

"""
# 46b
trials = 1000
print('normal')
for dc in range(5, 16, 5):
	print(dc, end='\t')
	success = 0
	for n in range(trials):
		normal_roll = random.randint(1, 20)
		if normal_roll >= dc: success += 1
	print(success / trials)
print('\n')

print('advantage')
for dc in range(5, 16, 5):
	print(dc, end='\t')
	success = 0
	max_score = 0
	for n in range(trials):
		roll_a1 = random.randint(1, 20)
		roll_a2 = random.randint(1, 20)
		if roll_a1 > roll_a2: max_score = roll_a1
		else: max_score = roll_a2
		if max_score >= dc: success += 1
	print(success / trials)
print('\n')

print('disadvantage')
for dc in range(5, 16, 5):
	print(dc, end='\t')
	success = 0
	min_score = 0
	for n in range(trials):
		roll_d1 = random.randint(1, 20)
		roll_d2 = random.randint(1, 20)
		if roll_d1 < roll_a2: min_score = roll_d1
		else: min_score = roll_d2
		if min_score >= dc: success += 1
	print(success / trials)
"""

"""
# 47a
rolls = 1000
deaths = 0
stable = 0
revives = 0
for i in range(rolls):
	failures = 0
	successes = 0
	for j in range(3):
		d1 = random.randint(1, 20)
		if 1 < d1 < 10:   failures += 1
		if 20 > d1 >= 10: successes += 1
		if d1 == 1:       failures += 2
		if d1 == 20:      revives += 1
#		print(d1)
#	print(f'Failures: {failures}', f'Successes: {successes}')
	if failures >= 3: deaths += 1
	if successes == 3: stable += 1

print(deaths/rolls, stable/rolls, revives/rolls)
"""

"""
# 47b
success = 0
failure = 0
health = 0
rounds = 1000
for i in range(rounds):
	roll = random.randint(1, 20)
	if roll < 10:
		failure += 1
	elif roll >= 10:
		success += 1
	elif roll == 1:
		failure += 2
	elif roll == 20:
		health += 1

	if failure >= 3:
		print("die")
	elif success >= 3:
		print("stable")
	elif health > 0:
		print("revived")

print("probability of stabilizes:", success / rounds)
print("probability of die:", failure / rounds)
print("probability of revives:", health / rounds)
"""

"""
# 47c
die = 0
stable = 0
revive = 0
games = 1000

for i in range(games):
	f = 0
	s = 0
	r = 0
	while f < 3 and s < 3 and r < 1:
		d = random.randint(1, 20)
		if d == 20: r += 1
		if d < 20 and d >= 10: s += 1
		if d < 10 and d >= 2: f += 1
		if d == 1: f += 2
		if f >= 3: die += 1
		if r == 1: revive += 1
		if s == 3: stable +=1

print(die/games)
print(stable/games)
print(revive/games)
"""

"""
# 47d
rolls = 1000
games = 0                  # number complete scenarios
stable = 0                 # scenarios ending in stable
die = 0                    # scenarios ending in die
revived = 0                # scenarios ending in revive
scs_tot = 0                # total success rolls
fail_tot = 0               # total fail rolls
for i in range(rolls):
	revive = 0
	success = 0
	fail = 0
	for j in range(1):
		r = random.randint(1, 20)

		if r == 1:
			fail += 2
		if r == 20:
			revive += 1
			games += 1
		if 2 <= r <= 9:
			fail += 1
		if 10 <= r <= 19:
			success += 1

	scs_tot += success
	fail_tot += fail
	revived += revive


	if fail_tot % 3 == 0 and fail > 0:
		die += 1
		games += 1
	if scs_tot % 3 == 0 and success > 0:
		stable += 1
		games += 1

print('p(die)=', die / games)
print('p(stable)=', stable / games)
print('p(revived)=', revived / games)
"""
