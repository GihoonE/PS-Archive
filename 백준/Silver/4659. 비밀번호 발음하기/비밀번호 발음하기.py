import sys
import heapq

v = {'a','e','i','o','u'}
while True:
    input = sys.stdin.readline().strip()
    if input == "end":
        break
    if not any( c in v for c in input):
        print(f'<{input}> is not acceptable.')
        continue
    else:
        filter = False
        for i in range(0,len(input)-1):
            if (input[i] != 'e' and input[i] != 'o') and input[i] == input[i+1]:
                print(f'<{input}> is not acceptable.')
                filter = True
                break
        if filter:
            continue
        for i in range(0,len(input)-2):
            if not any( c in v for c in input[i:i+3]):
                print(f'<{input}> is not acceptable.')
                filter = True
                break
            elif all( c in v for c in input[i:i+3]):
                print(f'<{input}> is not acceptable.')
                filter = True
                break
        if filter:
            continue
        print(f'<{input}> is acceptable.')

