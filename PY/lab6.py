#RO:

#Sa se scrie o functie care extrage cuvintele dintr-un text dat ca parametru. Un cuvant este definit ca o secventa de caractere alfa-numerice.

import urllib.request
f = urllib.request.urlopen("https://stackoverflow.com")
print(f.read())

#Sa se scrie o functie care primeste ca parametru un sir de caractere regex, un sir de caractere text si un numar intreg x si returneaza acele substring-uri de lungime maxim x care fac match pe expresia regulata data.


#Sa se scrie o functie care primeste ca parametru un sir de caractere text si o lista de expresii regulate si returneaza o lista de siruri de caractere care fac match pe cel putin o expresie regulata data ca parametru.


#Sa se scrie o functie care primeste ca parametru path-ul catre un document xml si un dictionar attrs si returneaza acele elemente care au ca atribute toate cheile din dictionar si ca valoare valorile corespunzatoare. De exemplu, pentru dictionarul {"class": "url", "name": "url-form", "data-id": "item"} se vor selecta elementele care au atributele: class="url" si name="url-form" si data-id="item".


#Sa se scrie o alta varianta a functiei de la exercitiul anterior care returneaza acele elemente care au cel putin un atribut care corespunde cu o pereche cheie-valoare din dictionar.


#Sa se scrie o functie care pentru un text dat ca parametru, cenzureaza cuvintele care incep si se termina cu vocale. Prin cenzurare se intelege inlocuirea caracterelor de pe pozitii impare cu caracterul * .


#Sa se verifice, folosind o expresie regulata, daca un sir de caractere reprezinta un CNP valid.


#Sa se scrie o functie care parcurge recursiv un director si afiseaza acele fisiere a caror nume face match pe o expresie regulata data ca parametru sau contine un sir de caractere care face match pe aceeasi expresie. Fisierele care satisfac ambele conditii vor fi afisate prefixate cu ">>" 