
def get_factors(n):
    
    x = 2
    result = []
    fd = {}
    while x not in fd and x < n//2:
        y = n // x
        if x*y == n:
            fd[x] = y
            fd[y] = x
        x += 1

    result = [(k, v) for k, v in fd.items()]
    return result


if __name__ == '__main__':
    for i in range(35):
        print("{}: {}".format(i, get_factors(i)))