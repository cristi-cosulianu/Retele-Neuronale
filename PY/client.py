#import socket, sys

#def client():
#    if len(sys.argv) >= 2:
#        addr = sys.argv[1]
#        port = int(sys.argv[2])

#        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#        server.connect((addr, port))
#        server.send(b"exit")
#        server.close()

#client()

#from ftplib import FTP
##drwxr-sr-x 18 1176 1176 4096 Sep 17 09:55 dists
#def parse_line(line):
#    if line.startswith("d"):
#        print (line.rsplit(" ",1)[1])
#try:
#    client = FTP("ftp.debian.org")
#    res = client.login()
#    print (res)
#    client.retrlines("LIST /debian/",parse_line)
#    client.quit()
#except Exception as e:
#    print (e)


class CarList:
    cars = ["Dacia","BMW","Toyota"]
    def __iter__(self):
        self.pos = -1
        return self
    def __next__ (self):
        self.pos += 1
        if self.pos==len(self.cars): raise StopIteration
        return self.cars[self.pos]

c = CarList()
for i in c:
    print(i)


#from ftplib import FTP
#cmdToDownload = "RETR /debian/extrafiles"
#try:
#    client = FTP("ftp.debian.org")
#    client.storbinary()
#    res = client.login()
#    f = open("debian_extrafiles","wb")
#    client.retrbinary(cmdToDownload ,lambda buf: f.write(buf))
#    f.close()
#    client.quit()
#except Exception as e:
    #print (e)