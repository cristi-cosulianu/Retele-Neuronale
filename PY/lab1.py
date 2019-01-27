import re

# 1. Find The largest common divisor of multiple numbers. Define a function with variable number of parameters to resolve this.

def cmmdc(a, b):
	while(b > 0):
		rest = a % b
		a = b
		b = rest
	return a

def multiple_cmmdc(*parameters):
	last_cmmdc = 0
	if len(parameters) >= 2:
		for parameter in parameters:
			last_cmmdc = cmmdc(last_cmmdc, parameter)
	return last_cmmdc
# print(multiple_cmmdc(12,15,21))



# 2. Write a function that calculates how many vowels are in a string.

def count_vowels(string):
	vowels = "aeiou"
	counter = 0
	for char in vowels:
		counter += string.count(char)
	return counter
# print(count_vowels("aaeeiioouu"))


# 3. Scrieti o functie care returneaza numarul de cuvinte care exista intr-un string. Cuvintele sunt separate de spatii, semne de punctuatie (, ;, ? ! . )

def count_words(string):
	separators = re.compile(" |,|;|:|\?|\.")
	words = re.split(separators, string)
	for index in range(len(words)):
		if len(words[index]) is 0:
			words.pop(index)
	return len(words)
		

# print(count_words("aaa,aaa,bbb fff?"))


# 4. Write a function that receives two strings as parameters and returns the number of occurrences of the first string in the second.

def count_sub_string(sub_string, string):
	return string.count(sub_string)

# print(count_sub_string("aaa","aaabbb,aaa,ccc,aaa,aaa,dddaaa"))

# 5. Write a function that checks whether a character string contains special characters (\r, \t, \n, \a, \b, \f, \v)

def check_special_chars(string):
	special_chars = "\r\t\n\a\b\f\v"
	for special_char in special_chars:
		if string.count(special_char) > 0:
			return True
	return False

# print(check_special_chars("ab\acdefg"))

# 6. Write a function that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.

def replace_camel_case(string):
	for i in range(len(string)):
		if string[i].isupper():
			if i is 0:
				string = string[i].lower() + string[i+1:]
			else:
				string = string[:i] + "_" + string[i].lower() + string[i+1:]
	return string

# print(replace_camel_case("ReplaceCamelCase"))

# 7. Write a function that receives a char_len integer and a variable number of strings (strings) and check that each two neighboring strings follow the following rule: the second string starts with the last char_len characters of the first string (like the word game pheasant).

def check_rule(length, *strings):
	for i in range(1,len(strings)):
		if strings[i - 1][-length:] != strings[i][:length]:
			return False
	return True

# print(check_rule(2, "aabb", "bbcc", "ccdd", "eddee"))

# 8. Give a string that represents a polynomial (Ex: "3x ^ 3 + 5x ^ 2 - 2x - 5") and a number (whole or float). Evaluate the polynomial for the given value.

def evaluate_polynomial(string, x):
	elements = string.split(" ")
	for i in range(len(elements)):
		if "x" in elements[i] and len(elements[i]) > 1:
			elements[i] = "" + str(int(elements[i].replace("x", "")) * x)
		if i < len(elements) - 2 and elements[i+1] is "^":
			elements[i] = str(int(elements[i]) **  int(elements[i+2]))
			elements[i+1] = ""
			elements[i+2] = ""
	elements = [element for element in elements if element != ""]
	result = int(elements[0])
	for i in range(2, len(elements)):
		if elements[i-1] == "+":
			result += int(elements[i])
		elif elements[i-1] == "-":
			result -= int(elements[i])
	return result

# print(evaluate_polynomial("3x ^ 3 + 5x ^ 2 - 2x - 5", 1))

# 9. Write a function that returns the largest prime number from a string given as a parameter or -1 if the character string contains no prime number. Ex: input: 'ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda'; output: 271

def isprime(number):
	for i in range(2, number // 2):
		if number % i == 0:
			return False
	return True

def prime_in_string(string):
	prime = -1
	number = 0
	for char in string:
		if char.isdigit():
			number = number * 10 + int(char)
		
		if not char.isdigit():
			if number != 0 and isprime(number) and number > prime:
				prime = number
			number = 0

	return prime

# print(prime_in_string("ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda"))

