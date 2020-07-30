def nth_fibonacci(n):
    if (n <= 1):
        return n
    fibo = []
    fibo.append(0)
    fibo.append(1)
    for i in range(n):
    	fibo.append(fibo[i]+fibo[i+1])

    return fibo[n]

print(nth_fibonacci(int(input())))
