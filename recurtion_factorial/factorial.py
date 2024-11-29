

def factorial(n):
    if n == 1:
        return 1
    
    return n * factorial(n-1)


def fact_tail_recurtion(n, a=1):
    if n == 1:
        return a
    
    return fact_tail_recurtion(n-1, n*a)




fact = factorial(5)

print(str(fact))


fact2 = fact_tail_recurtion(5)

print(str(fact2))
