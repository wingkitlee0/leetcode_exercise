def jump(p):
    np = len(p)
    if p[0] == '*':
        j = 0
        while j <= np-2:
            if p[j] == '*':
                j += 1
            else:
                break
        return j

if __name__ == '__main__':
    p = '*'
    j = jump(p)

    print(p, j)