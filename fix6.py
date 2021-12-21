def count(s1, s2):
	s1=s1.lower()

	s2=s2.lower()
	if s2 in s1:
		return s1.count(s2)
	return 0

print(count("MissiSSippi", "Ss"))