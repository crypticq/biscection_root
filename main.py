#!/usr/bin/python3
import numpy as np
import time
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
        
    return xr


if __name__ == "__main__":
  xl, xu = {-1 , 1} # your xl ,  xu Value 
  n = 6 # your order 
  es = 0.5*10**(2-n) # es static formula
  maxit = np.round(np.log2(abs(xu - xl)/(es/100))) ### to find max it , static formaula.
  f = lambda x: x**3 -x +6  ### insert your equation
  start = time.time()
  root = bisection(f, xl, xu, es, maxit) # the root finding equation
  print(root)
  end = time.time()
  print("the bisection took:", (end - start)*1000, " ms")
