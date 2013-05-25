
import itertools
import math

def isPalindrome(n):
    order = int(math.log(n, 10)) + 1
    for i in range(int(order/2)):
        d1 = int((n % 10**(i+1)) / 10**i)
        d2 = int((n % 10**(order-i)) / 10**(order-i-1))
        if d1 != d2:
            return False
    return True

def largestPalindromeProduct(n):
    
    li, lj = 0, 0
    for (i,j) in itertools.product(range(10**n-1, 10**(n-1)-1, -1), 
                                   range(10**n-1, 10**(n-1)-1, -1)):
        if i+j > 2*(li*lj)**0.5 and isPalindrome(i*j) and i*j > li*lj:
            li = i
            lj = j
    return (li, lj)

if __name__ == '__main__':
    li, lj = largestPalindromeProduct(3)
    print(li, lj, li*lj)