# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    else:
        t = [0,1]
        for i in range(2,n+1):
            t.append(t[i-1]+t[i-2])
        return t[-1]

n = int(input())
print(calc_fib(n))
