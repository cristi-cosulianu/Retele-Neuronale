import time, socket
import random, json, zipfile
import os, sys, hashlib
import urllib,re
from urllib import request

def problema0(a, b):
    sum = 0
    for i in range(a,b):
        sum += i
    return sum

def problema1(my_str):
    new_str = str()
    for index in range(len(my_str)):
        if index == 0:
            new_str += my_str[index].lower()
        elif not my_str[index].islower():
            new_str += "_" + my_str[index].lower()
        else:
            new_str += my_str[index]
    return new_str

def problema2(my_list):
    my_set = set()
    for elem in my_list:
        if my_list.count(elem) % 2 == 1:
            my_set.add(elem)
    return list(my_set)

def problema3(my_list):
    pattern = re.compile("\d\d\d\d(\d)+")
    new_dict = dict()
    for elem in my_list:
        if re.findall(pattern, elem):
            md5 = hashlib.md5()
            md5.update(elem.encode())
            md5 = md5.hexdigest()
            new_dict[md5] = elem
    return new_dict

def problema4(my_url):
    data_list = list()
    response = dict(json.loads(urllib.request.urlopen(my_url).read()))
    data_list.append(response["data"])
    while(response.get("next")):
        response = dict(json.loads(urllib.request.urlopen(my_url).read()))
        data_list.append(response["data"])
    return data_list

def problema6(my_file="", my_folder=""):
    my_dict = dict()
    if my_folder != "":
        for (root, dirs, files) in os.walk(my_folder):
            for file in files:
                content = open(os.path.join(root, file), "rb").read()
                sha256 = hashlib.sha256()
                sha256.update(content)
                sha256 = sha256.hexdigest()
                if my_dict.get(sha256):
                    my_dict[sha256].append(os.path.abspath(os.path.join(root, file)))
                else:
                    my_dict[sha256] = [os.path.abspath(os.path.join(root, file))]

    max = 0;
    max_value = list()
    for (key, value) in my_dict.items():
        if len(value) > max:
            max = len(value)
            max_value = value
    return max_value
