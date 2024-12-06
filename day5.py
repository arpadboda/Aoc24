import sys
from collections import defaultdict


def task1():
    file1 = open('input_2024_day5.txt', 'r')
    Lines = file1.readlines()
 
    rules = defaultdict(list)
    incorrects = []
    sum = 0

    for line in Lines:
        if len(line) < 3:
            continue
        if "|" in line:
            num1, num2 = line.strip().split("|")
            rules[int(num1)].append(int(num2))
        else:
            nums = [int(x) for x in line.strip().split(",")]
            right = True
            for i in range(1, len(nums)):
                for j in range(i):
                    if nums[j] in rules[nums[i]]:
                        right = False
                        break

            if right:
                sum += nums[len(nums)//2]
            else:
                incorrects.append(nums) 

    print(sum)
    return rules, incorrects

def task2():
    rules, incorrects = task1()
    sum = 0

    for ic in incorrects:
        right = False
        while not right:
            right = True
            for i in range(1, len(ic)):
                for j in range(i):
                    if ic[j] in rules[ic[i]]:
                        right = False
                        ic[i], ic[j] = ic[j], ic[i]
                        break
                if not right:
                    break
        sum += ic[len(ic)//2]

    print(sum)

def main() -> int:
    task2()

if __name__ == '__main__':
    sys.exit(main())


