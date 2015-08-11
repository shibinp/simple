def sum_odd(n):	
	if n < 2:
		return 1
	elif n % 2== 0:
		return sum_odd(n-1)
	else:
		return n+ sum_odd(n-2)

print sum_odd(5)
