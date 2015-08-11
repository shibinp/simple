def fact(n):
	if n== 1:
		return n
	else:
		return n* fact(n-1)

number=int(input("Enter the number"))

print ("The factorial of ",number,"is",fact(number))
