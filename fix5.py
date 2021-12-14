def seperate(s):
	l = len(s)
	temp = s[0::2]+ s[1::2]
	return temp

print(seperate("a-c-e-g-i-")) 