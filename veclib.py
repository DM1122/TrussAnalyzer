# David Maranto
# A library containing useful vector operations
# Rev 2.0

import math


def mag(a):
    '''
    Returns magnitiude of vector a.

    Args:
     a (list): vector

    >>>mag([1,1])
    1.4142135623730951
    '''

    sum = 0
    for e in a:
        sum += e**2

    mag = math.sqrt(sum)


    return mag


def sub(a,b):
    '''
    Subtracts vectors a b and returns vector c. Assumes vectors are of equal dims.

    Args:
     a (list): point/vector at tail
     b (list): point/vector at head

    >>>vecsub([1,2], [3,4])
    [2,2]
    '''

    c = [b[i]-a[i] for i in range(len(a))]


    return c

def add(a,b):
    '''
    Adds vectors a b and returns vec c. Assumes vectors are of equal dims.

    Args:
     a (list): point/vector
     b (list): point/vector
    '''

    c = [b[i]+a[i] for i in range(len(a))]

    return c


def magsub(a,b):
    '''
    Combined mag and sub functions: mag(sub())
    '''

    c = mag(sub(a,b))

    return c


def magadd(a,b):
    '''
    Combined mag and add functions: mag(add())
    '''

    c = mag(add(a,b))

    return c


def unit(a):
    '''
    Returns a unit vector in the same direction as a.

    Args:
     a (list): a vector

    >>>unit([2,2])
    [1,1]
    '''

    a_mag = mag(a)
    a_unit = [a[i]/a_mag for i in range(len(a))]


    return a_unit


def dot(a,b):
    '''
    Computes the dot product between two vectors. Assumes equal dims.

    Args:
     a (list): vector
     b (list): vector
    
    >>>dot([1,2], [3,4])
    11
    '''

    dot = 0
    for i in range(len(a)):
        dot += a[i]*b[i]

    #sum((a*b) for a, b in zip(v1, v2))

    return dot


def scal(a,c):
    '''
    Performs scalar multiplication on vector a by scalar c.

    Args:
     a (list): vector
     c (num): scalar
    
    >>>scal([1,2], 3)
    [3,6]
    '''

    a = [a[i]*c for i in range(len(a))]


    return a


def proj(a,b):
    '''
    Projects vector a onto b

    Args:
     a (list): vector to be projected
     b (list): vector to be projected onto
    
    >>>proj([1,1], [1,0])
    [1,0]
    '''

    # may consider deriving projection from cosine formula instead
    scalar = dot(a, unit(b))

    proj = scal(unit(b), scalar)


    return proj


def cross(a,b):
    '''
    Returns the cross of two vectors. Assumes vectors exist in R3. Will pad vectors in < R3 automatically.

    Args:
     a (list): vector
     b (list): vector
    
    >>>cross([1,0,0], [0,1,0])
    [0,0,1]
    '''
    
    # padding
    while len(a) != 3:
        a.append(0)

    while len(b) != 3:
        b.append(0)


    c = []
    c.append(a[1]*b[2] - a[2]*b[1])
    c.append(a[2]*b[0] - a[0]*b[2])
    c.append(a[0]*b[1] - a[1]*b[0])


    return c


def ang(a,b):
    '''
    Computes the angle between vectors a and b. Returns angle in degrees.

    Args:
     a (list): vector
     b (list): vector
    
    >>>ang([1,1], [1,0])
    45
    '''

    # Not working for ang > 90
    # adj = mag(proj(a,b))
    # hyp = mag(a)

    # ang = math.acos(adj / hyp)

    ang = math.acos( dot(a,b) / (mag(a)*mag(b)) )


    return math.degrees(ang)



if __name__ == '__main__':
    a = [1,1]
    b = [1,-1]
    c = 2

    print("Testing veclib...")
    print('a:', a)
    print('b:', b)

    print('ang():', ang(a,b))
    print('cross():', cross(a,b))
    print('dot():', dot(a,b))
    print('mag():', mag(a))
    print('proj():', proj(a,b))
    print('scal():', scal(a,c))
    print('sub():', sub(a,b))
    print('unit():', unit(a))

