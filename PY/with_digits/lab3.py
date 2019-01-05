# 1.Write a function that receives as parameters two lists a and b and returns a set of sets containing: (a intersected with b, a reunited with b, a - b, b - a)

def function1(a, b):
    a_set = set(a)
    b_set = set(b)
    return (a_set.intersection(b_set), a_set.union(b_set), a_set.difference(b_set), b_set.difference(a_set))

# print(function1([1,2,3,4], [3,4,5,6]))

# 2. Write a function that receives a string as a parameter and returns a dictionary in which the keys are the characters in the character string and the values are the number of occurrences of that character in the given text.

def function2(string):
    characters_dict = dict()
    for char in string:
        if char not in characters_dict:
            characters_dict.setdefault(char, 0)
        characters_dict[char] += 1
    return characters_dict

# print(function2("Ana are mere."))

# Example: For string "Ana has apples." given as a parameter the function will return the dictionary: {'A': 1, '': 2, 'n': 1, 'a': 2, 'r': 2, '.': 1}.

# 3. Compare two dictionaries without using the operator "==" and return a list of differences as follows: (Attention, dictionaries must be recursively covered because they can contain other containers, such as dictionaries, lists, sets, etc.)

def function3(dict1, dict2):
    items1 = dict1.items()
    items2 = dict2.items()

    for item in items1:
        if item not in items2:
            return False

    for item in items2:
        if item not in items1:
            return False

    return True

# print(function3({"a": [1,2,3], "b":0,"c":"d","d":(1,2,3)}, {"a": [1,2,3], "b":0,"c":"d","d":[1,2,3]}))

# 4. The build_xml_element function receives the following parameters: tag, content, and key-value elements given as name-parameters. Build and return a string that represents the corresponding XML element. Example: build_xml_element ("a", "Hello there", "href =" http://python.org ", _class =" my-link " //python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"

def build_xml_element(tag, content, **dictionary):
    return_string = "<" + tag
    for tuple in dictionary.items():
        return_string += " " + tuple[0] + "=\"" + tuple[1] + "\""
    return_string += ">" + content + "</" + tag + ">"
    return return_string

# print(build_xml_element("a", "Hello there", href="http://python.org",   _class="my-link", id="someid"))

# 5. Fie functia validate_dict care primeste ca parametru un set de tuple care reprezinta reguli de validare pentru un dictionar cu chei de tipul string si valori tot de tipul string si un dictionare. O regula este definita astfel: (cheie, "prefix", "middle", "sufix"). O valoare este considerata valida daca incepe cu "prefix", "middle" se gaseste in interiorul valorii (nu la inceput sau sfarsit) si se sfarsete cu "sufix". Functia va returna True daca dictionarul dat ca parametru respecta toate regulile, False in caz contrar. 

def function5(rules, dictionary):
    for rule in rules:
        key = rule[0]
        prefix = rule[1]
        middle = rule[2]
        sufix = rule[3]
        if key in dictionary.keys():
            value = dictionary[key]
            if not value.startswith(prefix):
                return False
            if not value.endswith(sufix):
                return False
            if middle not in value:
                return False
            elif not (value.index(middle) > 0) and not(value.index(middle) < len(value)):
                return False
    return True

# print(function5([("key1", "", "inside", ""), ("key2", "start", "middle", "winter")], {"key2": "starting the engine in the middle of the winter", "key1": "come inside, it's too cold outside", "key3": "this is not valid"}))

# Exemplu: regulile [("key1", "", "inside", ""), ("key2", "start", "middle", "winter")] si dictionarul {"key2": "starting the engine in the middle of the winter", "key1": "come inside, it's too cold outside", "key3": "this is not valid"} => False deoarece desi regulile sunt respectate pentru "key1" si "key2", apare "key3" care nu apare in reguli.

# 6. Fie un dictionar global

operators = {    

    "+": lambda a, b: a + b,     

    "*": lambda a, b: a * b,

    "/": lambda a, b: a / b,

    "%": lambda a, b: a % b

}

#  Sa se construiasca o functie apply_operator(operator, a, b) care va aplica peste a si b regula specificata de dictionarul global. Sa se implementeze astfel incat, in cazul adaugarii unui operator nou, sa nu fie necesara modificarea functiei. 

def apply_operator(operator, a, b):
    if operator in operators.keys():
        function = operators[operator]
        return function(a, b)

# print(apply_operator("+", 2, 3))
# print(apply_operator("*", 3, 2))


# 7. Fie un dictionar global definit asemanator cu cel de mai sus, cu deosebirea ca functiile date ca valori ale dictionarului poate primi orice combinatie de parametri. Sa se scrie o functie apply_function care primeste ca parametru numele unei operatii si aplica functia corespunzatoare peste argumentele primite. Sa se implementeze astfel incat, in cazul adaugarii unei functii noi, sa nu fie necesara modificarea functiei apply_function.

# Un exemplu de dictionar global ar putea fi urmatorul:

print_functions = {

    "print_all": lambda *a, **k: print(a, k),

    "print_args_commas": lambda *a, **k: print(a, k, sep=", "),

    "print_only_args": lambda *a, **k: print(a),

    "print_only_kwargs": lambda *a, **k: print(k)

}

def apply_print_function(print_function, *a, **k):
    if print_function in print_functions.keys():
        function = print_functions[print_function]
        return function(a, k)

# print(apply_print_function("print_only_args", [1,2,3], [1,2,3], [1,2,3], keys = [1,2,3], values = [1,2,3]))

# 8. Sa se scrie o functie care primeste ca parametru un set si returneaza un tuplu (a, b), a reprezentand numarul de elemente unice din set iar b reprezentand numarul de elemente duplicate din set.

def function8(vector):
    a = 0
    b = 0
    vector_set = set(vector)
    for elem in vector_set:
        if vector.count(elem) == 1:
            a += 1
        else:
            b += 1 
    return (a,b)

# print(function8([1,2,3,4,5,2,3,5]))

# 9. Sa se scrie o functie care primeste un numar variabil de seturi si returneaza un dictionar cu urmatoarele operatii dintre toate seturile doua cate doua: reuniune, intersectie, a-b, b-a. Cheia va avea urmatoarea forma: "a op b", unde a si b sunt doua seturi, iar op este operatorul aplicat: |, &, -. 

# Ex: {1,2}, {2, 3} =>

# {

#     "{1, 2} | {2, 3}": 3,

#     "{1, 2} & {2, 3}": 1,

#     "{1, 2} - {2, 3}": 1,

#     ...

# }

def return_dictionary(*sets):
    return_dict = dict()
    for i in range(len(sets) - 1):
        for j in range(i + 1, len(sets)):
            union_key = "" + str(sets[i]) + " | " + str(sets[j])
            union_value = sets[i].union(sets[j])
            return_dict.update({union_key:union_value})

            intersection_key = "" + str(sets[i]) + " & " + str(sets[j])
            intersection_value = sets[i].intersection(sets[j])
            return_dict.update({intersection_key:intersection_value})

            difference_key = "" + str(sets[i]) + " - " + str(sets[j])
            difference_value = sets[i].difference(sets[j])
            return_dict.update({difference_key:difference_value})

            difference_key = "" + str(sets[j]) + " - " + str(sets[i])
            difference_value = sets[j].difference(sets[i])
            return_dict.update({difference_key:difference_value})

    return return_dict

# print(return_dictionary({1,2}, {2,3}, {3,4}))
