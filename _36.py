def decimalToBin(n):
	bi = []
	while n > 1:
		n,r = divmod(n,2)
		if r:
			bi.append('1')
		else:
			bi.append('0')
	bi.append(str(n))
	return ''.join(bi[::-1])
		
result = 0
for x in range(1000000):
	a = str(x)
	bi = decimalToBin(x)
	if a == a[::-1] and bi == bi[::-1]:
		result =  result + x

print (result)