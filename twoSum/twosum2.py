def twopass1(A, target):
    
    seen = {}
    result = []
    for i, x in enumerate(A):
        y = target - x

        if x not in seen:
            seen[x] = 1

        if y in seen and y != x:
            if [x, y] not in result:
                result.append([x, y])
               
    return result

def twopass2(nums, target):
    
    sort = lambda x, y: [x, y] if y > x else [y, x]

    ht = {}
    result = []
    for i, x in enumerate(nums):
        y = target - x

        if x not in ht:
            ht[x] = [i]
        else:
            ht[x].append(i)

        if y in ht and y != x:
            result.append(sort(x, y))

    return result

def twopass3(A, target):

    if A == [] or target < 0:
        return None
    
    sort = lambda x, y: (x, y) if y > x else (y, x)

    seen = dict()
    result = set()
    for i, x in enumerate(A):
        y = target - x

        if x not in seen:
            seen[x] = i
        
        if y in seen and seen[y] != i:
            result.add( sort(x,y) )

    return [list(L) for L in result]
    #return list(result)


if __name__ == '__main__':
    A = [ 5, 3, 6, 7, 8, 1, 4, 2]
    #A = [ 5, 3, 8, 0, 1, 4, 4, 4, 4]
    x = 8

    result = twopass1(A, x)
    print(result)

    result = twopass2(A, x)
    print(result)
    result = twopass3(A, x)
    print(result)