
def primeList(n):
    i = 2
    primes = []
    while len(primes) < n:
        isPrime = True
        for prime in primes:
            if i % prime == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)
        i += 1
    return primes

if __name__ == '__main__':
    print(primeList(10001)[10000])