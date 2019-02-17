#

def f(amount, coins):
    print("calling f ({}, {})".format(amount, coins))
    if len(coins) == 0:
        return -1

    if len(coins) == 1:
        c = coins[0]
        if amount - (amount // c) * c == 0:
            return amount // c
        else:
            return -1

    if len(coins) >= 2:
        cmin = min(coins)
        cmax = max(coins)
        print("cmin, cmax = ", cmin, cmax)
        if cmin > amount:
            return -1
        else:
            if amount >= cmax:
                nmax = amount // cmax
            else:
                # amount < cmax
                nmax = 0

            print(nmax)
            while nmax >= 0:
                amount_ = amount - cmax * nmax
                coins.remove(cmax)
                print("amount_ = ", amount_)
                res = f(amount_, coins)
                if res == -1:
                    nmax -= 1
                    continue
                else:
                    return res

if __name__=='__main__':
    #res = f(13, [2,5])
    res = f(11, [2,3,5])
    print(res)