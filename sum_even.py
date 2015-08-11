def sum_even(n):
	if n < 1:
		return 0
	elif n%2 != 0:
		return sum_even(n-1)
	else:
		return n + sum_even(n-2)

print sum_even(4)

