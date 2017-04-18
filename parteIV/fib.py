#!/usr/bin/python

#coding: utf-8

"""fib.py 
   Implementa Fibonacci"""

def fin(n):
    """Fibonacci:
	Se n <= 1, fib(n) = 1
	Se n > 1, fib(n) = fib(n-1)+ fib(n-2)
    
    Exemplos de uso:
    >>> fib(0)
    1
    >>> fib(1)
    1
    >>> fib(10)
    89
    >>> [ fib(x)for x in xrange(10)]
    [1,1,2,3,4,5,8,13,21,34,55]
    >>> fib('')
    Traceback(most recent call lasta):
      File"<input>", line 1, in?
      File"<input>", line 19, in fib
    TypeError
    >>>
    """
    if not type(n) is int:
    	raise TypeError

    if n>1:
    	return fib(n-1) + fib (n-2)
    else:
        return 1

def __doctest():
    #Evoca o doctest
    import doctest
    doctest.testmod()


if __name__ == "__main__":
	__doctest()
