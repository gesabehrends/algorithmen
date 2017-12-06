

def coinChangeGreedy(money, coins):
    n = len(coins)
    returnCoins = []
    while( n > 0):
        n -= 1
        returnCoins.append(money//coins[n])
        money = money%coins[n]
    return sum(returnCoins)

def coinChangeDynamic(money, coins):

    matrix = [list(range(0,money + 1))]

    for i in range(1, len(coins)):
        listForCoin = []
        for j in range(money+1):
            if (j) < coins[i]:
                listForCoin.append(matrix[i - 1][j])
            elif j == coins[i]:
                listForCoin.append(1)
            else: 
                possibilities = []
                for k in range((j // coins[i])+1):
                    value = matrix[i-1][j-k*coins[i]] + k
                    possibilities.append(value)
                listForCoin.append(min(possibilities))
        matrix.append(listForCoin)

    return matrix[len(coins)-1][money]


def compareGreedyToDynamic(coins):

    funktioniert = True
    for i in range(1, calculatekgV(coins)):
        if( coinChangeDynamic(i, coins) == coinChangeGreedy(i, coins)):
            funktioniert &= True
        else:
            funktioniert &= False
    return funktioniert

def calculatekgV(coins):
    def ggT(m,n):
        if (n==0):
            return m
        else:
            return ggT(n, m%n)

    def kgV(m,n):
        o = ggT(m,n)
        p = (m * n) // o
        return p

    if len(coins) < 1: return 1
    if len(coins) == 2:
        return kgV(coins[0], coins[1])
    else:
        l = 1
        for i in range(len(coins)):
            l = kgV(l, coins[i])
        return l


