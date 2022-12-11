import numpy as np
import random as rand
import math


# n-dimensional random walk
# 1D 2 directions
# 2D 4 directions
# 3D 6...
# 4D 8
# 5D 10
# 6D 12
# 7D 14
# 8D 16
# I guess it makes sense if x+1 then the doubled term is +1*2 as well

dimension = 2

def walk_dir(n):
    directions = []
    for i in range(n):
        directions.append('x%i+'%(i+1))
        directions.append('x%i-'%(i+1))
    print(directions)

def walk_steps(steps, dim):
    initial = np.zeros(dim, int)
    start = np.zeros(dim, int)

    for i in range(steps):
        # 50/50 for +/-
        chance = rand.randrange(4)

        # random direction
        r = rand.randrange(len(start))

        if chance <= 1:
            start[r] += 1

        if chance > 1:
            start[r] -= 1
    print(start, distance(initial, start))

def mult(n, steps, dim):
    for i in range(n):
        walk_steps(steps, dim)

def distance(x1, x2):
    if len(x1) == len(x2):
        dim = len(x1)
        values = []
        for i in range(dim):
            values.append(np.square((x2[i]-x1[i])))
        distance = math.sqrt(sum(values))
        return distance
                                    

#mult(100, 1000000, 5)


def recurrence(dim):
    initial = np.zeros(dim, int)
    start = np.zeros(dim, int)
    time = 0

    # Get 'em rollin'
    cchance = rand.randrange(4)
    rr = rand.randrange(len(start))
    #print(time, start)
    
    if cchance <= 1:
        start[rr] += 1

    if cchance > 1:
        start[rr] -= 1
    time += 1

    

    while start != initial:
        """if start != initial:
            print('away')
        elif start == initial:
            print('HOME!!')"""
            
        chance = rand.randrange(4)
        r = rand.randrange(len(start))

        time += 1
        
        if chance <= 1:
            start[r] += 1

        if chance > 1:
            start[r] -= 1

        #print(time, start)

    print('ReCURRED AFTER %i STEPS!!'%time)

recurrence(1)


def random_walk(n, pop):
    pass

























# n-simplex
# d = dimension
def nsimplex_faces(n):
    faces = int(((n+1)*n)/2)
    return faces

def doubles(n):
    for i in range(n):
        j = 2 * i
        print(i,j)

# From ChatGPT
"""# Python code for 2D random walk.
import numpy
import matplotlib.pyplot
import random

# defining the number of steps
n = 10

#creating two array for containing x and y coordinate
#of size equals to the number of size and filled up with 0's
x = numpy.zeros(n)
y = numpy.zeros(n)

# filling the coordinates with random variables
for i in range(1, n):
    val = random.randint(1, 4)
if val == 1:
    x[i] = x[i - 1] + 1
    y[i] = y[i - 1]
elif val == 2:
    x[i] = x[i - 1] - 1
    y[i] = y[i - 1]
elif val == 3:
    x[i] = x[i - 1]
    y[i] = y[i - 1] + 1
else:
    x[i] = x[i - 1]
    y[i] = y[i - 1] - 1


# plotting stuff:
matplotlib.pyplot.title("Random Walk ($n = " + str(n) + "$ steps)")
matplotlib.pyplot.plot(x, y)
matplotlib.pyplot.savefig("rand_walk"+str(n)+".png",bbox_inches="tight",dpi=600)
matplotlib.pyplot.show()"""
