# 1 
# https://projecteuler.net/problem=1
# Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000


def get_sum_multiples(x=3, y=5, MAX=1000, formula = 'triangular'):
    
    '''#1 
    https://projecteuler.net/problem=1
    Multiples of 3 and 5
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
    The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000
    '''

    # How many 3s and 5s could fit into MAX? Call these n3 and n5 (or nx and ny because they are variables)
    nx = (MAX-1) // x # floor or integer division
    ny = (MAX-1) // y
    nxy = (MAX-1) // (x*y)

    # Factor integers 3 and 5 from MAX. There will be n3 multiples of 3 up to MA 
    # In brackets we have a sequence, sum of the sequence is the following formula
    # 3 x (1 + 2 + 3 + ... + n3)
    # 5 x (1 + 2 + 3 + ... + n5)

    # nth triangular number (Gauss: group 1 and n to give n+1, group 2 and n-1 to give n+1 ... there are n/2 groupings)
    # This is also the formula for Sum of small powers with power k = 1  

    S_1_nx = nx * (nx + 1) / 2   
    S_1_ny = ny * (ny + 1) / 2
    # these are in both series so need to filter out one instance
    S_1_nxy = nxy * (nxy + 1) / 2

    s = x*S_1_nx + y*S_1_ny - x*y*S_1_nxy


    """
        # Alternatively can use the formula for the sum of an arithmetic series S = (n/2) * (a_1 + a_n) 
        # with a_1 = x, n = nx and a_n = x*nx to give the same calculation
        # (nx/2) * (x + x*nx)  =  nx * x * (1 + nx) / 2
        s_ax =  (nx/2) * (x + x*nx)
        s_ay =  (ny/2) * (y + y*ny)
        s_axy = (nxy/2) * (x*y + x*y*nxy)
        s = s_ax + s_ay - s_axy
    """    
    
    return s


if __name__ == "__main__":

    x = input("Enter the first integer or hit return to leave it blank:\n" or 3)
    y = input("Enter the second integer or hit return to leave it blank:\n" or 5)
    MAX = input("Enter the maximum integer or hit return to leave it blank:\n" or 1000)
    
    try: 
        x = int(x)
        y = int(y)
        MAX = int(MAX)

    except (ValueError) as e:
        print("Please ensure you enter a number or nothing, text and special characters are not accepted: {0}".format(e))

    s = get_sum_multiples(x, y, MAX)
    
    print (s)