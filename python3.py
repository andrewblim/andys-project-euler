
def largestPrimeFactor(n):
    i = 2
    while i <= n**0.5:
        if n % i == 0:
            n = n/i
        i += 1
    return n

if __name__ == '__main__':
    print(largestPrimeFactor(600851475143))