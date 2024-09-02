# ARP Scanner
## Passing Arguments to a Script
The name of our script will be:
```shell
arpScan.py
```

With the library `sys` we can read the arguments passed to a script.
```python
import sys

for i in range(0, len(sys.argv)):
    print('argument:', i, 'value:', sys.argv[i])
```

```shell
python arpScan.py arg1 arg2

#Output
argument: 0 value: d:\06-Programación\01-Python\01-Varios\01-arpScan.py
argument: 1 value: arg1
argument: 2 value: arg2
```

### Limiting Number of Arguments
```python
import sys

def main():
    if (len(sys.argv)>3):
        return
    else:
        print('Hello', sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
```

```shell
python arpScan.py 1 2

#Output
Hello 1 2
```
- Now we can pass a limited number of arguments


## scapy Module
We are going to make use of the module "scapy" that let us interact with networks. From this module we will use the function `arping` to send a broadcast to the devices in the network passed as argument.

- https://scapy.readthedocs.io/en/latest/usage.html#arp-ping

As we can see in the linked documentation, the function
```python
arping("192.168.1.0/24")
```
Is a similar way to execute the ARP ping with the following command:
```python
ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.1.0/24"), timeout=2)

#We can read the output with the following command:
ans.summary(lambda s,r: r.sprintf("%Ether.src% %ARP.psrc%") )
```

Then we need to define a new function where we will pass an argument:
```python
def arpscan(ip):
    scapy.arping(ip)
```

And finally ensemble our script:
```python
import sys
import scapy.all as scapy

def arpscan(ip):
    scapy.arping(ip)

def main():
    if (len(sys.argv)>2):
        return
    else:
        arpscan(sys.argv[1])

if __name__ == "__main__":
    main()

```
- This code can be modified to add some comments and print some help if the input is wrong.

## Final Script
```python
'''
This python script will make an ARP request to all the host in the given network to identify the active hosts.
'''

import sys
import scapy.all as scapy


def arpscan(net_ip):
    scapy.arping(net_ip)

def main():
    if len(sys.argv) == 2:
        arpscan(sys.argv[1])
    else:
        print("---------------------------------------------------------")
        print("---------------------------------------------------------")
        print("Usage in Windows: python arpScan.py network_address")
        print("Usage in Windows: python arpScan.py 192.168.1.0/24 \n")
        print("Usage in Linux: sudo python3 arpScan.py network_address")
        print("Usage in Linux: sudo python3 arpScan.py 192.168.1.0/24")
        print("---------------------------------------------------------")
        print("---------------------------------------------------------")


if __name__ == "__main__":
    main()

```

