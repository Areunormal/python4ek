def summa(*chisla):
    """Vozvrashaet summu chisel"""
    return sum(chisla)
def fib(nomer):
    """Naxodit chislo fibonachi opredelennogo modulya"""
    if nomer == 1:
        return 0
    elif nomer == 2 or nomer == 3:
        return 1
    return fib(nomer-1) + fib(nomer-2)