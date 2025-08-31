import sys
s = int(sys.stdin.readline().strip())
MOD = 1_000_000_007
def recur(n,mod = None):
    if n == 0:
        return (0,1)
    a,b = recur(n >> 1, mod)
    if mod is None:
        c = a*(2*b-a)
        d = a*a+b*b
        if n&1:
            return d,c+d
        else:
            return c,d
    else:
        t = (2*b-a)%mod
        c = (a*t)%mod
        d = (a*a+b*b)%mod
        if n&1 :
            return d, (c+d)%mod
        else:
            return c,d

def fib(n,mod=None):
    return recur(n,mod)[0]

print(fib(s,MOD))