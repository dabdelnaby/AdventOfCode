


fp = open('day1test.txt','r')
x = 0
for line in fp:
        line = line.strip()
        y = int(line[0] + line[-1])
        x = x + y
        print(x)
