import sys
n1 = int(sys.stdin.readline().strip())
arr1 = list(map(int,sys.stdin.readline().strip().split()))
n2 = int(sys.stdin.readline().strip())
arr2 = list(map(int,sys.stdin.readline().strip().split()))
arr1 = sorted(arr1)

def bin_search(l,h,arr,tar):
    if l > h:
        return 0
    else:
        mid = l + (h-l)//2
        if arr[mid] == tar:
            return 1
        elif arr[mid] < tar:
            return bin_search(mid+1,h,arr,tar)
        else:
            return bin_search(l,mid-1,arr,tar)
for num in arr2:
    print(bin_search(0,len(arr1)-1,arr1,num))
