#RO:

#0. TOATE problemele din acest laborator vor trata exceptiile ce pot aparea. Detalii despre exceptii gasiti in cursul 4.

#1. Scrieti un program python care sa primeasca de la linia de comanda doua numere (a si b) si care sa afiseze:

#a) a-b

#b) a+b

#c) a/b

#d) a*b

import sys

def problema1():
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(a - b)
    print(a + b)
    print(a / b)
    print(a // b)
    print(a * b)

#2. Scrieti un script care primeste ca parametru de la linia de comanda un path si afiseaza primii 4096 bytes daca path-ul duce la un fisier, intrarile din acesta daca path-ul reprezinta un director si un mesaj de eroare daca path-ul nu este unul valid.

import os

def problema2(path):
    if os.path.isfile(path):
        print(open(path, "rt").read(4096))
    elif os.path.isdir(path):
        print(os.listdir(path))
    else:
        print("Not a valid path!")

#3. Scrieti o functie care primeste ca parametru un nume de fisier. Aceasta va scrie in fisier datele din os.environ, fiecare linie continand cate o intrare din acest dictionar, sub forma cheie [tab] valoare.

def problema3(file_path):
    file = open(file_path, "wt")
    for (key, value) in os.environ.items():
        file.write(key + " --- " + value + "\n")

#4. Scrieti o functie care primeste ca parametru un path ce reprezinta un director de pe sistem, parcurge recursiv structura de fisiere si directoare pe care acesta le contine si afiseaza in consola toate path-urile pe care le-a parcurs. NU aveti voie sa folositi os.walk.

def problema4(dir_path):
    for (root, dirs, files) in os.walk(dir_path):
        for file in files:
            print(os.path.join(root, file))
        for dir in dirs:
            print(os.path.join(root, dir))

#5. Scrieti un script care primeste 2 parametri de la consola reprezentand un path catre un director de pe sistem si un nume de fisier. Scriptul va parcurge recursiv structura de fisiere si directoare din directorul dat ca parametru, utilizand os.walk si va scrie in fisierul dat ca parametru toate path-urile pe care le-a parcurs si tipul acestuia (FILE, DIRECTORY, UNKNOWN), separate de |. Fiecare path va fi scris pe cate o linie.

def problema5():
    dir_path = sys.argv[1]
    file_path = sys.argv[2]
    output_file = open(file_path, "wt")
    for (root, dirs, files) in os.walk(dir_path):
        for dir in dirs:
            output_file.write(os.path.join(root, dir) + " | DIRECTORY\n")
        for file in files:
            output_file.write(os.path.join(root, file) + " | FILE\n")

#6. Scrieti un script care primeste 3 parametri de la consola. Primul va fi un path catre un fisier, al doilea un path catre un director iar al treilea va fi dimensiunea unui buffer. Scriptul va copia fisierul dat ca parametru in directorul dat ca parametru, utilizand un buffer de marimea celui de-al treilea parametru, in bytes.



#7. Creati-va un modul propriu in care sa implementati cel putin 3 functii. Utilizati aceste functii intr-un script.

#8. Sa se scrie un script care primeste urmatoarele argumente: path, tree_depth, filesize , filecount, dircount si care creeaza o structura de directoare de adancime depth astfel: incepand din radacina path vor fi create dircount directoare si filecount fisiere cu continut de filesize octeti (doar caracterul "a" de exemplu") iar acest proces va fi repetat recursiv pentru fiecare director creat pana cand se obtine adancimea dorita (in directoarele aflate la adacimea maxima nu se vor crea alte directoare)

#De exemplu, daca rulam scriptul astfel: python3 create_dummy_tree.py test 2 1024 3 3 va fi creat in directorul curent urmatoarea structura:

#    test

#    test/dir0

#    test/dir0/file1 (size 1024)

#    test/dir0/file2 (size 1024)

#    test/dir0/file3 (size 1024)

#    test/dir1

#    test/dir1/file1 (size 1024)

#    test/dir1/file2 (size 1024)

#    test/dir1/file3 (size 1024)

#    test/dir2

#    test/dir2/file1 (size 1024)

#    test/dir2/file2 (size 1024)

#    test/dir2/file3 (size 1024)

#    test/file0 (size 1024)

#    test/file1 (size 1024)

#    test/file2 (size 1024)

#9. Sa se creeze un script care afiseaza urmatoarele informatii despre sistem: 

#    versiunea de python folosita. Daca se foloseste Python 2 va afisa in plus mesajul "=== Python 2 ===" iar daca se foloseste Python 3 va afisa in plus mesajul "Running under Py3" (hint: sys.version_info)
#    numele user-ului care a executat scriptul, 
#    path-ul complet al scriptului.
#    path-ul directorului in care se afla scriptul, 
#    tipul sistemului de operare, 
#    numarul de core-uri, 
#    directoarele din PATH-ul procesului cate unul pe linie, 

#10. Sa se scrie o functie search_by_content care primeste ca parametru doua siruri de caractere target si to_search si returneaza o lista de fisiere care contin to_search. Fisierele se vor cauta astfel: daca target este un fisier, se cauta doar in fisierul respectiv iar daca este un director se va cauta recursiv in toate fisierele din acel director. Daca target nu este nici fisier nici director, se va arunca o exceptie de tipul ValueError cu un mesaj corespunzator.

#11. Sa se scrie o functie get_file_info care primeste ca parametru un sir de caractere care reprezinta calea catre un fisier si returneaza un dictionar cu urmatoarele campuri: 

#full_path = calea absoluta catre fisier, 

#file_size = dimensiunea fisierului in octeti, 

#file_extension = extensia fisierului (daca are) sau "", 

#can_read si can_write = True/False daca se poate citi din/scrie in fisier.

#12. Sa se scrie o functie get_dirs_info care primeste ca parametru un sir de caractere care reprezinta calea catre un director si returneaza un dictionar cu urmatoarele informatii:

#full_path = calea absoluta catre director, 

#total_size = dimensiunea tuturor fisierelor din acel director,

#files = calea relativa catre toate fisierele din acel director, grupate dupa adancime.

#dirs = calea absoluta catre toate directoarele din acel director cu toate informatiile corespunzatoare.

#Sa se scrie intr-un fisier output.txt numele directoarelor returnate de functia get_dirs_info sortate descrescator dupa numarul de fisiere cu adancimea 2.

#Sa se scrie intr-un fisier size.txt numele directoarelor returnate de functia get_dirs_info sortate descrescator dupa total_size.

#Sa se scrie intr-un fisier lungime.txt numele directoarelor returnate de functia get_dirs_info sortate descrescator dupa numarul maxim de caractere din numele fișierelor.

#13. Sa se scrie o funcție ce returnează o lista cu toate fisierele dintr-un director(primit ca parametru), ce au o anumita extensie (primita ca parametru).

#Sa se scrie o functie clasifica ce va copia fisierele returnate de la funcția anterioară în felul următor:

# - în 5 directoare cu nume specific, in functie de size - (0-10KB, 10KB-1MB, 1MB-2MB, 2MB-5MB, 5MB-)

# - în 5 directoare cu nume specific, in functie de size - (diferență de maxim 1 fișier între 2 directoare)

# - în directoare cu nume specific, in functie de primul caracter din nume

# - în 2 directoare cu nume specific - numele format doar din litere sau nu