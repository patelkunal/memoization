from memoization import memo


@memo
def fibo2(n):
    if n in (0, 1):
        return n
    return fibo2(n - 1) + fibo2(n - 2)


def fibo(n):
    if n in (0, 1):
        return n
    return fibo(n - 1) + fibo(n - 2)


def fibo3(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    n = 100

    import time
    starttime = time.clock()
    fibo(n)
    print("recursive fibo  = %f sec" % (time.clock() - starttime))

    starttime = time.clock()
    fibo2(n)
    print("memoized fibo  = %f sec" % (time.clock() - starttime))
    
    starttime = time.clock()
    fibo3(n)
    print("iterative fibo  = %f sec" % (time.clock() - starttime))
