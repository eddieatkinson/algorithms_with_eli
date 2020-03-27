def is_palindrome(num):
	num_as_string = str(num)
	# print num_as_string[1]
	i = 0
	palindrome = True
	while palindrome and i < (len(num_as_string) / 2):
		if num_as_string[i] != num_as_string[len(num_as_string) - 1 - i]:
			palindrome = False
		else:
			i += 1
	return palindrome

def is_largest_palindrome():
	max_num = 999
	least_num = 100
	max_possible = max_num * max_num
	least_possible = least_num * least_num
	for i in range (max_possible, least_possible, -1):
		if is_palindrome(i):
			for j in range (max_num, least_num, -1):
				if i % j == 0 and max_num > i / j > least_num:
					return i

print is_largest_palindrome()