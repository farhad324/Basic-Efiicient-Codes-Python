# Accurate upto 71th position; n>=0 and n<=71
#O(1) program for small numbers

import math

def binets_formula(n):

    sqrt5 = math.sqrt(5)

    nth_fibo = int((( (1 + sqrt5) ** n - (1 - sqrt5) ** n ) / ( 2 ** n * sqrt5 )))

    return nth_fibo
print(binets_formula(71))

