def fib_series(n):

    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    series = fib_series(n - 1)
    series.append(series[-1] + series[-2])
    return series

ans=fib_series(5)
print(ans)