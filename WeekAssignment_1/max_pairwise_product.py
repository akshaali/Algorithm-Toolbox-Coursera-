# python3


def max_pairwise_product(numbers):
    n = max(numbers)
    numbers.pop(numbers.index(n))
    p = max(numbers)
    max_product = n*p 
    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
