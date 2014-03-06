import math


def mean(array):
    acc = 0.0
    for i in array:
        acc += i
    return float(acc) / len(array)


def unbiased_sample_variance(array):
    # Get a copy of the array
    a = array[:]
    x_ = mean(array)
    
    sq_diff = lambda x: math.fabs(x - x_) ** 2
    map(sq_diff, a)
    s2 = float(sum(a))/(len(a)-1)
    return s2


def population_variance(array):
    # Get a copy of the array
    a = array[:]
    x_ = mean(array)
    
    # TODO: I don't know why, but (x-x_)**2 < 0 sometimes...
    sq_diff = lambda x: math.fabs(x - x_) ** 2
    map(sq_diff, a)
    sigma2 = float(sum(a))/len(a)
    return sigma2


def standard_deviation(array):
    var = variance(array)
    std_dev = math.sqrt(var)
    return std_dev


def covariance(array_x, array_y):
    # http://mathworld.wolfram.com/Covariance.html
    assert len(array_x) == len(array_y)
    x_ = mean(array_x)
    y_ = mean(array_y)

    acc = 0.0
    for xi, yi in zip(array_x, array_y):
        acc += (xi - x_) * (yi - y_)
    
    cov = float(acc) / len(array_x)
    return cov


def ordinary_least_squares(array_x, array_y):
    assert len(array_x) == len(array_y)

    n = len(array_x)
    sx = sum(array_x)
    sx2 = sum([ x**2 for x in array_x])
    sy = sum(array_y)
    #sy2 = sum([ x**2 for y in array_y])
    sxy = sum( x*y for x, y in zip(array_x, array_y))

    beta = ((n * sxy) - (sx * sy)) / ((n * sx2) - (sx**2))
    alpha = (sy/n) - (beta * (sx/n))
    return alpha, beta


def alt_ordinary_least_squares(array_x, array_y):
    """ Doesnt work... """
    # http://en.wikipedia.org/wiki/Simple_linear_regression
    assert len(array_x) == len(array_y)
    x_ = mean(array_x)
    y_ = mean(array_y)
    beta = covariance(array_x, array_y) / unbiased_sample_variance(array_x)
    alpha = y_ - (beta * x_)
    return alpha, beta

