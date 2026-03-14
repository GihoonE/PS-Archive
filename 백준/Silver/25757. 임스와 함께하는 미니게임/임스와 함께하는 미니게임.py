import sys
input = sys.stdin.readline
N, t = input().split()
names = {}
for _ in range(int(N)):
    cur = input().strip()
    names[cur] = 1
if t == 'Y':
    print(len(names))
elif t == 'F':
    print(len(names)//2)
else:
    print(len(names)//3)