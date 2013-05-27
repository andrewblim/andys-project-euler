
def sumsq(n):
    return n*(n+1)*(2*n+1)/6

def sqsum(n):
    return (n*(n+1)/2)**2

if __name__ == '__main__':
    print(sqsum(100) - sumsq(100))