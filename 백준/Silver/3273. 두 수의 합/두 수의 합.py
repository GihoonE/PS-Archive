import sys
input = sys.stdin.readline
N = int(input())
arr = [0]*(2000001)
c = list(map(int, input().split()))
tar = int(input())
count = 0
for n in c:
    arr[n] = 1
for n in c:
    if arr[tar-n] == 1:
        count += 1
print(count//2)

