MAX = 100000000

x = 7
y = 5

s = 0

while x+y < MAX:
    s += MAX/(x+y)
    newx = 3*x + 4*y
    newy = 3*y + 2*x
    x = newx
    y = newy

print s
