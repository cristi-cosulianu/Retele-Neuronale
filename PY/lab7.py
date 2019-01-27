#1. Scrieti un program care la fiecare x secunde unde x va fi aleator ales la fiecare iteratie (din intervalul [a, b] , unde a, b sunt date ca argumente) afiseaza de cate minute ruleaza programul (in minute, cu doua zecimale). Programul va rula la infinit.

import time
import random

def display_running_time_loop(a, b, initial_time):
    curr_time = time.time()
    print("Running for: ", round((curr_time - initial_time) / 60, 2), " minutes and: ", curr_time - initial_time - ((curr_time - initial_time) // 60) * 60)
    x = random.randint(a, b)
    time.sleep(x)
    display_running_time_loop(a, b, initial_time)


def display_running_time(a, b):
    initial_time = time.time()
    display_running_time_loop(a, b, initial_time)
    
#display_running_time(1, 6)

#2. Scrieti doua functii de verificare daca un numar este prim, si verificati care dintre ele este mai eficienta din punct de vedere al timpului.

def is_prime1(number):
    div = 2
    while div <= (number // 2):
        if number % div == 0:
            return False
        else:
            div += 1

    return True

def is_prime2(number):
    if number % 2 == 0:
        return False
    else:
        div = 3
        while div <= (number // 2):
            if number % div == 0:
                return False
            else:
                div += 2

    return True

def test_prime_speed(number):
    initial_time = time.time()
    #print("First prime: ", is_prime1(number))
    is_prime1(number)
    print("Time: ", time.time() - initial_time)
    initial_time = time.time()
    #print("Second prime: ", is_prime1(number))
    is_prime1(number)
    print("Time: ", time.time() - initial_time)

#test_prime_speed(179426549)

#3. Gasiti toate fisierele duplicate dintr-un director dat ca argument si afisati timpul de rulare. Calea grupurilor de fisiere duplicate vor fi scrise intr-un fisier output.txt. 

import os

def check_for_duplicates(path):
    init_time = time.time()
    if os.path.isdir:
        files_dict = dict()
        for (root, dirs, files) in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                value = files_dict.get(file)
                if not value:
                    files_dict[file] = [file_path]
                else:
                    value.append(file_path)
                    files_dict[file] = value

        output_file = open("output.txt", "wt")
        for (key, value) in files_dict.items():
            if len(value) > 1:
                for path in value:
                    output_file.write(path + "\n")
            output_file.write("\n")
    curr_time = time.time()
    print("Duration time: ", curr_time - init_time)
                
#check_for_duplicates("C:\\Users\\crist\\OneDrive\\Documents\\GitHub\\Retele-Neuronale\\PY\\test")

#4. Sa se scrie un script care primeste ca argument un director si creeaza un fisier JSON cu date despre toate fisierele din acel director. Pentru fiecare fisier vor fi afisate urmatoarele informatii: nume_fisier, md5_fisier, sha256_fisier, size_fisier (in bytes), cand a fost creat fisierul (in format human-readable) si calea absoluta catre fisier.

import hashlib
import json
import time
import os

def write_JSON(path):
    files_dict = dict({"key":"value"})
    if os.path.isdir(path):
        for (root, dirs, files) in os.walk(path):
            for file in files:
                md5_file = hashlib.md5()
                md5_file.update(file.encode("utf-8"))
                md5_digest = md5_file.hexdigest()

                sha256_file = hashlib.sha256()
                sha256_file.update(file.encode("utf-8"))
                sha256_digest = sha256_file.hexdigest()

                abs_path = os.path.join(root, file)

                info_dict = dict()
                info_dict["nume_fisier"] = file
                info_dict["md5_fisier"] = md5_digest
                info_dict["sha256_fisier"] = sha256_digest
                info_dict["size_fisier"] = os.stat(abs_path).st_size
                info_dict["create_time"] = time.ctime(os.stat(abs_path).st_ctime)
                info_dict["abs_path"] = abs_path

                files_dict[file] = info_dict
        json_file = json.dumps(files_dict)
        open("serialization.json", "wt").write(json_file)

write_JSON("C:\\Users\\crist\\OneDrive\\Documents\\GitHub\\Retele-Neuronale\\PY\\folder")

#5. Sa se creeze doua scripturi care sa comunice intre ele prin date serializate. Primul script va salva periodic o lista cu toate fisierele dintr-un director iar al doilea script va adauga intr-o arhiva toate fisierele cu size mai mic de 100kb si modificate cu cel mult 5 minute in urma (nu va fi adaugat acelasi fisier de 2 ori).

import zipfile

def write_files(path):
    if os.path.isdir(path):
        json_dict = dict()
        for (root, dirs, files) in os.walk(path):
            for file in files:
                abs_path = os.path.join(root, file)
                json_dict[abs_path] = file

        json_content = json.dumps(json_dict)
        open("communicate.json", "wt").write(json_content)

def create_zip():
    json_data = open("communicate.json", "rt").read()
    json_dict = json.loads(json_data)
    curr_time = time.time()
    zip_file = zipfile.ZipFile("small_files.zip", mode="w", compression= zipfile.ZIP_STORED)
    for path in json_dict.keys():
        file_size = os.stat(path).st_size / 1000
        mod_time = os.stat(path).st_mtime
        if file_size < 100 and curr_time - mod_time < 5 * 60:
            zip_file.write(path, path)

                    
write_files("C:\\Users\\crist\\OneDrive\\Documents\\GitHub\\Retele-Neuronale\\PY\\folder")

create_zip()

#6. Sa se scrie un script care afiseaza in ce zi a saptamanii este anul nou, pentru ultimii x ani (x este dat ca argument).

import sys
import time

def new_year_week_day():
    if len(sys.argv) >= 1:
        x = int(sys.argv[1])

        curr_time_obj = time.localtime()

        for index in range(x):
            curr_time_obj.tm_year -= 1
            print(curr_time_obj)
            

new_year_week_day()

#7. Sa se simuleze extragerea 6/49. 