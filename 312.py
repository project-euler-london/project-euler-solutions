def C(n, mod):
    if n < 3:
        return 1
    fu = 2
    fd = 3
    for i in xrange(3, n):
        fu, fd = (2 * fu * fu * fd) % mod, (2 * fu * fd * fd) % mod
    return (fu ** 3) % mod

print C(3, 10000000000000000)
print C(5, 10000000000000000)
print C(10000, 10**8)
print C(10000, 13**8)

CYCLE_LEN = 28960854
print C(C(C(10000, CYCLE_LEN), CYCLE_LEN), 13**8)
