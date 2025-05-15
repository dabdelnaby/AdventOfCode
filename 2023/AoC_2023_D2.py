#--- Day 2: Cube Conundrum ---
# goal: > 12 R, > 13 G, > 14 B

import argparse

parser = argparse.ArgumentParser(description='Finds games that are possible')
parser.add_argument('file', help='Input the file')
parser.add_argument('red', type=int, help='Number of RED Balls')
parser.add_argument('grn', type=int, help='Number of GREEN Balls')
parser.add_argument('blu', type=int, help='Number of BLUE Balls')
arg = parser.parse_args()

colorgames = {'red': arg.red, 'green': arg.grn, 'blue': arg.blu}

with open(arg.file, 'r') as fp:
    total = 0
    for line in fp:
        reject = False
        game = line.split(':')
        for group in game[1].split(';'):
            for numb in group.split(','):
                nlist = numb.split()
                if int(nlist[0]) > colorgames[nlist[1]]:
                    reject = True
        if reject == True: continue
        
        total += int(game[0].split(' ')[1])

        #print(game[0])
        #print(total)