def fib(n):
    """Calculates the nth Fibonacci number"""
    if n < 0:
        return int((-1)**(n+1))*fib_iter(1, 0, 0, 1, abs(n))
    else:
        return fib_iter(1, 0, 0, 1, n)


def fib_iter(a, b, p, q, count):
    if not count:
        return b
    elif not count % 2:
        return fib_iter(a, b, p**2+q**2, q**2+2*p*q, count / 2)
    else:
        return fib_iter(a*q+b*q+a*p, b*p+a*q, p, q, count - 1)


# for i in range(-10, 11, 1):
#     print(i, fib(i))
print(fib(1000000))
