import sys
from collections import defaultdict

def check_list(l):
    mindiff = 1000
    maxdiff = -1000
    for i in range(len(l) -1 ):
        d = l[i+1] - l[i]
        if d == 0:
            return False
        mindiff = min(mindiff, d)
        maxdiff = max(maxdiff, d)

    if mindiff * maxdiff < 1:
        return False

    return (mindiff > -4) and (maxdiff < 4)

def task1():
    file1 = open('input_2024_day2.txt', 'r')
    Lines = file1.readlines()
 
    sum = 0   

    for line in Lines:
        nums = [int(x) for x in line.split()]
        sum += 1 if check_list(nums) else 0

    print(sum)

def task2():
    file1 = open('input_2024_day2.txt', 'r')
    Lines = file1.readlines()

    sum = 0

    for line in Lines:
        nums = [int(x) for x in line.split()]
        if check_list(nums):
            sum += 1
        else:
            for i in range(len(nums)):
                small_list = nums.copy()
                small_list.pop(i)
                if check_list(small_list):
                    sum += 1
                    break

    print(sum)

def main() -> int:
    task1()
    task2()

if __name__ == '__main__':
    sys.exit(main())


