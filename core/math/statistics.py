import math

def mean(array):
    acc = 0.0
    for i in array:
        acc += i
    return float(acc)/len(array)

def variance(array):
    # Get a copy of the array
    a = array[:]
    x_ = mean(array)
    print x_
    
    # TODO: I don't know why, but (x-x_)**2 < 0 sometimes...
    sq_diff = lambda x: math.fabs(x - x_) ** 2
    map(sq_diff, a)
    #print [ q for q in a if q < 0]
    var = float(sum(a))/len(a)
    return var

def standard_deviation(array):
    var = variance(array)
    std_dev = math.sqrt(var)
    return std_dev

