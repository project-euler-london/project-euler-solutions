'''
http://oeis.org/A198257
Number of meanders of length (n+1)*5 which are composed by arcs of equal length and a central angle of 72 degrees.
Definition of a meander:
A binary curve C is a triple (m, S, dir) such that
(a) S is a list with values in {L,R} which starts with an L,
(b) dir is a list of m different values, each value of S being allocated a value of dir,
(c) consecutive Ls increment the index of dir,
(d) consecutive Rs decrement the index of dir,
(e) the integer m>0 divides the length of S and
(f) C is a meander if each value of dir occurs length(S)/m times.
For this sequence, m = 5.
The terms are proved by brute force for 0 <= n <= 6, but not yet in general.
'''

'''
a(n) = Sum{k=0..n} Sum{j=0..4} Sum{i=0..4} (-1)^(j+i)*C(i,j)*C(n,k)^5*(n+1)^j*(k+1)^(4-j)/(k+1)^4. - Peter Luschny, Nov 02 2011
a(n) = Sum_{k=0..n} h(n,k)*binomial(n,k)^5, where h(n,k) = (1+k)*(1-((n-k)/(1+k))^5)/(1+2*k-n) if 1+2*k-n <> 0 else h(n,k) = 5. - Peter Luschny, Nov 24 2011
?
'''


# t = (direction, counts), where direction is the direction at the end of the path,
# counts[d] = the count of 'visits' of direction d on the path (0 <= d < 5).
# paths[t] = the number of such paths.

def next_step(paths, limit):
    # limit = the maximum number of visits of any dir on a path = N//5
    newpaths = {}

    for t in paths:
        direction, counts = t

        newcounts = list(counts)

        if newcounts[direction] >= limit:
            continue

        newcounts[direction] += 1
        newcounts = tuple(newcounts)

        for d in ((direction + 1) % 5, (direction - 1) % 5):
            tt = (d, newcounts)
            if tt in newpaths:
                newpaths[tt] += paths[t]
            else:
                newpaths[tt] = paths[t]

    return newpaths

paths = {(0, (0, 0, 0, 0, 0)): 1}
N = 70
n = N // 5

for step in range(N):
    paths = next_step(paths, n)

print(paths[(0, (n, n, n, n, n))])
