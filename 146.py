import math
import random
 
from random import randrange
# https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test


def is_strong_pseudoprime(n, a):
    '''
    The bitwise shift would save calculation on bigger numbers, not a big difference up to 150million
    leaving in incase is needed
    https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    '''
    d, s = n-1, 0

    # while d % 2**6 == 0:
    #     d, s = d >> 5, s+6

    # while d % 2**5 == 0:
    #     d, s = d >> 4, s+5

    # while d % 2**4 == 0:
    #     d, s = d >> 3, s+4

    while d % 2**3 == 0:
        d, s = d >> 2, s+3

    while d % 2 == 0:
        d, s = d/2, s+1

    t = pow(a, d, n)

    if t == 1:
        return True

    while s > 0:
        if t == n - 1:
            return True

        t, s = pow(t, 2, n), s - 1

    return False

def is_prime(n):
    '''
    For the pyramid of doom see https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    section Deterministic variants

    if n < 2,047, it is enough to test a = 2;
    if n < 1,373,653, it is enough to test a = 2 and 3;
    if n < 9,080,191, it is enough to test a = 31 and 73;
    if n < 25,326,001, it is enough to test a = 2, 3, and 5;
    if n < 3,215,031,751, it is enough to test a = 2, 3, 5, and 7;
    if n < 4,759,123,141, it is enough to test a = 2, 7, and 61;
    if n < 1,122,004,669,633, it is enough to test a = 2, 13, 23, and 1662803;
    if n < 2,152,302,898,747, it is enough to test a = 2, 3, 5, 7, and 11;
    if n < 3,474,749,660,383, it is enough to test a = 2, 3, 5, 7, 11, and 13;
    if n < 341,550,071,728,321, it is enough to test a = 2, 3, 5, 7, 11, 13, and 17.

    '''

    if n % 2 == 0:
        return n == 2

    if n < 2047:
        a = [2]
    if n < 1373653:
        a = [2, 3]
    if n < 9080191:
        a = [31, 73]
    if n < 25326001:
        a = [2, 3, 5]
    if n < 3215031751:
        a = [2, 3, 5, 7]
    if n < 4759123141:
        a = [2, 7, 61]
    if n < 1122004669633:
        a = [2, 13, 23, 1662803]
    if n < 2152302898747:
        a = [2, 3, 5, 7, 11]
    if n < 3474749660383:
        a = [2, 3, 5, 7, 11, 13]
    if n < 341550071728321:
        a = [2, 3, 5, 7, 11, 13, 17]
    if n < 3825123056546413051:
        a = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    else:
        a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    for i in a:
        if not is_strong_pseudoprime(n, i):
            return False

    return True



def run():
    # order is reversed because more numbers fails on 13 and 1 than 27 and 3
    numbers_to_add = [
        13, 1, 9,  3, 7, 27
    ]
    max_num = 150 * 1000000

    s = 0

    for num in range(10, max_num, 10):
        if (num % 3 == 0):
            continue
        if (num % 7 != 3 and num % 7 != 4):
            continue
        if (num % 13 == 0 or num % 13 == 2 or num % 13 == 5 or num % 13 == 8 or num % 11 == 0):
            continue
          
        squared = num * num
        for num_to_add in numbers_to_add:
            temp = squared + num_to_add

            if not is_prime(temp):
                break
        else:
            # test for consecutiveness
            l = len([i for i in range(squared, squared+28) if is_prime(i)])
            if l == 6:
                print(num, l)
                s += num

    return s


if __name__ == "__main__":
    result = run()
    print(result)
