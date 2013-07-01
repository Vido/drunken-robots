# -*- coding: utf-8 -*-

import math

class State():
    # Tree Structure. I don't know if i'm going to use it.
    def __init__(self, price):
        self.price = price
        self.up = None
        self.down = None

    def __setattr__(self, name, value):

        overwrite_mesg = "'State' object does not support item overwriting"
 
        if name == 'price':
            raise TypeError(overwrite_mesg)
        
        if not (type(value) == 'State'):
            raise TypeError("untreeble type: '%s'" % repr(type(value)))

        if name == 'up':
            if self.up is None:
                self.up = value
            else:
                raise TypeError(overwrite_mesg)

        elif name == 'down':
            if self.down is None:
                self.down = value
            else:
                raise TypeError(overwrite_mesg)

        else:
            mesg = "'State' object has no attribute '%s'" % name
            raise AttributeError(mesg)

    def __repr__(self):
        s_price = str(self.price)
        s_up = str(self.up.price) if self.up is not None else 'Empty'
        s_down = str(self.down.price) if self.down is not None else 'Empty'
        repr_string = "State: %s [up: %s; down: %s]" % s_price, s_up, s_down
        return repr_string

    # TODO: def __hash__(self):


def bopm_europian(S, K, r, sigma, periods, opt_type, step=1):
    """
        S -> spot price
        K -> strike price (exercice price)
        r -> interest rate (per period)
        sigma -> volatility in yearly logarithmic returns.
        periods -> number of periods
        step -> duration of step in years

        http://en.wikipedia.org/wiki/Binomial_options_pricing_model
        http://finance.bi.no/~bernt/gcc_prog/recipes/recipes.pdf #  P.88
    """
    
    if opt_type not in ['call', 'put']:
        raise Exception("opt_type must be 'call' or 'put'")

    u = math.exp(sigma * math.sqrt(step)) #  Up
    d = 1.0/u #  Down

    p = (math.exp(r)-d)/(u-d) #  Prob Up
    q = 1-p #  Prob Down

    end_prices = [0.0] * (periods + 1)
    for i in xrange(periods + 1):
        # print "i:", i # DEBUG
        # print "p-i:", periods - i # DEBUG
        end_prices[i] = S * (u ** i) * (d ** (periods-i)) 

    for i in xrange(len(end_prices)):
        if opt_type == 'call':
            end_prices[i] = max(0, end_prices[i]-K)
        else:
            end_prices[i] = max(0, K-end_prices[i])

    # Just Alias
    v = end_prices

    for t in xrange(periods, -1, -1):
        for i in xrange(t):
            # end_prices is ordered. v[0] < v[1]
            v[i] = ((q * v[i]) + (p * v[i+1])) / math.exp(r)         
        # The last is dirt from the last interation
        v[i+1] = 0

    return end_prices[0]

# TODO: Teste
#bopm_europian(100, 110, 0.01, 0.2, 5, 'put')
