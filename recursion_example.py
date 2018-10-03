def fib(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


# 0 1 1 2 3 5 8 ..
print(fib(20))


def factorial(n):
    if not isinstance(n, int):
        return None

    if n <= 0:
        return None

    if n == 1:
        return 1

    return n * factorial(n - 1)


print(factorial('ram'))


def nth_term(n):
    return 7 + (n - 1) * 5


print(nth_term(15))
