import sys
import heapq

H,W,N,M = map(int,sys.stdin.readline().split())
if H%(N+1) > 0:
    a = (H//(N+1))+1
else:
    a = H//(N+1)

if W%(M+1) > 0:
    b = (W//(M+1))+1
else:
    b = W//(M+1)

print(a*b)