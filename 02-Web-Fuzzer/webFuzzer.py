'''
This script will fuzz the URL specified with a dictionary of directories (one directory per line).
'''

import sys
import requests


def req(fqnd, directory):
    lines = []
    with open(directory) as f:
        lines = [line.rstrip() for line in f]
    
    print(f"URL: {fqnd}")

    out = ["Directory", "Status Code", "Length"]

    print("{:-<90}".format("-"))
    print("{:<30}{:<30}{:<30}".format(out[0], out[1], out[2]))
    print("{:-<90}".format("-"))

    i = 0
    for line in lines:
        i+=1

        x = fqnd + "/" + line
        r = requests.get(x)

        print("{:<30}{:<30}{:<30}".format(line, r.status_code, len(r.text)))
        

def main():
    if len(sys.argv) == 3:
        req(sys.argv[1], sys.argv[2])
    else:
        print("Usage in Windows: python webFuzzer.py URL ./dictionary.txt")
        print("Usage in Windows: python webFuzzer.py https://www.google.com ./dictionary.txt \n")
        print("Usage in Linux: python3 webFuzzer.py URL ./dictionary.txt")
        print("Usage in Linux: python3 webFuzzer.py https://www.google.com ./dictionary.txt")


if __name__ == "__main__":
    main()
