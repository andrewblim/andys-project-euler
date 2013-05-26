
def sumsq(n):
    return sum([x**2 for x in range(1,n+1)])

def sqsum(n):
    return (n*(n+1)/2)**2

if __name__ == '__main__':
    print(sqsum(100) - sumsq(100))