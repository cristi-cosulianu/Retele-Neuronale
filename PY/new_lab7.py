#1. Scrieti un program care la fiecare x secunde unde x va fi aleator ales la fiecare iteratie (din intervalul [a, b] , unde a, b sunt date ca argumente) afiseaza de cate minute ruleaza programul (in minute, cu doua zecimale). Programul va rula la infinit.

import time, socket
import random, json, zipfile
import os, sys, hashlib, urllib

def aux_loop(a, b, start_time):
    curr_time = time.time()
    sleep_seconds = random.randint(a,b)
    print(round((curr_time - start_time) / 60, 2), "--->" , sleep_seconds)
    time.sleep(sleep_seconds)
    aux_loop(a, b, start_time)

def infinit_loop(a, b):
    start_time = time.time()
    aux_loop(a, b, start_time)

#2. Scrieti doua functii de verificare daca un numar este prim, si verificati care dintre ele este mai eficienta din punct de vedere al timpului.

#3. Gasiti toate fisierele duplicate dintr-un director dat ca argument si afisati timpul de rulare. Calea grupurilor de fisiere duplicate vor fi scrise intr-un fisier output.txt. 

def problema3(directory):
    start_time = time.time()
    files_dict = dict()
    
    for (root, dirs, files) in os.walk(directory):
        for file in files:
            if files_dict.get(file):
                files_dict[file].append(os.path.join(root, file))
            else:
                files_dict[file] = [os.path.join(root, file)]

    fd = open("output.txt", "w")
    for (file, path_list) in files_dict.items():
        if len(path_list) > 1:
            for path in path_list:
                fd.write(path + "\n")
    fd.close()
    end_time = time.time()
    print("Running time: ", str(end_time - start_time))


#4. Sa se scrie un script care primeste ca argument un director si creeaza un fisier JSON cu date despre toate fisierele din acel director. Pentru fiecare fisier vor fi afisate urmatoarele informatii: nume_fisier, md5_fisier, sha256_fisier, size_fisier (in bytes), cand a fost creat fisierul (in format human-readable) si calea absoluta catre fisier.

def problema4(directory):
    files_dict = dict()
    for (root, dirs, files) in os.walk(directory):
        for file in files:
            file_dict = dict()

            file_path = os.path.join(root, file)
            abs_file_path = os.path.abspath(file_path)
            file_size = os.stat(file_path).st_size
            creation_time = time.ctime(os.stat(file_path).st_ctime)

            content = open(file_path, "rb").read()
            
            md5 = hashlib.md5()
            md5.update(content)
            md5 = md5.hexdigest()

            sha256 = hashlib.sha256()
            sha256.update(content)
            sha256 = sha256.hexdigest()

            file_dict["nume_fisier"] = file
            file_dict["md5_fisier"] = md5
            file_dict["sha256_fisier"] = sha256
            file_dict["data_crearii"] = creation_time
            file_dict["marime_fisier"] = file_size
            file_dict["calea_absoluta"] = abs_file_path

            files_dict[abs_file_path] = file_dict
            
    json_content = json.dumps(files_dict)
    open("serialization.json", "w").write(json_content)

#5. Sa se creeze doua scripturi care sa comunice intre ele prin date serializate. Primul script va salva periodic o lista cu toate fisierele dintr-un director iar al doilea script va adauga intr-o arhiva toate fisierele cu size mai mic de 100kb si modificate cu cel mult 5 minute in urma (nu va fi adaugat acelasi fisier de 2 ori).

def problema5_1(directory):
    files_dict = dict()
    for (root, dirs, files) in os.walk(directory):
        for file in files:
            files_dict[os.path.join(root, file)] = file
    json_content = json.dumps(files_dict)
    open("communcation.json", "w").write(json_content)
    
def problema5_2(json_file):
    json_data = open(json_file, "r").read()
    json_contet = json.loads(json_data)

    zip_archive = zipfile.ZipFile("zipfile.zip", mode="w", compression=zipfile.ZIP_STORED)

    curr_time = time.time()
    in_zip_files = dict()
    for file_path in json_contet.keys():
        file_size = os.stat(file_path).st_size
        file_ctime = os.stat(file_path).st_mtime

        if (file_size < 100000 and curr_time - file_ctime < 5 * 60):
            filename = os.path.basename(file_path)
            if not in_zip_files.get(filename):
                zip_archive.write(file_path, os.path.basename(file_path))
                in_zip_files[os.path.basename(file_path)] = True

    zip_archive.close()


#6. Sa se scrie un script care afiseaza in ce zi a saptamanii este anul nou, pentru ultimii x ani (x este dat ca argument).

def new_year_week_day(x):
        curr_time_obj = time.localtime()

        for index in range(x):
            curr_time_obj.tm_year -= 1
            print(curr_time_obj)

#7. Sa se simuleze extragerea 6/49. 