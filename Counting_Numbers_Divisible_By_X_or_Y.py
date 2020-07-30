#Counting Numbers Divisible by X or Y upto N
import math
N = 10000000
X = 6
Y = 9
def LCM(x, y):
    if x > y:
        z = x
    else:
        z = y
    return x * y // math.gcd(x, y)
count = math.floor(N/X) + math.floor(N/Y) - math.floor(N/LCM(X,Y))
print(int(count))
