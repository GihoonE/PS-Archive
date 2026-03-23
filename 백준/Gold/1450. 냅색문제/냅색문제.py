import sys
input = sys.stdin.readline
N, C = map(int,input().split())
items = list(map(int,input().split()))

left = items[:N//2]
right = items[N // 2:]

def get_subset_sums(arr):
    sums = []
    m = len(arr)

    for mask in range(1 << m):
        s = 0
        for i in range(m):
            if mask & (1 << i):
                s += arr[i]
        sums.append(s)
    return sums
lefts_sums = get_subset_sums(left)
rights_sums = get_subset_sums(right)
rights_sums.sort()
count = 0
from bisect import bisect_right
for n in lefts_sums:
    count += bisect_right(rights_sums,C-n)
print(count)