def merge(left,right):
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i++
        else:
            result.append(right[j])
            j++
    result +=left[i:]
    result +=right[j:]
def mergesort(lst):
    if len(lst) <=:
        return lst
    mid = int(len(lst))//2
    left = mergesort(lst[:mid])
    right = mergeg(lst[mid:])
    return merge(left, right)
arr = [1,23,-1,4,30,-6,-2,22,33,0]
print(mergesort(arr))

    
        
