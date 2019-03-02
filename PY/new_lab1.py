#1.  Find The largest common divisor of multiple numbers. Define a function with variable number of parameters to resolve this.

def cmmdc(x, y):
	while y != 0:
		aux = x % y
		x = y
		y = aux
	return x

def multi_cmmdc(*argv):
	d = 0
	for arg in argv:
		d = cmmdc(arg, d)
	return d


#2. Write a function that calculates how many vowels are in a string.

def count_vowels(string):
	counter = 0
	for chr in "aeiou":
		counter += string.count(chr)
	return counter

#3. Scrieti o functie care returneaza numarul de cuvinte care exista intr-un string. Cuvintele sunt separate de spatii, semne de punctuatie (, ;, ? ! . )

import re

def count_words(string):
    word = re.compile("\w+")
    return len(re.findall(word, string))

#4. Write a function that receives two strings as parameters and returns the number of occurrences of the first string in the second.

def count_substring(substring, string):
    return string.count(substring)

#5. Write a function that checks whether a character string contains special characters (\r, \t, \n, \a, \b, \f, \v)

def check_special_chars(string):
    for char in "\r\t\n\a\b\f\v":
        if char in string:
            return True
    return False

#6. Write a function that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.



def replace_camel_case(string):
    for char in string:
       if char.isupper():
            index = string.index(char)
            if index == 0:
                string = char.lower() + string[index + 1:]
            else:
                string = string[:index] + "_" + char.lower() + string[index + 1:]
    return string

#7. Write a function that receives a char_len integer and a variable number of strings (strings) and check that each two neighboring strings follow the following rule: the second string starts with the last char_len characters of the first string (like the word game pheasant).

def fazan(char_len, *strings):
    for index in range(1, len(strings)):
        string1 = strings[index - 1]
        string2 = strings[index]
        if string1[-char_len:] != string2[:char_len]:
            return False
    return True

#8. Give a string that represents a polynomial (Ex: "3x ^ 3 + 5x ^ 2 - 2x - 5") and a number (whole or float). Evaluate the polynomial for the given value.

#def evaluate_polynomial(string, number):
#    elements = string.split(" ")
#    result = 0
#    for index in range(len(elements)):
#        value = 0
#        element = elements[index]
#        if "x" in element:
#            value += int(element[:-1]) * number
#            if elements[index + 1] == "^":
#                value = value ** int(elements[index + 2])
#                elements.pop(index + 1)
#                elements.pop(index + 2)
#        else:
#            value += int(element)
#        result += value
#    return result



#9. Write a function that returns the largest prime number from a string given as a parameter or -1 if the character string contains no prime number. Ex: input: 'ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda'; output: 271

def check_prime(number):
    for div in range(2, number//2):
        if number % div == 0:
            return False
    return True

def bigest_prime(string):
    max = 0
    number_pattern = re.compile("\d+")
    for number in re.findall(number_pattern, string):
        integer = int(number)
        if check_prime(integer) and integer > max:
            max = integer

    return max