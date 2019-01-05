# 1.Create a module that contains a function named "sort_uuids". This function reads the file sample.txt ( download ), and sorts the lines base on the string that is between the first and second dash ("-"). Ex: 00e43761-e18a-40c6-b252-3407aa1d8e45 => is sorted by "e18a".  There might be situations where the code might raise Exception. Catch them all ! Create a new file, named "results.txt". Write in this file the sorted uuids. 

def sort_uuids():
    sample_file = open("sample.txt","rt")
    content = sample_file.read()
    list_of_lines = content.split("\n")
    new_list_of_lines = []
    for line in list_of_lines:
        if line.count("-") == 0:
            new_line = "" + line[:8] + "-" + line[8:12] + "-" + line[12:16] + "-" + line[16:20] + "-" + line[20:]
            line = new_line
        new_list_of_lines.append(line)
    list_of_lines = new_list_of_lines
    try:
        list_of_lines.sort(key = lambda line : line.split("-")[1])
    except Exception as e:
        print(e)
    results_file = open("results.txt","wt")
    for line in list_of_lines:
        results_file.write(line + "\n")

# print(sort_uuids())

# A universally unique identifier (UUID) is a 128-bit number used to identify information in computer systems. In its canonical textual representation, the sixteen octets of a UUID are represented as 32 hexadecimal (base 16) digits, displayed in five groups separated by hyphens, in the form 8-4-4-4-12 for a total of 36 characters (32 alphanumeric characters and four hyphens). (wiki)


# 2. Using the same file from Problem 1 (sample.txt), modify the line that does not respect the uuid format (if there is any). This modification means to replace the bad line with this message "|INVALID_UUID|". You may use the file cursor to make the changes (seek or tell)

def change_sample():
    sample_file = open("sample.txt", "r+")
    position = sample_file.tell()
    line = sample_file.readline()
    while line:
        line = line.strip()
        if len(line) < 36:
            print("|INVALID_UUID|")
            sample_file.seek(position)
            sample_file.writelines("|INVALID_UUID|" + (" " * (len(line) - len("|INVALID_UUID|"))) + "\n")
        else:
            print(line)

        position = sample_file.tell()
        line = sample_file.readline()

# change_sample()


# 3. Write a script that reads a file, line by line, and for every triple (a, b, c - separated by spaces) applies operator c for the operands a and b. The valid operations are : +, *, -,  \, ** .

# Input Example:

# 3 5 ** => 3 ** 5 =  243
# 7 2 + => 7 + 2   = 9

def apply_operator():
    input_file = open("input.txt", "rt")
    lines = input_file.readlines()
    for line in lines:
        line = line.strip()
        elements = line.split(" ")
        print(elements)
        if elements[2] == "**":
            print(elements[0] + elements[2] + elements[1] + "=" + str((int(elements[0]) ** int(elements[1]))))
        elif elements[2] == "*":
            print(elements[0] + elements[2] + elements[1] + "=" + str((int(elements[0]) * int(elements[1]))))
        elif elements[2] == "+":
            print(elements[0] + elements[2] + elements[1] + "=" + str((int(elements[0]) + int(elements[1]))))
        elif elements[2] == "-":
            print(elements[0] + elements[2] + elements[1] + "=" + str((int(elements[0]) - int(elements[1]))))
        elif elements[2] == "/":
            print(elements[0] + elements[2] + elements[1] + "=" + str((int(elements[0]) / int(elements[1]))))

apply_operator()