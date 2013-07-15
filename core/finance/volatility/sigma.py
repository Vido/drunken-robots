# http://www.wikihow.com/Calculate-Historical-Stock-Volatility

import math

from core.math.statistics import standard_deviation 
import returns

def blind_rr_log(array):
    rr_array = []
    for i in xrange(len(array)-1):
        rr = returns.rr_log(array[i], array[i+1])
        rr_array.append(math.fabs(rr))

    sigma = standard_deviation(rr_array)
    return sigma

