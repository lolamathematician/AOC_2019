with open("data.txt", "r") as f:
	l = [i for i in f]
	l2 = [int(i[:-1]) for i in l[:-1]]
	l2.append(int(l[-1]))
	s = [(i//3)-2 for i in l2]

for i in zip(l2, s):
	print(i)

print(sum(s))
