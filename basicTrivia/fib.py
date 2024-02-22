def fib(x):
    if x == 0:
        return 1
    else:
        return x * fib(x-1)

#driver code
print(fib(4))
