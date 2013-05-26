
def factorize(n):
    i = 2
    while i <= n**0.5:
        if n % i == 0:
            factors = [i]
            factors.extend(factorize(n/i))
            return factors
        i += 1
    return [n]

def smallestDivisibleByAll(n):
    factorCounts = {}
    for i in range(2, n+1):
        factors = factorize(i)
        for factor in set(factors):
            factorCount = len(filter(lambda x: x == factor, factors))
            if factor not in factorCounts:
                factorCounts[factor] = factorCount
            else:
                factorCounts[factor] = max(factorCount, factorCounts[factor])
    return reduce(lambda x,y: x*y, [x**y for (x,y) in factorCounts.iteritems()])

if __name__ == '__main__':
    print(smallestDivisibleByAll(20))