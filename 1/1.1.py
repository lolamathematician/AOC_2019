import math

with open("data.txt", "r") as f:
	l = [i for i in f]
	l2 = [int(i[:-1]) for i in l[:-1]]
	l2.append(int(l[-1]))
	s = [math.floor(i/3)-2 for i in l2]

print(len(l), len(l2), len(s))

# answer_1 = sum([math.floor(i/3.0)-2 for i in l2])

for i in zip(l2, s):
	print(i)

print(sum(s))