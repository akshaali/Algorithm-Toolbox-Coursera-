# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    proportion = list(float(v)/float(w) for v , w in zip(values, weights))
    for i in range(len(values)):
        if capacity == 0 :
            return value 
            break 
        max_weight = max(proportion)
        index = proportion.index(max_weight)
        proportion[index] = -1
        if weights[index] <= capacity:
            value += values[index]
            capacity -= weights[index]
        else:
            value += capacity * max_weight 

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
