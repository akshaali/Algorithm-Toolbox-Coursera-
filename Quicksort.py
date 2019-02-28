from random import randint
import time

# create randomised , unsorted array for testing
def create_array(size=10, max = 50):
    return[randint(0,max) for _ in range(size)]
#print ("Given array is " create_array())

def quicksort(a):
    if len(a) <= 1 :
        return a
    smaller , equal , larger = [], [], []
    pivot = a[randint(0, len(a)-1)]
    for x in a:
        if x<pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)
    return quicksort(smaller) + equal + quicksort(larger)
a = create_array()
print("Unsorted array: " , a)
s = quicksort(a)
print("Sorted array: ", s)
#Time taken by Algorithm
t1 = time.time()
quicksort(a)
t2 = time.time()
print("Time taken: " t2-t1)

        
