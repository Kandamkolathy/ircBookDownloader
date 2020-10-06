import socket
import re 

def dccDownload(TCP_IP, TCP_PORT, BUFFER_SIZE): 
    dcc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print('soc created |', s)

    dcc.connect((TCP_IP,TCP_PORT))

    data = dcc.recv(BUFFER_SIZE)
    f = open('search.rar', 'wb')
    f.write(data)
    f.close()
    print(data)
    #173.80.26.71
    #!Oatmeal Zara Novak - [Midnight Mafia 02] - Caged, A Dark Vampire Romance (epub).rar
    #2907707975 3093 277193


#def irc():
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '154.35.136.18'
PORT = 6667
NICK = "george___"
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

while check == 1:
    data = s.recv(4096).decode('utf-8')
    print("LINE: " + data)
    if data.find('PING') != -1:
        s.send(str('PONG ' + data.split(':')[2]).encode())
        #print(str('PONG ' + data.split(':')[2]))
        #print('PONG sent \n')
        s.send(f'JOIN {CHANNEL}  \r\n'.encode())
        s.send(('PRIVMSG ' + CHANNEL + ' :@search dune \r\n').encode())
    if data.find('DCC') != -1:
        data = data.split('\n')
        print(data)
        TCP_IP = data[0].split()[-1]
        #print(data)
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



#def main():


#if __name__ == "__main__" :
#    main()

#:SearchOok!ook@OokMP3.users.undernet.org NOTICE george___ :DCC Send SearchOok_results_for_ dune.txt.zip (80.43.54.162)
#:SearchOok!ook@OokMP3.users.undernet.org PRIVMSG george___ :DCC SEND SearchOok_results_for__dune.txt.zip 1345009314 2048 18199