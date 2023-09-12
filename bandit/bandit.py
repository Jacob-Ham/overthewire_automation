# Jacob H
# Overthewire bandit automation

from pwn import *

def main():
    passwd = ["bandit0"]
    passwd.append(str(bandit0(passwd[0]).strip()))
    passwd.append(str(bandit1(passwd[1]).strip()))
    passwd.append(str(bandit2(passwd[2]).strip()))
    passwd.append(str(bandit3(passwd[3]).strip()))
    passwd.append(str(bandit4(passwd[4]).strip()))
    passwd.append(str(bandit5(passwd[5]).strip()))
    passwd.append(str(bandit6(passwd[6]).strip()))
    passwd.append(str(bandit7(passwd[7]).strip()))
    passwd.append(str(bandit8(passwd[8]).strip()))
    passwd.append(str(bandit9(passwd[9]).strip()))

    for i in range(0, len(passwd)):
        print(f"Pass bandit{i}: {passwd[i]}")

def bandit0(password):
    s = ssh(user='bandit0', host='bandit.labs.overthewire.org', port=2220, password=password)
    f = SSHPath('readme', ssh=s)
    b1Pass = f.read_bytes().decode()
    return b1Pass

def bandit1(password):
    print("Solving bandit1...\n")
    s = ssh(user='bandit1', host='bandit.labs.overthewire.org', port=2220, password=password)
    f = SSHPath('-', ssh=s)
    b2Pass = f.read_bytes().decode()
    return b2Pass

def bandit2(password):
    print("Solving bandit2...\n")
    s = ssh(user='bandit2', host='bandit.labs.overthewire.org', port=2220, password=password)
    f = SSHPath('spaces\ in\ this\ filename', ssh=s)
    b3Pass = f.read_bytes().decode()
    return b3Pass

def bandit3(password):
    print("Solving bandit3...\n")
    s = ssh(user='bandit3', host='bandit.labs.overthewire.org', port=2220, password=password)
    f = SSHPath('inhere/.hidden', ssh=s)
    b4Pass = f.read_bytes().decode()
    return b4Pass
    
def bandit4(password):
    print("Solving bandit3...\n")
    s = ssh(user='bandit4', host='bandit.labs.overthewire.org', port=2220, password=password)
    f = SSHPath('inhere/-file07', ssh=s)  
    b5Pass = f.read_bytes().decode()
    return b5Pass

def bandit5(password):
    print("Solving bandit6...\n")
    s = ssh(user='bandit5', host='bandit.labs.overthewire.org', port=2220, password=password)
    result = s.process("cat $(find inhere/ -type f -size 1033c ! -executable)", shell=True)
    b6Pass = result.recvall().decode()
    return b6Pass

def bandit6(password):
    print("Solving bandit7...\n")
    s = ssh(user='bandit6', host='bandit.labs.overthewire.org', port=2220, password=password)
    result = s.process("cat $(find / -user bandit7 -group bandit6 -size 33c 2>/dev/null)", shell=True)
    b7Pass = result.recvall().decode()
    return b7Pass

def bandit7(password):
    print("Solving bandit8...\n")
    s = ssh(user='bandit7', host='bandit.labs.overthewire.org', port=2220, password=password)
    result = s.process("echo $(grep millionth data.txt) | cut -f2 -d' '", shell=True)
    b8Pass = result.recvall().decode()
    return b8Pass

def bandit8(password):
    print("Solving bandit9...\n")
    s = ssh(user='bandit8', host='bandit.labs.overthewire.org', port=2220, password=password)
    result = s.process("echo $(sort data.txt | uniq -c | grep '^ *1 ') | cut -f2 -d' '", shell=True)
    b9Pass = result.recvall().decode()
    return b9Pass

def bandit9(password):
    print("Solving bandit10...\n")
    s = ssh(user='bandit9', host='bandit.labs.overthewire.org', port=2220, password=password)
    result = s.process("strings data.txt | grep '==' | cut -d ' ' -f 2 | tail -1", shell=True)
    b10Pass = result.recvall().decode()
    return b10Pass

main()
