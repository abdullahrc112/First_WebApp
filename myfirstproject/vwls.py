import operator


def vwl(text):
	vowels_dict = {char:text.count(char) for char in text if char in 'aeiou'}
	total_vowels = sum(vowels_dict.values())
	sorted_vowels = sorted(vowels_dict.items(), key=operator.itemgetter(1), reverse=True)
	return total_vowels, sorted_vowels


