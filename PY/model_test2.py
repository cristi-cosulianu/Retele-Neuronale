import re, urllib, os, hashlib, zipfile, socket
from urllib import request

def problema1(s):
    words = re.findall("\w+", s)
    return sorted(words)

def problema2(s, url):
    return s in urllib.request.urlopen(url).read().decode("ISO-8859-1")

def problema3(path):
    if os.path.isdir(path):
        md5_list = []
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                file_content = open(file_path, "rb").read()
                md5 = hashlib.md5()
                md5.update(file_content)
                md5_list.append(md5.hexdigest())
        return sorted(md5_list)

def problema4(path):
    file_list = []
    arhiva = zipfile.ZipFile(path, mode="r")
    for file in arhiva.infolist():
        if file.compress_size > 1000:
            file_list.append(os.path.basename(file.filename))
    return sorted(file_list)

def problema5(host, port, text):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((host, port))
    server.send(text.encode("UTF-8"))

    sha256 = hashlib.sha256()
    sha256.update(server.recv(32))
    server.send(sha256.hexdigest().encode("UTF-8"))
    return server.recv(32).decode("UTF-8")