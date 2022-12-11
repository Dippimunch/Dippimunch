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

def walk_steps(steps):
    start = [0, 0, 0, 0]

    for i in range(steps):
        chance = rand.randrange(4)
        r = rand.randrange(4)
        
        if chance <= 1:
            start[r] += 1

        if chance > 1:
            start[r] -= 1
    print(start, distance([0,0,0,0], start))

def mult(n, steps):
    for i in range(n):
        walk_steps(steps)

def distance(x1, x2):
    if len(x1) == len(x2):
        dim = len(x1)
        values = []
        for i in range(dim):
            values.append(np.square((x2[i]-x1[i])))
        distance = math.sqrt(sum(values))
        return distance
                                    

mult(1000, 1000)     
    


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
