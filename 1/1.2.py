import math

with open("data.txt", "r") as f:
	l = [i for i in f]
	l2 = [int(i[:-1]) for i in l[:-1]]
	l2.append(int(l[-1]))

	for i in l2:
		print(i)

	summ = 0

	for mass in l2:
		while mass >= 9:
			mass = (mass // 3) - 2
			summ += mass

	print(summ)
