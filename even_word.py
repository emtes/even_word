'''
P: return the minimum number of letters we need to remove such that every letter in the string appears an even number of times.

D: hash tables, need to lookup the number of occurances of each letter to determine if its even or odd

A:
1. iterate through chars in string, build up table with number of occurances values.
2. loop through values on table, for any odd number of occurances add one to the number of letters we need to erase.
'''
def even_word(s):
	to_del = 0
	occ = {}
	for char in s:
		if char not in occ:
			occ[char] = 1
		else:
			occ[char] += 1
	for num in occ.values():
		if num % 2 != 0:
			to_del += 1
	return to_del


# Tests
print(even_word('aaaa') == 0)
print(even_word('potato') == 2)
print(even_word('aabbbb') == 0)
print(even_word('aaabbbccc') == 3)
