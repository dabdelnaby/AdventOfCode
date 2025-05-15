# AoC 2023 --- Day 1: Trebuchet?! --- #
#Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

#You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

#Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

#You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

#As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

#The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number."



#Can be done using first wget to get the input file from "https://adventofcode.com/2023/day/1/input"

## PROBLEM 1 ##
#   use grep to remove letters
#   sed 's/[a-z]//g' > day1test.txt.gz
#   use cut to select 1st and last numbers
#   create loop to add all 

def day1pt1():
    fp = open('day1test.txt','r')
    x = 0
    for line in fp:
            line = line.strip()
            y = int(line[0] + line[-1])
            x = x + y
    fp.close()
    print(x)

day1pt1()
## PROBLEM 2 ##
# in CLI
# cat Data/day1input.txt | sed 's/one/o1e/g' | sed 's/two/t2o/g' | sed 's/three/t3e/g' | sed 's/four/f4r/g' | sed 's/five/f5e/g' | sed 's/six/s6x/g' | sed 's/seven/s7n/g' | sed 's/eight/e8t/g' | sed 's/nine/n9e/g' | sed 's/[a-z]//g' > day1part2.txt

def day1pt2():
    fp2 = open('day1part2.txt','r')
    x = 0
    for line in fp2:
            line = line.strip()
            y = int(line[0] + line[-1])
            x = x + y
    fp2.close()
    print(x)

day1pt2()