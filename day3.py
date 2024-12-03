import sys
from collections import defaultdict
import re

def task1():
    file1 = open('input_2024_day3.txt', 'r')
    Lines = file1.readlines()
 
    sum = 0   

    line = "".join(Lines)

    for m in re.finditer("mul\(", line):
        mulargs = line[m.end():].split(")",1)[0]
        mulargs = mulargs.split(",")
        if len(mulargs) != 2:
            continue
        if not all([x.isdigit() for x in mulargs]):
            continue
        sum += (int(mulargs[0]) * int(mulargs[1]))

    print(sum)

def task2():
    file1 = open('input_2024_day3.txt', 'r')
    Lines = file1.readlines()

    sum = 0

    line = "".join(Lines)

    instructions = ""
    lastdo = 0
    lastdont = 0

    while lastdo > -1 and lastdont > -1:
        if lastdo >= lastdont:
            nextdont = line[lastdo:].find("don't()")
            if nextdont == -1:
                lastdont = -1
                instructions += line[lastdo:]
                break
            else:
                lastdont = lastdo + nextdont
                instructions += line[lastdo:lastdont]
                continue
        else:
            nextdo = line[lastdont:].find("do()")
            if nextdo == -1:
                  lastdo = -1
                  break
            else:
                lastdo = lastdont + nextdo
                continue

    for m in re.finditer("mul\(", instructions):
        mulargs = instructions[m.end():].split(")",1)[0]
        mulargs = mulargs.split(",")
        if len(mulargs) != 2:
            continue
        if not all([x.isdigit() for x in mulargs]):
            continue
        sum += (int(mulargs[0]) * int(mulargs[1]))

    print(sum)

def main() -> int:
    task1()
    task2()

if __name__ == '__main__':
    sys.exit(main())


