#RO:

#Sa se scrie o functie care sa returneze o lista cu primele n numere din sirul lui Fibonacci.

def first_fibo(n):
    fibo_list = list()
    fibo_list.append(0)
    if n == 1:
        return fibo_list
    fibo_list.append(1)
    if n == 2:
        return fibo_list
    for index in range(2, n):
        fibo_list.append(fibo_list[index - 1] + fibo_list[index - 2])
    return fibo_list

#Sa se scrie o functie care primeste o lista de numere si returneaza o lista cu numerele prime care se gasesc in ea.

def isprime(number):
    for div in range(2, number//2):
        print(div, "   ",  number % div)
        if number % div == 0:
            return False
    return True

def select_prime(numbers):
    prime_list = list()
    for number in numbers:
        if isprime(number):
            prime_list.append(number)
    return prime_list

#Fie un tuplu (x,y) reprezentarea unui punct intr-un sistem cartezian. Sa se scrie o functie care primeste ca parametru o lista de puncte si returneaza o lista de tuple (a,b,c) unice care reprezinta dreptele unice determinate de acele puncte ( (a,b,c) corespunde dreptei ax + by + c = 0).

#def gaseste_drepte(lista_puncte):
    
#    for (x, y) in lista_puncte:


#Sa se scrie o functie care primeste ca parametri doua liste a si b si returneaza: (a intersectat cu b, a reunit cu b, a - b, b - a)

def function(a, b):
    a = set(a)
    b = set(b)
    return (a.intersection(b), a.union(b), a.difference(b), b.difference(a))

#Sa se scrie o functie care primeste ca parametru o lista x, si un numar k. Sa se returneze o lista cu tuple care sa reprezinte combinari de len(x) luate cate k din lista x. Exemplu: pentru lista x = [1,2,3,4] si k = 3 se va returna [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)].

final_list = set()

def combinari_loop(x, y, k):
    if len(y) == k:
        final_list.add(tuple(y))

    for elem in x:
        if elem not in y:
            combinari_loop(x, sorted(y + [elem]), k)

def combinari(x, k):
    combinari_loop(x, [], k)
    return sorted(list(final_list))


#Sa se scrie o functie care primeste ca parametru un numar variabil de liste si un numar intreg x. Sa se returneze o lista care sa contina elementele care apar de exact x ori in listele primite. Exemplu: pentru listele [1,2,3], [2,3,4], [4,5,6], [4, 1, "test"] si x = 2 se va returna [1, 2, 3, 4] # 1 se afla in lista 1 si 4, 2 se afla in lista 1 si 2, 3 se afla in listele 1 si 2, 4 se afla in listele 2 si 3.

def problema7(*argv):
    if type(argv[-1]) == type(1):
        x = argv[-1]
        lists = argv[:-1]
        dictt = dict()
        for list in lists:
            for elem in list:
                if dictt.get(elem):
                    dictt[elem] = dictt[elem] + 1
                else:
                    dictt[elem] = 1
        print(dictt)
        return_list = []
        for (key, value) in dictt.items():
            if value == x:
                return_list.append(key)
        return return_list


#Sa se scrie o functie care primeste ca parametri un numar x default egal cu 1, un numar variabil de siruri de caractere si un flag boolean setat default pe True. Pentru fiecare sir de caractere, sa se genereze o lista care sa contina caracterele care au codul ASCII divizibil cu x in caz ca flag-ul este setat pe True, in caz contrar sa contina caracterele care au codul ASCII nedivizibil cu x. Exemplu: x=2, "test", "hello", "lab002", flag=False va returna (["e", "s"], ["e", "o"], ["a"]). Atentie: functia trebuie sa returneze un numar variabil de liste care sa corespunda cu numarul de siruri de caractere primite ca input.

def problema8(x = 1, *strings, flag = True):
    list_of_lists = []
    for string in strings:
        list = []
        for char in string:
            if (flag == True and ord(char) % x == 0):
                list.append(char)
            if (flag == False and ord(char) % x != 0):
                list.append(char)
        list_of_lists.append(list)
    return list_of_lists

#Sa se scrie o functie care primeste un numar variabil de liste si returneaza o lista de tuple astfel: primul tuplu sa contina primele elemente din liste, al doilea element sa contina elementele de pe pozitia 2 din liste, etc. Ex: pentru listele [1,2,3], [5,6,7], ["a", "b", "c"] se va returna: [(1,5,"a"), (2,6,"b"), (3,7,"c")]. Observatie: In cazul in care listele primite ca input nu au acelasi numar de elemente, elementele lipsa vor fi inlocuite cu None pentru a putea fi generate max([len(x) for x in input_lists]) tuple.

def problema9(*lists):
    max_len = max([len(x) for x in lists])
    for vect in lists:
        if len(vect) < max_len:
            for i in range(max_len - len(vect)):
                vect.append(None)
    return_list = list()
    for elem in range(max_len):
        new_list = list()
        for index in range(len(lists)):
            new_list.append((lists[index])[elem])
        return_list.append(tuple(new_list))

    return return_list

#Să se scrie o funție ce va ordona o listă de tuple de string-uri în funcție de al 3-lea caracter al celui de-al 2-lea element din tuplă. Exemplu: [('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]

def problema10(tuples):
    return sorted(tuples, key = lambda x : x[1][2])
