import math

# http://en.wikipedia.org/wiki/Rate_of_return

def rr_log(vi, vf):
    """ Logarithmic or continuously compounded return """
    return math.log(float(vf) / vi)

def rr_arith(vi, vf):
    """ Arithmetic return for a single period"""
    return float(vf - vi) / vi

