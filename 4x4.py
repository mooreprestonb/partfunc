#!/usr/bin/python3

from itertools import combinations

L = 16
Na=8

def generate_bitmasks(N):
    for positions in combinations(range(L), N):
        mask = 0
        for p in positions:
            mask |= 1 << p
        yield mask
## Example
#for mask in generate_bitmasks(Na):
#    print(bin(mask))

def generate_grid(N):
    for A_pos in combinations(range(L),N):
        grid = ['B']*L
        for pos in A_pos:
            grid[pos]='A'
        yield tuple(grid)

for grid in generate_grid(Na):
    print(grid)
