def pali_check(word):
	pali_word = word.lower()
	if pali_word == pali_word[::-1]:
		return f'{word} is a palindrome.'
	else:
		return f'{word} is not a palindrome.'

