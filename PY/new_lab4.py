#1.Create a module that contains a function named "sort_uuids". This function reads the file sample.txt ( download ), and sorts the lines base on the string that is between the first and second dash ("-"). Ex: 00e43761-e18a-40c6-b252-3407aa1d8e45 => is sorted by "e18a".  There might be situations where the code might raise Exception. Catch them all ! Create a new file, named "results.txt". Write in this file the sorted uuids. 

import os

def sort_uuids():
    fd = open("sample.txt", "r")
    lines = fd.readlines()
    try:
        sorted(lines, key = lambda line : line.split("-")[1])
    except Exception as e:
        print(e)
    
    result_fd = open("results.txt", "w")
    result_fd.write(lines)
    result_fd.close()


#A universally unique identifier (UUID) is a 128-bit number used to identify information in computer systems. In its canonical textual representation, the sixteen octets of a UUID are represented as 32 hexadecimal (base 16) digits, displayed in five groups separated by hyphens, in the form 8-4-4-4-12 for a total of 36 characters (32 alphanumeric characters and four hyphens). (wiki)


#2. Using the same file from Problem 1 (sample.txt), modify the line that does not respect the uuid format (if there is any). This modification means to replace the bad line with this message "|INVALID_UUID|". You may use the file cursor to make the changes (seek or tell)

import re

def replace_bad_lines():
    pattern = "(\w){8}-(\w){4}-(\w){4}-(\w){4}-(\w){12}"
    pattern = re.compile(pattern)

    fd = open("sample.txt", "r+")
    position = fd.tell()
    line = fd.readline().strip()
    while (line):
        if not re.match(pattern, line):
            print(line)
            print(position)
            fd.seek(position)
            invalid_string = "|INVALID|" + " " * (len(line) - len("|INVALID|")) + "\n"
            print(invalid_string)
            fd.write(invalid_string)
        position = fd.tell()
        line = fd.readline().strip()


#3. Write a script that reads a file, line by line, and for every triple (a, b, c - separated by spaces) applies operator c for the operands a and b. The valid operations are : +, *, -,  \, ** .

#Input Example:

#        3 5 ** => 3 ** 5 =  243
#        7 2 + => 7 + 2   = 9

import os

def apply_operator(file_path):
    if (os.path.isfile(file_path)):
        fd = open(file_path, "r")
        for line in fd.readlines():
            elements = line.strip().split(" ")
            a = int(elements[0])
            b = int(elements[1])
            if elements[2] == "+":
                print(a + b)
            elif elements[2] == "-":
                print(a - b)
            elif elements[2] == "*":
                print(a * b)
            elif elements[2] == "/":
                print(a / b)
            elif elements[2] == "**":
                print(a ** b)
