import sys
from collections import defaultdict


def task1():
    file1 = open('input_2024_day1.txt', 'r')
    Lines = file1.readlines()
 
    sum = 0   

    l0 = []
    l1 = []

    for line in Lines:
        nums = line.split()
        l0.append(int(nums[0]))
        l1.append(int(nums[1]))

    l0 = sorted(l0)
    l1 = sorted(l1)

    for i in range(len(l0)):
        sum += abs(l1[i] - l0[i])

    print(sum)

def task2():
    file1 = open('input_2024_day1.txt', 'r')
    Lines = file1.readlines()

    sum = 0

    l0 = []
    l1 = defaultdict(int)

    for line in Lines:
        nums = line.split()
        l0.append(int(nums[0]))
        l1[int(nums[1])] += 1

    for i in l0:
        sum += (i * l1[i])

    print(sum)

def main() -> int:
    task1()
    task2()

if __name__ == '__main__':
    sys.exit(main())


