#!/usr/bin/python3


def bisection(xl  , xu , es , imax , xr , iterr , ea):
    '''
    Function to find the root using bisection method
    
    
    '''
    
    iterr = 0
    xr = 0
    ea = 100
    while True:
        xold = xr
        xr = (xl + xu) // 2
        iterr += 1
        if xr != 0:
            ea = abs((xr - xold) / xr) * 100
        test = f(xl) * f(xr)
        if test < 0:
            xu = xr
        elif test > 0:
            xl = xr
        else:
            ea = 0
        if ea < es or iterr > imax:
            break
        i +=1
    return xr


