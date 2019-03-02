#RO:

#Sa se scrie o functie care extrage cuvintele dintr-un text dat ca parametru. Un cuvant este definit ca o secventa de caractere alfa-numerice.

#import urllib.request
#f = urllib.request.urlopen("https://stackoverflow.com")
#print(f.read())

import re

def extract_words(text):
    return re.findall("\w+", text)

#print(extract_words("#Sa se scrie o functie care extrage cuvintele dintr-un text dat ca parametru. Un cuvant este definit ca o secventa de caractere alfa-numerice."))

#Sa se scrie o functie care primeste ca parametru un sir de caractere regex, un sir de caractere text si un numar intreg x si returneaza acele substring-uri de lungime maxim x care fac match pe expresia regulata data.

def get_substrings(expression, text, max_lenght):
    compiled_expression = re.compile(expression)
    return re.findall(compiled_expression, text)

#print(get_substrings("\w", "Sa se scrie o functie care extrage cuvintele dintr-un text dat ca parametru. Un cuvant este definit ca o secventa de caractere alfa-numerice.", 4))

#Sa se scrie o functie care primeste ca parametru un sir de caractere text si o lista de expresii regulate si returneaza o lista de siruri de caractere care fac match pe cel putin o expresie regulata data ca parametru.

def find_exp_match(text, exp_list):
    for exp in exp_list:
        exp = re.compile(exp)

    results_set = set()
    for exp in exp_list:
        for result in re.findall(exp, text):
            results_set.add(result)

    return list(results_set)

#print(find_exp_match("Sa se scrie o functie 111 care extrage cuvintele dintr-un 123 text dat ca parametru. Un cuvant #131 este definit ca o  #123* secventa de caractere alfa-numerice.", ["\d+", "#\d+", "#\d+\*", "[a-z]+", "\. [A-Za-z]*", "\w+-\w+"] ))

#Sa se scrie o functie care primeste ca parametru path-ul catre un document xml si un dictionar attrs si returneaza acele elemente care au ca atribute toate cheile din dictionar si ca valoare valorile corespunzatoare. De exemplu, pentru dictionarul {"class": "url", "name": "url-form", "data-id": "item"} se vor selecta elementele care au atributele: class="url" si name="url-form" si data-id="item".

import os

def get_xml_elements(path_to_xml, attrs):
    if os.path.isfile(path_to_xml):
        xml = open(path_to_xml, "rt")
        xml_content = xml.read()

        attributes_exp = "<(?P<tag_name>\w+) "
        for attr in attrs:
            attributes_exp += attr + "=\"" + attrs[attr] + "\""
        attributes_exp += ">"

        elements = list()
        attributes_exp = re.compile(attributes_exp)
        return re.findall(attributes_exp, xml_content) 

#print(get_xml_elements("file.xml", {"class": "class"}))


#Sa se scrie o alta varianta a functiei de la exercitiul anterior care returneaza acele elemente care au cel putin un atribut care corespunde cu o pereche cheie-valoare din dictionar.

def get_xml_elements2(path_to_xml, attrs):
    if os.path.isfile(path_to_xml):
        xml = open(path_to_xml, "rt")
        xml_content = xml.read()

        elements = list()

        for attr in attrs:
            anything_non_greedy = "(.*?)"
            attributes_exp = "<(?P<tag_name>\w+)" + anything_non_greedy + attr + "=\"" + attrs[attr] + "\"" + anything_non_greedy + ">"
        
            attributes_exp = re.compile(attributes_exp)
            elements.extend([result[0] for result in re.findall(attributes_exp, xml_content)])
        return elements

#print(get_xml_elements2("file.xml", {"id": "id"}))


#Sa se scrie o functie care pentru un text dat ca parametru, cenzureaza cuvintele care incep si se termina cu vocale. Prin cenzurare se intelege inlocuirea caracterelor de pe pozitii impare cu caracterul * .

def censor(word):
    for index in range(0,len(word)):
        if (index + 1) % 2 == 0:
            word = word[:index] + "*" + word[index+1:]
    return word

def censor_words(text):
    word_string = "\w+"
    word_exp = re.compile(word_string)
    words = re.findall(word_exp, text)

    rule_string = "^[aeiou]\w*[aeiou]$"
    rule_exp = re.compile(rule_string)
    for word in words:
        if re.match(rule_exp, word):
            censored_word = censor(word)
            word_exp = re.compile(word)
            text = re.sub(word_exp, censored_word, text)
    return text

print(censor_words("Sa se scrie o functie care pentru un text dat ca parametru, cenzureaza cuvintele care incep si se termina cu vocale. Prin cenzurare se intelege inlocuirea caracterelor de pe pozitii impare cu caracterul * ."))


#Sa se verifice, folosind o expresie regulata, daca un sir de caractere reprezinta un CNP valid.

def validate_CNP(string):
    if len(string) == 13:
        cnp_rule_string = "([12])(\d{2})((0[1-9])|(1[0-2]))(([0-2]\d)|(3[01]))(\d{6})"
        cnp_rule_exp = re.compile(cnp_rule_string)
        if re.match(cnp_rule_exp, string):
            return True
        else:
            return False
    else:
        return False

#print(validate_CNP("1971108225890"))
#print(validate_CNP("2970530225890"))
#print(validate_CNP("2001231225890"))

#Sa se scrie o functie care parcurge recursiv un director si afiseaza acele fisiere a caror nume face match pe o expresie regulata data ca parametru sau contine un sir de caractere care face match pe aceeasi expresie. Fisierele care satisfac ambele conditii vor fi afisate prefixate cu ">>" 

def search_file(dir_path, exp_string):
    if os.path.isdir(dir_path):
        exp_compiled = re.compile(exp_string)
        for (root, dirs, files) in os.walk(dir_path):
            for file in files:
                
                file_path = os.path.join(root, file)
                file_desc = open(file_path, "rt")
                file_content = file_desc.read()
                
                name_matched = False
                content_matched = False
                
                if re.search(exp_string, file):
                    name_matched = True
                if re.search(exp_compiled, file_content):
                    content_matched = True

                if name_matched and content_matched:
                    print(">> ", file_path)
                elif name_matched or content_matched:
                    print("   ", file_path)

search_file("C:\\Users\\crist\\OneDrive\\Documents\\GitHub\\Retele-Neuronale\\PY\\folder", "(file|File|FILE)")