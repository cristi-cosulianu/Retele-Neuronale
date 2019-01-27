import re, urllib, os, hashlib, zipfile, socket, json
from urllib import request

def problema1(s):
    return re.findall(re.compile("[24680]+"), s)

def problema2(url, cheie):
    return list(dict(json.loads(urllib.request.urlopen(url).read()))[cheie])[-1]

def problema3(path):
    return_dict = dict()
    for (root, dirs, files) in os.walk(path):
        for file in files:
            file_conetent = open(os.path.join(root, file), "rt").read()
            md5_content = hashlib.md5()
            md5_content.update(file_conetent.encode("utf-8"))
            return_dict[file] = md5_content.hexdigest()

    return return_dict


def problema4(lista_arhive):
    file_set = set()
    for arhiva in lista_arhive:
        z = zipfile.ZipFile(arhiva, "r")
        for file in z.infolist():
            if (file.filename[-1] != "/") and (file.filename[-1] != "\\"):
                file_set.add(file.filename)
    return list(file_set)

def problema5(url):
    mydict = dict(json.loads(urllib.request.urlopen(url).read()))
    ip = mydict["ip"]
    port = int(mydict["port"])
    info = mydict["info"]

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port))
    server.send(info[:32].encode("utf-8"))
    response = server.recv(10).decode("utf-8")
    return response.count("A")
