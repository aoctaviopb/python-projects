'''
This script will decrypt a given hash in a TXT file comparing it with a list of passwords in a TXT file (one password per line).
'''

import sys
import hashlib


def opener(dir):
    #Open a TXT file and pass each line as a list element
    with open(dir) as f:
        return [line.rstrip() for line in f]
    

def crypt(password):
    #The password must be encoded as unicode - UTF-8 in this example
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def decrypt(hash, passwords):
    a = opener(hash)[0]
    b = opener(passwords)

    for i in b:
        c = crypt(i)
        if c == a:
            print(a, " -> ", i)
            break
        else:
            continue

 

def main():
    if len(sys.argv) == 3:
        decrypt(sys.argv[1], sys.argv[2])
    else:
        print("Usage in Windows: python sha256Decrypt.py hash.txt dictionary.txt \n")
        print("Usage in Linux: python3 sha256Decrypt.py hash.txt dictionary.txt")


if __name__ == "__main__":
    main()
