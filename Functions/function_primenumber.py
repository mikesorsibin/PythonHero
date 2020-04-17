def isprime(n):
	if n < 2:
		return False
	for i in range(2,n):
		if (n%2==0):
			return False
	return True

print(isprime(45))



