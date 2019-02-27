# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    count = 0
    maj = -1
    for i in range(len(a)):
        if count == 0:
            maj = a[i]
        if a[i] == maj:
            count +=1
        else:
            count -=1
    count = 0
    for i in range(len(a)):
        if a[i]==maj:
            count +=1
            if count > len(a)//2:
                return 1
            
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
