# mac_gen.py

this script generates mac addresses and adds them to a file. 
the script reads the addresses from the file to make sure the same addresses are never used again.

usage of the script:

usage: mac_gen.py [-h] [-n NUMBER] [-f FIRST]

Generate a random mac address

options:
  -h, --help            show this help message and exit
  -n NUMBER, --number NUMBER
                        number of mac addresses to generate
  -f FIRST, --first FIRST
                        first three octets of mac address