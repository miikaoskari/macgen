import random
import argparse

parser = argparse.ArgumentParser(description='Generate a random mac address')
parser.add_argument('-n', '--number', type=int, default=1, help='number of mac addresses to generate')
# add argument for first three octets
parser.add_argument('-f', '--first', type=str, default='00:00:00', help='first three octets of mac address')
args = parser.parse_args()

# function generates the random addresses
def gen_mac():
    return args.first + ':' + ':'.join(format(random.randint(0, 255), '02x') for _ in range(3))

# generate random mac addresses based on the number of mac addresses specified
for i in range(args.number):
    #check if the address exist in the file
    with open('used_mac_addresses.txt', 'r') as f:
        if args.first + ':' + ':'.join(format(random.randint(0, 255), '02x') for _ in range(3)) in f.read():
            continue
    generated_mac = gen_mac()
    print(generated_mac)
    # write the mac address to the file
    with open('used_mac_addresses.txt', 'a') as f:
        f.write(generated_mac + '\n')
    
