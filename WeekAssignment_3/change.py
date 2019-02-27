# Uses python3
import sys

def get_change(m):
	coins = [10,5,1]
	if (m == 0):
		return 0
	for coin in coins:
		if (coin<=m):
			return m//coin + get_change(m%coin)


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
