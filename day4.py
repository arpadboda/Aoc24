import sys
from collections import defaultdict

def task1():
    file1 = open('input_2024_day4.txt', 'r')
    Lines = file1.readlines()
 
    sum = 0   

    for line in Lines:
        sum += line.count("XMAS")
        sum += line.count("SAMX")

    for i in range(len(Lines) - 3):
        for j in range(len(Lines[0]) - 3):
            if Lines[i][j] == 'X' and Lines[i+1][j+1] == 'M' and Lines[i+2][j+2] == 'A' and Lines[i+3][j+3] == 'S':
                sum += 1
            elif Lines[i][j] == 'S' and Lines[i+1][j+1] == 'A' and Lines[i+2][j+2] == 'M' and Lines[i+3][j+3] == 'X':
                sum += 1

    for i in range(3, len(Lines)):
        for j in range(len(Lines[0]) - 3):
            if Lines[i][j] == 'X' and Lines[i-1][j+1] == 'M' and Lines[i-2][j+2] == 'A' and Lines[i-3][j+3] == 'S':
                sum += 1
            elif Lines[i][j] == 'S' and Lines[i-1][j+1] == 'A' and Lines[i-2][j+2] == 'M' and Lines[i-3][j+3] == 'X':
                sum += 1


    for i in range(len(Lines) - 3):
        for j in range(len(Lines[0])):
            if Lines[i][j] == 'X' and Lines[i+1][j] == 'M' and Lines[i+2][j] == 'A' and Lines[i+3][j] == 'S':
                sum += 1
            elif Lines[i][j] == 'S' and Lines[i+1][j] == 'A' and Lines[i+2][j] == 'M' and Lines[i+3][j] == 'X':
                sum += 1


    print(sum)

def task2():
    file1 = open('input_2024_day4.txt', 'r')
    Lines = file1.readlines()

    sum = 0

    for i in range(1, len(Lines) - 1):
        for j in range(1, len(Lines[0]) - 1):
            if Lines[i][j] != 'A':
                continue
            if (Lines[i+1][j+1] == 'S' and Lines[i-1][j-1] == 'M') or (Lines[i+1][j+1] == 'M' and Lines[i-1][j-1] == 'S'):
                if (Lines[i-1][j+1] == 'S' and Lines[i+1][j-1] == 'M') or (Lines[i-1][j+1] == 'M' and Lines[i+1][j-1] == 'S'):
                   sum += 1


    print(sum)

def main() -> int:
    task1()
    task2()

if __name__ == '__main__':
    sys.exit(main())


