# 0. TOATE problemele din acest laborator vor trata exceptiile ce pot aparea. Detalii despre exceptii gasiti in cursul 4.

# 1. Scrieti un program python care sa primeasca de la linia de comanda doua numere (a si b) si care sa afiseze:

# a) a-b

# b) a+b

# c) a/b

# d) a*b

import sys
import os
import my_module as mm

def operations():
    if len(sys.argv) >=3:
        try:
            a = int(sys.argv[1])
            b = int(sys.argv[2])
            print(a - b)
            print(a + b)
            print(a / b)
            print(a * b)
        except Exception as e:
            print(e)
        
# operations()
        

# 2. Scrieti un script care primeste ca parametru de la linia de comanda un path si afiseaza primii 4096 bytes daca path-ul duce la un fisier, intrarile din acesta daca path-ul reprezinta un director si un mesaj de eroare daca path-ul nu este unul valid.

def check_path():
    if len(sys.argv) >= 2:
        try:
            input_path = sys.argv[1]
            if os.path.isdir(input_path):
                print(os.listdir(input_path))
            elif os.path.isfile(input_path):
                file = open(input_path, "rt")
                print(file.read(4096))
            else:
                print("Invalid path!")
        except Exception as e:
            print("Invalid path!")
            print(e)

# check_path()

# 3. Scrieti o functie care primeste ca parametru un nume de fisier. Aceasta va scrie in fisier datele din os.environ, fiecare linie continand cate o intrare din acest dictionar, sub forma cheie [tab] valoare.

def write_info():
    if len(sys.argv) >= 2:
        try:
            file_path = sys.argv[1]
            if os.path.isfile(file_path):
                file = open(file_path, "wt")
                for item in os.environ.items():
                    file.write(item[0] + "\t\t" + item[1] + "\n")
        except Exception as e:
            print(e)
    else:
        print("Insert a file path!")

# write_info()

# 4. Scrieti o functie care primeste ca parametru un path ce reprezinta un director de pe sistem, parcurge recursiv structura de fisiere si directoare pe care acesta le contine si afiseaza in consola toate path-urile pe care le-a parcurs. NU aveti voie sa folositi os.walk.

def recursiv_walk(path):
    try:
        if os.path.isdir(path):
            for entry in os.listdir(path):
                new_path = os.path.join(path, entry)
                print(new_path)
                if os.path.isdir(new_path):
                    recursiv_walk(new_path)
        else:
            print("Is not directory!")
    except Exception as e:
        print(e)

#recursiv_walk("C:\\Users\\crist\\OneDrive\\Documents\\GitHub\\Retele-Neuronale\\PY")

# 5. Scrieti un script care primeste 2 parametri de la consola reprezentand un path catre un director de pe sistem si un nume de fisier. Scriptul va parcurge recursiv structura de fisiere si directoare din directorul dat ca parametru, utilizand os.walk si va scrie in fisierul dat ca parametru toate path-urile pe care le-a parcurs si tipul acestuia (FILE, DIRECTORY, UNKNOWN), separate de |. Fiecare path va fi scris pe cate o linie.

def function5():
    if len(sys.argv) >= 3:
        dir_path = sys.argv[1]
        file_name = sys.argv[2]
        paths = list()
        for (root, dirs, files) in os.walk(dir_path):
            for file in files:
                if file == file_name:
                    file_path = os.path.join(root, file)
                    file_desc = open(file_path, "wt")
                    for path in paths:
                        file_desc.write(path)
                else:
                    file_path = os.path.join(root, file)
                    paths.append(file_path + '\n')
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                paths.append(dir_path + '\n')

#function5()

# 6. Scrieti un script care primeste 3 parametri de la consola. Primul va fi un path catre un fisier, al doilea un path catre un director iar al treilea va fi dimensiunea unui buffer. Scriptul va copia fisierul dat ca parametru in directorul dat ca parametru, utilizand un buffer de marimea celui de-al treilea parametru, in bytes.

def move_file_content():
    if len(sys.argv) >= 4:
        file_path = sys.argv[1]
        dir_path = sys.argv[2]
        buffer_size = int(sys.argv[3])

        if os.path.isfile(file_path) and os.path.isdir(dir_path):
            file_name = os.path.basename(file_path)
            initial_file = open(file_path, "r")
            destination_path = os.path.join(dir_path, file_name)
            destination_file = open(destination_path, "a")

            content = initial_file.read(buffer_size)
            while content:
                destination_file.write(content)
                content = initial_file.read(buffer_size)


#mm.move_file_content()

# 7. Creati-va un modul propriu in care sa implementati cel putin 3 functii. Utilizati aceste functii intr-un script.

# 8. Sa se scrie un script care primeste urmatoarele argumente: path, tree_depth, filesize , filecount, dircount si care creeaza o structura de directoare de adancime depth astfel: incepand din radacina path vor fi create dircount directoare si filecount fisiere cu continut de filesize octeti (doar caracterul "a" de exemplu") iar acest proces va fi repetat recursiv pentru fiecare director creat pana cand se obtine adancimea dorita (in directoarele aflate la adacimea maxima nu se vor crea alte directoare)

def build_hierarchy(path, tree_depth, file_size, file_count, dir_count):
    if tree_depth > 1:
        for i in range(dir_count):
            dir_name = "dir" + str(i)
            dir_path = os.path.join(path, dir_name)
            try:
                os.mkdir(dir_path)
            except Exception as e:
                print(e)
            build_hierarchy(dir_path, tree_depth - 1, file_size, file_count, dir_count)

    for i in range(file_count):
        file_name = "file" + str(i)
        file_path = os.path.join(path, file_name)
        file = open(file_path, "w")
        file.write("a" * (file_size // 2))

def build_hierarchy_main():
    if len(sys.argv) >= 6:
        try:
            path = sys.argv[1]
            tree_depth = int(sys.argv[2])
            file_size = int(sys.argv[3])
            file_count = int(sys.argv[4])
            dir_count = int(sys.argv[5])
        except Exception as e:
            print(e)
        if os.path.isdir(path):
            build_hierarchy(path, tree_depth, file_size, file_count, dir_count)

#build_hierarchy_main()

# De exemplu, daca rulam scriptul astfel: python3 create_dummy_tree.py test 2 1024 3 3 va fi creat in directorul curent urmatoarea structura:

#     test

#     test/dir0

#     test/dir0/file1 (size 1024)

#     test/dir0/file2 (size 1024)

#     test/dir0/file3 (size 1024)

#     test/dir1

#     test/dir1/file1 (size 1024)

#     test/dir1/file2 (size 1024)

#     test/dir1/file3 (size 1024)

#     test/dir2

#     test/dir2/file1 (size 1024)

#     test/dir2/file2 (size 1024)

#     test/dir2/file3 (size 1024)

#     test/file0 (size 1024)

#     test/file1 (size 1024)

#     test/file2 (size 1024)

# 9. Sa se creeze un script care afiseaza urmatoarele informatii despre sistem: 

#     versiunea de python folosita. Daca se foloseste Python 2 va afisa in plus mesajul "=== Python 2 ===" iar daca se foloseste Python 3 va afisa in plus mesajul "Running under Py3" (hint: sys.version_info)
#     numele user-ului care a executat scriptul, 
#     path-ul complet al scriptului.
#     path-ul directorului in care se afla scriptul, 
#     tipul sistemului de operare, 
#     numarul de core-uri, 
#     directoarele din PATH-ul procesului cate unul pe linie, 

import getpass
import multiprocessing

def system_info():
    if sys.version_info.major == 3:
        print("Running under Py3")
    elif sys.version_info.major == 2:
        print("=== Python 2 ===")

    print("User: ", getpass.getuser())
    print("Script path: ", os.path.realpath(__file__))
    print("Script dir: ", os.path.dirname(os.path.realpath(__file__)))
    print("OS type: ", sys.platform)
    print("Cores number: ", multiprocessing.cpu_count())

#system_info()

# 10. Sa se scrie o functie search_by_content care primeste ca parametru doua siruri de caractere target si to_search si returneaza o lista de fisiere care contin to_search. Fisierele se vor cauta astfel: daca target este un fisier, se cauta doar in fisierul respectiv iar daca este un director se va cauta recursiv in toate fisierele din acel director. Daca target nu este nici fisier nici director, se va arunca o exceptie de tipul ValueError cu un mesaj corespunzator.

def check_content(file_path, to_search):
    file = open(file_path, "rt")
    content = file.read()
    file.close()
    return (to_search in content)

def search_by_content_main(target, to_search, curr_dir):
    files_list = []
    if os.path.isfile(target):
        if check_content(target, to_search):
            return os.path.basename(target)
    elif os.path.isdir(target):
        files = os.listdir(target)
        for file in files:
            file_path = os.path.join(target, file)
            result = search_by_content_main(file_path, to_search, curr_dir)
            if type(result) == type(list()):
                for elem in search_by_content_main(file_path, to_search, curr_dir):
                    files_list.append(elem)
            else:
                files_list.append(result)
    if target == curr_dir:
        if len(files_list) == 0:
            raise ValueError
        else:
            return files_list
    else:
        return files_list

def search_by_content(target, to_search):
    return(search_by_content_main(target, to_search, target))

#print(search_by_content("C:\\Users\\crist\\OneDrive\\Documents\\GitHub\\Retele-Neuronale\\PY\\test", "a"))



# 11. Sa se scrie o functie get_file_info care primeste ca parametru un sir de caractere care reprezinta calea catre un fisier si returneaza un dictionar cu urmatoarele campuri: 

# full_path = calea absoluta catre fisier, 

# file_size = dimensiunea fisierului in octeti, 

# file_extension = extensia fisierului (daca are) sau "", 

# can_read si can_write = True/False daca se poate citi din/scrie in fisier.

def file_info(path):
    dictionary = dict()
    dictionary.update({"full_path": os.path.abspath(path)})
    dictionary.update({"file_size": os.stat(path).st_size})
    dictionary.update({"file_extension": os.path.splitext(path)[1]})
    dictionary.update({"can_read": os.access(path, os.R_OK)})
    dictionary.update({"can_write": os.access(path, os.W_OK)})
    return dictionary

#print(file_info("lab5.py"))

# 12. Sa se scrie o functie get_dirs_info care primeste ca parametru un sir de caractere care reprezinta calea catre un director si returneaza un dictionar cu urmatoarele informatii:

# full_path = calea absoluta catre director, 

# total_size = dimensiunea tuturor fisierelor din acel director,

# files = calea relativa catre toate fisierele din acel director, grupate dupa adancime.

# dirs = calea absoluta catre toate directoarele din acel director cu toate informatiile corespunzatoare.

# Sa se scrie intr-un fisier output.txt numele directoarelor returnate de functia get_dirs_info sortate descrescator dupa numarul de fisiere cu adancimea 2.

# Sa se scrie intr-un fisier size.txt numele directoarelor returnate de functia get_dirs_info sortate descrescator dupa total_size.

# Sa se scrie intr-un fisier lungime.txt numele directoarelor returnate de functia get_dirs_info sortate descrescator dupa numarul maxim de caractere din numele fișierelor.

def get_dirs_info(path):
    dictionary = dict()
    dictionary.update({"full_path": os.path.abspath(path)})
    dictionary.update({"total_size": os.stat(path).st_size})
    dictionary.update({("files"): []})
    for (root, dirs, files) in os.walk(path):
        depth = 1
        rel_files_paths = []
        for file in files:
            rel_files_paths.append(os.path.relpath(os.path.join(root, file)))
        if len(dictionary["files"]) > 0:
            rel_files_paths.append(dictionary["files"])
        dictionary.update({("files"): rel_files_paths})
        depth += 1
    abs_dirs_paths = []
    for (root, dirs, files) in os.walk(path):
        for dir in dirs:
            abs_dirs_paths.append(os.path.abspath(dir))
    dictionary.update({("dirs"): abs_dirs_paths})

    return dictionary

#for (key, value) in get_dirs_info("C:\\Users\\crist\\OneDrive\\Documents\\GitHub\\Retele-Neuronale\\PY\\test").items():
#    print(key, "   ", value)

# 13. Sa se scrie o funcție ce returnează o lista cu toate fisierele dintr-un director(primit ca parametru), ce au o anumita extensie (primita ca parametru).

def copy_file(path, destination):
    file = open(path, "rb")
    content = file.read()
    destination_path = os.path.join(destination, os.path.basename(path))
    file_destination = open(destination_path, "wb")
    if os.path.exists(destination_path):
        print("IS THERE!")
    file_destination.write(content)

def make_dir(path):
    try:
        os.mkdir(path)
    except Exception as e:
        pass

def get_files_with_extension(path, extension):
    files_list = list()
    for (root, dirs, files) in os.walk(path):
        for file in files:
            if os.path.splitext(file)[1] == extension:
                files_list.append(os.path.join(root, file))
    return files_list

def clasify(files_list):
    curr_path = os.path.dirname(os.path.abspath(__file__))
    
    dir_0_10KB = os.path.join(curr_path, "0-10KB")
    dir_10KB_1MB = os.path.join(curr_path, "10KB-1MB")
    dir_1MB_2MB = os.path.join(curr_path, "1MB-2MB")
    dir_2MB_5MB = os.path.join(curr_path, "2MB-5MB")
    dir_5MB = os.path.join(curr_path, "5MB-")

    dir_without_digits = os.path.join(curr_path, "without_digits")
    dir_with_digits = os.path.join(curr_path, "with_digits")

    make_dir(dir_0_10KB)
    make_dir(dir_10KB_1MB)
    make_dir(dir_1MB_2MB)
    make_dir(dir_2MB_5MB)
    make_dir(dir_5MB)
    make_dir(dir_without_digits)
    make_dir(dir_with_digits)

    for file in files_list:
        file_size = os.stat(file).st_size
        if file_size // 1000 < 10:
            copy_file(file, dir_0_10KB)
        elif file_size // 1000 < 1000:
            copy_file(file, dir_10KB_1MB)
        elif file_size // 1000000 < 2:
            copy_file(file, dir_1MB_2MB)
        elif file_size // 1000000 < 5:
            copy_file(file, dir_2MB_5MB)
        else:
            copy_file(file, dir_5MB)
        
        file_name = os.path.basename(file)
        if any([char.isdigit() for char in file_name]):
            copy_file(file, dir_with_digits)
        else:
            copy_file(file, dir_without_digits)

clasify(get_files_with_extension("C:\\Users\\crist\\OneDrive\\Documents\\GitHub\\Retele-Neuronale\\PY", ".py"))

# Sa se scrie o functie clasifica ce va copia fisierele returnate de la funcția anterioară în felul următor:

#  - în 5 directoare cu nume specific, in functie de size - (0-10KB, 10KB-1MB, 1MB-2MB, 2MB-5MB, 5MB-)

#  - în 5 directoare cu nume specific, in functie de size - (diferență de maxim 1 fișier între 2 directoare)

#  - în directoare cu nume specific, in functie de primul caracter din nume

#  - în 2 directoare cu nume specific - numele format doar din litere sau nu