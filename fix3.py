
def evenSum(num):
	i = 1
	s = 0
	while i <= num:
		if i % 2 == 0:
			s = s+ i
		i =i+ 1
	return s
print(evenSum(10))
