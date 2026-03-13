import sys
import operator

N = int(sys.stdin.readline().strip())
expr = sys.stdin.readline().rstrip()

nums = []
ops = []

for i in range(len(expr)):
    if i % 2 == 0:
        nums.append(int(expr[i]))
    else:
        ops.append(expr[i])

calc = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}

ans = -float('inf')

def dfs(idx, cur):
    global ans

    if idx == len(ops):
        ans = max(ans, cur)
        return

    nxt = calc[ops[idx]](cur, nums[idx + 1])
    dfs(idx + 1, nxt)

    if idx + 1 < len(ops):
        bracket = calc[ops[idx + 1]](nums[idx + 1], nums[idx + 2])
        nxt = calc[ops[idx]](cur, bracket)
        dfs(idx + 2, nxt)


dfs(0, nums[0])

print(ans)