import socket
import re 
import zipfile


names = []

def dccDownload(TCP_IP, TCP_PORT, BUFFER_SIZE): 
    dcc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dcc.connect((TCP_IP,TCP_PORT))

    data = dcc.recv(BUFFER_SIZE)
    f = open('search.zip', 'wb')
    f.write(data)
    f.close()
    unzip()


def cleanSearchZip(member):
    for i in names:
        if i in member and 'epub' in member:
            return True
    return False
def unzip():
    finalLink = []
    zf = zipfile.ZipFile('search.zip')
    for fileName in zf.namelist():
        try:
            data = zf.read(fileName)
        except KeyError:
            print('ERROR: Did not find %s in zip file',fileName)
        else:
            print(fileName + ':')
            links = str(data).split('\\n')
            links = links[4:]
            links = list(filter(cleanSearchZip, links))
            for i in range(len(links)):
                finalLink.append(links[i].split("::INFO::")[0])
            print(finalLink)

def slicestr(member):
    return('!' + member[1:])
    

def irc(request):
    global names
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    HOST = '154.35.136.18'
    PORT = 6667
    NICK = "asdfjvndd__"
    USERNAME = "asdfjvndd__"
    REALNAME = "sdfnvindf__"
    CHANNEL = "#bookz"

    print('soc created |', s)
    remote_ip = socket.gethostbyname(HOST)
    print('ip of irc server is:', remote_ip)


    s.connect((HOST,PORT))

    print('connected to: ', HOST, PORT)
    nickMess = ('NICK ' + NICK + '\r\n').encode()
    s.send(nickMess)
    userMess= (f'USER {USERNAME} {USERNAME} {USERNAME} :{REALNAME} \r\n').encode()
    s.send(userMess)

    check = 1
    completedNames = 0
    while check == 1:
        data = s.recv(4096).decode('utf-8')
        print("LINE: " + data)
        if data.find('PING') != -1:
            s.send(str('PONG ' + data.split(':')[2]).encode())
            s.send(f'JOIN {CHANNEL}  \r\n'.encode())
            s.send(('PRIVMSG ' + CHANNEL + ' :@search '+ request +' \r\n').encode())

        if data.find('353') != -1:
            names.append(data)

        if data.find('353') == -1 and names != [] and completedNames != 1:
            names = ' '.join(names)
            names = names.split()
            names = list(filter(lambda x: True if '+' in x else False, names))
            names = list(map(slicestr , names))
            completedNames = 1

        if data.find('DCC') != -1:
            data = data.split('\n')
            print(data)
            TCP_IP = data[0].split()[-1]
            if data[1] == '' :
                data[1] = s.recv(4096).decode('utf-8')
            TCP_PORT = data[1].split()[-2]
            BUFFER_SIZE = data[1].split()[-1]
            print(TCP_IP)
            print(TCP_PORT)
            print(BUFFER_SIZE)
            BUFFER_SIZE = BUFFER_SIZE.strip('\x01')
            TCP_IP = re.sub('[()]', '', TCP_IP)
            dccDownload(TCP_IP, int(TCP_PORT), int(BUFFER_SIZE))
    s.close()



def main():
    request = input("Request: ")
    irc(request)


if __name__ == "__main__" :
    main()