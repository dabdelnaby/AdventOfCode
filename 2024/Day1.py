# Title: 24 Saving Throws
# Author: Dean A

import argparse

parser = argparse.ArgumentParser(description='Finds distance')
parser.add_argument('file', help='Input the file')
arg = parser.parse_args()

with open(arg.file, 'r') as fp:
    list1 = []
    list2 = []
    
    for line in fp:
        parts = line.strip().split()
        list1.append(int(parts[0]))
        list2.append(int(parts[1]))
    
    list1.sort()
    list2.sort()

    total = sum(abs(a - b) for a,b in zip(list1, list2))

    print(total)