# Uses python3
import sys
import math

def gcd_naive(a, b):
	current_gcd = math.gcd(a,b)
	return current_gcd

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
