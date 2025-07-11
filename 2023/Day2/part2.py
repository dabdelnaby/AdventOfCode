#--- Day 2: Cube Conundrum ---
# goal: > 12 R, > 13 G, > 14 B

import argparse

parser = argparse.ArgumentParser(description='Finds games that are possible')
parser.add_argument('file', help='Input the file')
arg = parser.parse_args()

#colorgames = {'red': arg.red, 'green': arg.grn, 'blue': arg.blu}



with open(arg.file, 'r') as fp:
    max_red = 0
    max_grn = 0
    max_blu = 0

    for line in fp:
        counts = {}

        #game = int(line.split()[1][:-1])
        for group in line:
		print(group)
          

 # for numbcol in group.split(','):
               # n,c = numbcol.split()
               # n = int(n)
               # print(numbcol)
           
