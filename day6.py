import sys
from collections import defaultdict
from enum import Enum, auto
from itertools import cycle
import copy

class Dir(Enum):
    UP = auto()
    RIGHT = auto()
    DOWN = auto()
    LEFT   = auto()

    def next(self):
        cls = self.__class__
        members = list(cls)
        index = members.index(self) + 1
        if index >= len(members):
            index = 0
        return members[index]


def task1():
    file1 = open('input_2024_day6.txt', 'r')
    Lines = file1.readlines()
 
    visited = set()
    current = (-1, -1)
    dir = Dir.UP

    for i in range(len(Lines)):
        for j in range(len(Lines[i])):
            if Lines[i][j] == '^':
                current = (i, j)
                break

    nxt = (-1, -1)

    while True:
        visited.add(current)
        if dir == Dir.UP:
            nxt = (current[0]-1, current[1])
        elif dir == Dir.RIGHT:
            nxt = (current[0], current[1]+1)
        elif dir == Dir.DOWN:
            nxt = (current[0]+1, current[1])
        else:
            nxt = (current[0], current[1]-1)

        if nxt[0] < 0 or nxt[0] >= len(Lines) or nxt[1] < 0 or nxt[1] > len(Lines[0].strip()):
            break

        if Lines[nxt[0]][nxt[1]] == '#':
            dir = dir.next()
            continue

        current = nxt
 

    print(len(visited))

def task2():
    file1 = open('input_2024_day6.txt', 'r')
    Lines = file1.readlines()

    visited = set()
    current = (-1, -1)
    dir = Dir.UP

    sum = 0

    for i in range(len(Lines)):
        for j in range(len(Lines[i])):
            if Lines[i][j] == '^':
                current = (i, j)
                break

    
    for i in range(len(Lines)):
        for j in range(len(Lines[i])):
            if Lines[i][j] in ['#', '^']:
                continue
            map = copy.deepcopy(Lines)
            tlist = list(map[i])
            tlist[j] = '#'
            map[i] = "".join(tlist)
            pos = copy.deepcopy(current)
            nxt = (-1, -1)
            visited = set()
            dir = Dir.UP
                        
            while True:
                state = (pos[0], pos[1], dir)
                if state in visited:
                    sum += 1
                    break
                visited.add(state)
                if dir == Dir.UP:
                    nxt = (pos[0]-1, pos[1])
                elif dir == Dir.RIGHT:
                    nxt = (pos[0], pos[1]+1)
                elif dir == Dir.DOWN:
                    nxt = (pos[0]+1, pos[1])
                else:
                    nxt = (pos[0], pos[1]-1)

                if nxt[0] < 0 or nxt[0] >= len(Lines) or nxt[1] < 0 or nxt[1] > len(Lines[0].strip()):
                    break

                if map[nxt[0]][nxt[1]] == '#':
                    dir = dir.next()
                    continue

                pos = nxt


    print(sum)

def main() -> int:
    task1()
    task2()

if __name__ == '__main__':
    sys.exit(main())


