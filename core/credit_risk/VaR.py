# -*- coding: utf-8 -*- 

import math
from random import random # Mersenne Twister [0, 1)


class CreditExposure():
    def __init__(self, ead, pd, lgd):
        self.ead = ead if ead > 0.0 else None
        self.pd = pd if pd > 0.0 and pd < 1.0 else None
        self.lgd = lgd if lgd > 0.0 else None

def monte_carlo_method(exposures, **kwargs):

    try:
        simulations = kwargs['simulations']
    except KeyError:
        simulations = 1000
    
    try:
        alpha = kwargs['alpha']
    except KeyError:
        alpha = 0.99

    max_alpha = float(simulations - 1) / simulations
    if alpha > max_alpha:
        raise Exception("Alpha is too big for given simulations.")

    # Monte Carlo Simulation    
    loss_distribution = []
    for i in xrange(simulations):
        loss = 0.0
        
        for expo in exposures:
            if expo.pd > random(): # Default Event
                loss += expo.ead * expo.lgd

        loss_distribution.append(loss)

    '''
        When in-2 < alpha < in-1
        Linear interpolation:
            "M" = [(Vn-1 - Vn-2) / (in-1 - in-2)]
            "VaR(alpha)" = ["M" * ("alpha" - "in-2")] - "Vn-2" 
    '''    
    
    loss_distribution.sort()
    l_idx = int(math.floor(alpha * simulations))
    u_idx = int(math.ceil(alpha * simulations))
 
    # u_idx >= l_idx
    # ld[u_idx] >= ld[l_idx] because loss_distribution is orderd

    if l_idx == u_idx:
        VaR = loss_distribution[l_idx]
    else:
        my = loss_distribution[u_idx] - loss_distribution[l_idx]
        mx = (float(u_idx)/simulations) - (float(l_idx)/simulations)
        VaR = ((my/mx) * (alpha - float(u_index)/simulations))
        VaR += loss_distribution[l_idx]
    
    return VaR

