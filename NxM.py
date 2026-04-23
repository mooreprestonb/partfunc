#!/usr/bin/env python3
# from Nx x Ny Grid of L size with Na A types enerate all possible combinatins 
from itertools import combinations
import numpy
import math
import time

Nx = 4
Ny = 6
L = Nx*Ny
Na=8
comb = math.comb(L,Na)
print(f"{Nx}x{Ny}={L} with {Na} type A and {comb} combinations")
ngbr = numpy.zeros((L,4),dtype=int)
ttime = time.perf_counter()

def print_dict(data):
    sum =0
    for key, value in data.items():
        print(f"{key}: {value}")
        sum += value
    print("N = ",sum)
    
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

#---------------------------------
# Main

#create ngbr array (Nx4) as there are 4 neighbors
for n in range(L): # periodic neighbors
    i = n%Nx # i value mod Nx
    j = int(n/Nx) # J value floor n/Nx
    nl = (i+1)%Nx + j*Nx # left 
    nr = (i-1)%Nx + j*Nx # right
    nu = i        + ((j+1)%Ny)*Nx # up 
    nd = i        + ((j-1)%Ny)*Nx # down
    ngbr[n]=numpy.array([nl,nr,nu,nd]) # store
    #print(n,i,j,nl,nr,nu,nd)
    #print(n,ngbr[n])

#print(ngbr)

sdict = {}
keys = ['AA','AB','BA','BB'] # interaction types 
ngrid = 0
stime = ntime = time.time()
treport = 5
for grid in generate_grid(Na):
    ngrid += 1
    #print(grid)
    #print(ngrid)
    n = [None]*4
    nb  = dict.fromkeys(keys,0)
    for i in range(L):
        id = grid[i]
        for j in range(4):
            key = id+grid[ngbr[i][j]]
            nb[key] += 1
    skey = "AA"+str(nb["AA"])+",AB"+str(nb["AB"]+nb["BA"])+",BB"+str(nb["BB"])
    sdict[skey]=sdict.get(skey,0)+1

    if(time.time()-ntime>treport):
        print(f"{ngrid}/{comb} = {ngrid/comb:.3f} ~ {(time.time()-stime)*comb/ngrid:.2f} total seconds")
        ntime = time.time()
        
#print(sdict)
print_dict(sdict)
ttime = time.perf_counter() - ttime
print(f"Runtime: {ttime:.2f} seconds")

exit()
