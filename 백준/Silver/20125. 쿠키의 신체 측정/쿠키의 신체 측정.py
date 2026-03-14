import sys
input = sys.stdin.readline
N = int(input())
arr = []
x,y = -1,-1
for i in range(N):
    arr.append(input().rstrip())
    for j in range(1,len(arr[i])-1):
        if '***' in arr[i]:
            if arr[i][j-1] == '*' and arr[i][j] == '*' and arr[i][j+1] == '*' and arr[i-1][j] == '*':
                x,y = i,j
def dfs_head(count,ind_x, ind_y):
    if ind_x-1 >= 0 and arr[ind_x-1][ind_y] == '*':
        return dfs_head(count+1,ind_x-1,ind_y)
    else:
        return count

def dfs_left(count,ind_x,ind_y):
    if ind_y-1 >= 0 and arr[ind_x][ind_y-1] == '*':
        return dfs_left(count+1,ind_x,ind_y-1)
    else:
        return count

def dfs_right(count,ind_x,ind_y):
    if ind_y+1 < len(arr[ind_x]) and arr[ind_x][ind_y+1] == '*':
        return dfs_right(count+1,ind_x,ind_y+1)
    else:
        return count

def dfs_back(count,ind_x,ind_y):
    if ind_x+1 < len(arr) and arr[ind_x+1][ind_y] == '*':
        return dfs_back(count+1,ind_x+1,ind_y)
    else:
        return count, ind_x-1, ind_y

def dfs_leg(count,ind_x,ind_y):
    if ind_x+1 < len(arr) and arr[ind_x+1][ind_y] == '*':
        return dfs_leg(count+1,ind_x+1,ind_y)
    else:
        return count

print(x+1, y+1)
b_count,b_x,b_y = dfs_back(0,x,y)
print(dfs_left(0,x,y),dfs_right(0,x,y),b_count,dfs_leg(0,b_x+1,b_y-1), dfs_leg(0,b_x+1,b_y+1))



