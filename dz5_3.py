def fib(nomer):
    if nomer == 1:
        return 0
    elif nomer == 2 or nomer == 3:
        return 1
    return fib(nomer-1) + fib(nomer-2)
print(fib(25))