
def findTriplets(n):
    triplets = []
    for a in range(1, n-1):
        for b in range(a+1, n):
            c2 = a**2 + b**2
            if c2 > n**2:
                break
            if int(c2**0.5)**2 == c2:
                triplets.append((a,b,int(c2**0.5)))
    return triplets

if __name__ == '__main__':
    triplet = filter(lambda x: sum(x) == 1000, findTriplets(1000-1-4))[0]
    print(triplet, triplet[0]*triplet[1]*triplet[2])