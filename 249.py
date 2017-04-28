def primes_to_n(n):
    sieve = [True] * n

    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False] * ((n-i*i-1)/(2*i)+1)

    primes = [2]

    for i in range(3, n, 2):
        if sieve[i]:
            primes.append(i)

    return primes

'''

sequences A000586

0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 - count
1, 0, 1, 1, 0, 2, 0, 2, 1, 1, 2,  1,  2,   2,  2,  2, 3 - result

n=16 has a(16) = 3 partitions into distinct prime parts: 16 = 2+3+11 = 3+13 = 5+11.

Formula: Product_{k=1..inf} (1+x^prime(k)).

https://oeis.org/A000586
'''


def p249(limit=5000, mod=10**16):
    # sequences A000586
    # the coefficents of the expansion of (1+x^Prime[k]) for Prime[k] < StopS
    # (1 + x^2) * (1 + x^3) * (1 + x^5) * (1 + x^7) * (1 + x^11) =
    # x^28+x^26+x^25+2 x^23+2 x^21+x^20+x^19+2 x^18+x^17+2 x^16+x^15+2 x^14+x^13+2 x^12+x^11+2 x^10+x^9+x^8+2 x^7+2 x^5+x^3+x^2+1
    # 1 + 0*x^1 + x^2 + x^3 + 0*x^4 + 2*x^5 + 0*x^6 + 2*x^7 + x^8 + x^9 + 2*x^10
    # 1,  0,      1,    1,    0,      2,      0,      2,      1,    1,    2
    # 1,0,1,1,0,2,0,2,1,1,2

    primes = primes_to_n(limit)
    all_primes = primes_to_n(sum(primes))
    last_prime = all_primes[-1]
    all_primes = set(all_primes)

    # array of number of ways to make that nth prime with primes
    coefficents = [0] * (limit**2 // 2)
    coefficents[0] = 1
    prime_sums = 0
    for prime in primes:

        prime_sums += prime
        for x in reversed(range(prime_sums)):
            coefficents[x + prime] = (coefficents[x + prime] + coefficents[x]) % mod

    return sum([coefficents[i] for i in all_primes]) % mod


print(p249())
