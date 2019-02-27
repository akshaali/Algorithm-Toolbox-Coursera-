# Uses python3
import sys

def merge(left, right):
    i , j , inver_count = 0,0,0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            inver_count += len(left) - i
            j +=1
    result +=left[i:]
    result +=right[j:]
    return result , inver_count
def mergesort(arr):
    global total_count
    if len(arr)<=1:
        return arr
    mid = len(arr)//2

    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    sorted_arr , temp = merge(left , right)
    total_count +=temp
    return sorted_arr

total_count = 0
    
            

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    mergesort(a)
    print(total_count)
