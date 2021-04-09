import sys
import copy
import operator
import math
import collections
import heapq
import itertools
import functools
import bisect

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def solution(grid):
    R,C = len(grid), len(grid[0])
    @functools.lru_cache(None)
    def solve(grid):
        grid = list(map(list,grid))
        if sum(row.count('-') for row in grid) == 0:
            return False
        for i in range(R):
            for j in range(C):
                if grid[i][j] == '.':
                    # vertical
                    vertical_works = True
                    grid2 = copy.deepcopy(grid)
                    grid2[i][j] = '-'
                    for i2 in range(i+1,R):
                        if grid[i2][j] == '.':
                            grid2[i2][j] = '-'
                        elif grid[i2][j] == '-':
                            break
                        else:
                            vertical_works = False
                    for i2 in range(i-1,-1,-1):
                        if grid[i2][j] == '.':
                            grid2[i2][j] = '-'
                        elif grid[i2][j] == '-':
                            break
                        else:
                            vertical_works = False
                    if vertical_works:
                        if not solve(tuple(map(tuple,grid2))):
                            return True
                    # horizontal
                    horizontal_works = True
                    grid2 = copy.deepcopy(grid)
                    grid2[i][j] = '-'
                    for j2 in range(j+1,C):
                        if grid[i][j2] == '.':
                            grid2[i][j2] = '-'
                        elif grid[i][j2] == '-':
                            break
                        else:
                            horizontal_works = False
                    for j2 in range(j-1,-1,-1):
                        if grid[i][j2] == '.':
                            grid2[i][j2] = '-'
                        elif grid[i][j2] == '-':
                            break
                        else:
                            horizontal_works = False
                    if horizontal_works:
                        if not solve(tuple(map(tuple,grid2))):
                            return True
        return False

    ans = 0
    for i in range(R):
        for j in range(C):
            if grid[i][j] == '.':
                # vertical
                vertical_works = True
                grid2 = copy.deepcopy(grid)
                grid2[i][j] = '-'
                for i2 in range(i+1,R):
                    if grid[i2][j] == '.':
                        grid2[i2][j] = '-'
                    elif grid[i2][j] == '-':
                        break
                    else:
                        vertical_works = False
                for i2 in range(i-1,-1,-1):
                    if grid[i2][j] == '.':
                        grid2[i2][j] = '-'
                    elif grid[i2][j] == '-':
                        break
                    else:
                        vertical_works = False
                if vertical_works and not solve(tuple(map(tuple,grid2))):
                    ans += 1
                # horizontal
                horizontal_works = True
                grid2 = copy.deepcopy(grid)
                grid2[i][j] = '-'
                for j2 in range(j+1,C):
                    if grid[i][j2] == '.':
                        grid2[i][j2] = '-'
                    elif grid[i][j2] == '-':
                        break
                    else:
                        horizontal_works = False
                for j2 in range(j-1,-1,-1):
                    if grid[i][j2] == '.':
                        grid2[i][j2] = '-'
                    elif grid[i][j2] == '-':
                        break
                    else:
                        horizontal_works = False
                if horizontal_works and not solve(tuple(map(tuple,grid2))):
                    ans += 1
    return ans

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    R,C = map(int,input().split())
    grid = []
    for _ in range(R):
        grid.append(list(input()))
    res = solution(grid)
    print("Case #{}: {}".format(case_num, res))
