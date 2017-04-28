import sys
from fractions import gcd

if __name__ == '__main__':
    limit = 50
    """3 triangle types:
       (0,0), p on x-axis, q on y-axis, right angle in origin (0,0);
       (0,0), p on x-axis, q neither on x- nor on y-axis, right angle in p;
       (0,0), p on y-axis, q neither on x- nor on y-axis, right angle in p:
    """
    total = 3 * limit ** 2
    """
        4th triangle type:
        (0,0), p neither on x- nor on y-axis, q above/left of p, right angle in p:
    """
    for x in xrange(1, limit+1):
        for y in xrange(1, limit+1):
            # GCD of p(x,y) coordinates determines smallest p - q line increment
            g = gcd(x, y)
            # Number of p - q increments fitting between p and upper grid boundary
            f1 = g * (limit - y) / x
            # Number of p - q increments fitting between p and left grid boundary
            f2 = g * x / y
            # Pick smallest because the other is out of boundary
            if f1 <= f2:
                # Factor 2 because this type can be mirrored through x = y axis (5th type)
                total += 2 * f1
            else:
                total += 2 * f2

    print(total)
