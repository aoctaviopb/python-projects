# Web Fuzzer
- https://requests.readthedocs.io/en/latest/
- https://realpython.com/python-requests/
## Basic Schema
```python
import sys
import requests


def req():
	#Code


def main():
    req()


if __name__ == "__main__":
    main()

```

## Adding GET Request
```python
import sys
import requests


def req(fqnd):
	r = requests.get(fqnd)
    print(r.status_code)


def main():
    req("https://www.google.com")


if __name__ == "__main__":
    main()

```

### Printing Response
```python
import sys
import requests


def req(fqnd):
    r = requests.get(fqnd)
    print(f"URL: {fqnd}, Status code: {r.status_code}, Length:{len(r.text)}")


def main():
    req("https://www.google.com")


if __name__ == "__main__":
    main()

```

## Passing URL as Parameter
```python
import sys
import requests


def req(fqnd):
    r = requests.get(fqnd)
    print(f"URL: {fqnd}, Status code: {r.status_code}, Length:{len(r.text)}")


def main():
    if len(sys.argv) == 2:
        req(sys.argv[1])
    else:
        print("Usage in Windows: python 02-webFuzzer.py https://www.google.com")
        print("Usage in Linux: python3 02-webFuzzer.py https://www.google.com")


if __name__ == "__main__":
    main()

```

### Reading URLs from a TXT file
```python
import sys
import requests


def req(fqnd):
    lines = []
    with open(fqnd) as f:
        lines = [line.rstrip() for line in f]

    for line in lines:
        r = requests.get(line)
        print(f"URL: {line}, Status code: {r.status_code}, Length:{len(r.text)}")


def main():
    if len(sys.argv) == 2:
        req(sys.argv[1])
    else:
        print("Usage in Windows: python 02-webFuzzer.py ./urls.txt")
        print("Usage in Linux: python3 02-webFuzzer.py ./urls.txt")


if __name__ == "__main__":
    main()

```
- Now we can pass a TXT file with a URL per line and the script will make a request to every URL

## Passing URLs and Web Directories
Here we are going to introduce as parameters the URL we want to fuzz and and TXT file with the directories we wan to try
```python
import sys
import requests


def req(fqnd, directory):
    lines = []
    with open(directory) as f:
        lines = [line.rstrip() for line in f]
    
    print(f"URL: {fqnd}")

    for line in lines:
        x = fqnd + "/" + line

        r = requests.get(x)
        print(f"Directory: /{line}, Status code: {r.status_code}, Length:{len(r.text)}")


def main():
    if len(sys.argv) == 3:
        req(sys.argv[1], sys.argv[2])
    else:
        print("Usage in Windows: python 02-webFuzzer.py https://www.google.com ./dictionary.txt")
        print("Usage in Linux: python3 02-webFuzzer.py https://www.google.com ./dictionary.txt")


if __name__ == "__main__":
    main()

```

## Formatting Output
```python
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

```

![01-Web Fuzzer](00-Assets/01-Web%20Fuzzer.png)
- Finally we have our output formatted by columns of the same dimension

### Explaining print Statement
```python
print("{:-<90}".format("-"))
```
- This code will print in a column of 90 characters a hyphen (`.format("-")`) aligned to the left (`<`). The other 89 characters will be filled with other hyphens (`:-<90`)

