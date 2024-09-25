'''
This script will encode or decode a string from a TXT file to base64 used by PowerShell.
'''

import sys
import base64


def opener(dir):
    #Open a TXT file and pass each line as a list element
    with open(dir) as f:
        return [line.rstrip() for line in f]

def encode(content):
    #We must pass a bytes-like object. The output is given as bytes too then we decode to string/UTF-8
    return base64.b64encode(content.encode('utf-16-le')).decode('utf-8')

def decode(content):
    #Two ways to convert the bytes given by b64decode to string/UTC-8
    #return str(base64.b64decode(content), encoding='utf-8')
    return base64.b64decode(content).decode('utf-8')


def encode_decode(b64_file, use = "-d"):
    file_content = opener(b64_file)
    match use:
        case "-d":
            #decode
            for i in file_content:
                output = decode(i)
                print(output)
        case "-e":
            #encode
            for i in file_content:
                output = encode(i)
                print(output)


def main():
    if len(sys.argv) == 2:
        encode_decode(sys.argv[1])
    elif len(sys.argv) == 3:
        encode_decode(sys.argv[1], sys.argv[2])
    else:
        print("Usage in Windows:")
        print("Decode: python base64PS.py file.txt")
        print("Encode: python base64PS.py file.txt -e\n")
        print("Usage in Linux:")
        print("Encode: python3 base64PS.py file.txt")
        print("Decode: python3 base64PS.py file.txt -e")


if __name__ == "__main__":
    main()
