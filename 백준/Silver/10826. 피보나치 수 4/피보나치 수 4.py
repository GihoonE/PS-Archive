import sys
T = int(sys.stdin.readline().strip())
if T <= 1:
    print(T)
else:
    a,b = 0,1
    for i in range(2,T+1):
        a,b = b,a+b
    print(b)