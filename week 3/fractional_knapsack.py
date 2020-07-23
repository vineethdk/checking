# Uses python3
import sys

"""def get_optimal_value(capacity, weights, values):
    #value = 0.
    n=len(weights)
    res_weight=0
    res_value=0
    for i in range(n):
        if(res_weight==capacity):
            return(res_value)
        maxi=0
        try:
            for j in range(len(weights)):
                if(maxi<(values[j]/weights[j])):
                    maxi=values[j]/weights[j]
                    value=values[j]
                    weight=weights[j]
            values.remove(value)
            weights.remove(weight)
        except:
            None
        if((capacity-res_weight)>=weight):
            res_value=res_value+value
            res_weight=res_weight+weight
        else:
            res_value=res_value+(value*(capacity-res_weight)/weight)
            return(res_value)
        #print(res_value,res_weight)
    return(res_value)"""



def get_optimal_value(capacity, weight,value):
    """Return maximum value of items and their fractional amounts.
 
    (max_value, fractions) is returned where max_value is the maximum value of
    items with total weight not more than capacity.
    fractions is a list where fractions[i] is the fraction that should be taken
    of item i, where 0 <= i < total number of items.
 
    value[i] is the value of item i and weight[i] is the weight of item i
    for 0 <= i < n where n is the number of items.
 
    capacity is the maximum weight.
    """
    # index = [0, 1, 2, ..., n - 1] for n items
    index = list(range(len(value)))
    # contains ratios of values to weight
    ratio = [v/w for v, w in zip(value, weight)]
    # index is sorted according to value-to-weight ratio in decreasing order
    index.sort(key=lambda i: ratio[i], reverse=True)
 
    max_value = 0
    fractions = [0]*len(value)
    for i in index:
        if weight[i] <= capacity:
            fractions[i] = 1
            max_value += value[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity/weight[i]
            max_value += value[i]*capacity/weight[i]
            break
 
    return max_value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
