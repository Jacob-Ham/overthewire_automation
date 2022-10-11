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

main()