# I suggest you to run this code from PC terminal for appropriate layout

import matplotlib.pyplot as plt
import time

def funcSingle(x):
    return (5*x**7) - (9*x**4) + (4*x) - 2

def funcDouble(x, y):
    return (5*x**7) - (9*y**4) + (4*x) - 2

def funcTriple(x, y, z):
    return (5*x**7) - (9*y**4) + (4*z) - 2

# Nilai Exact
exact1 = 234880.40
exact2 = 328064.80
exact3 = 656385.60

def midpointSingle(f, a, b, n):
    hx = float((b-a)/n)
    I = 0
    for i in range (n):
        xi = a+hx/2+i*hx
        I += hx*f(xi)
    return I

def midpointDouble(f, a, b, c, d, n):
    hx = float((b-a)/n)
    hy = float((d-c)/n)
    I = 0
    for i in range(n):
        for j in range(n):
            xi = a+hx/2+i*hx
            yj = c+hy/2+j*hy 
            I += hx*hy*f(xi, yj)
    return I

def midpointTriple(f, a, b, c, d, g, h, n):
    hx = float((b-a)/n)
    hy = float((d-c)/n)
    hz = float((h-g)/n)
    I = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                xi = a+hx/2+i*hx
                yj = c+hy/2+j*hy
                zk = g+hz/2+k*hy
                I += hx*hy*hz*f(xi, yj, zk)
    return I

startSingle = time.time()
numericalSingle = round(midpointSingle(funcSingle, 3, 5, 50), 2)
stopSingle = time.time()
timeSingle = round(stopSingle - startSingle, 5)

startDouble = time.time()
numericalDouble = round(midpointDouble(funcDouble, 3, 5, 7, 9, 50), 2)
stopDouble = time.time()
timeDouble = round(stopDouble - startDouble, 5)

startTriple = time.time()
numericalTriple = round(midpointTriple(funcTriple, 3, 5, 7, 9, 11, 13, 50), 2)
stopTriple = time.time()
timeTriple = round(stopTriple - startTriple, 5)

print('\nExact Value of Single Midpoint Integration :\t', exact1)
print('\tSingle Midpoint Integration :\t\t', numericalSingle)
print('\tTime for Single Midpoint :\t\t', timeSingle)
print('\tError Single Midpoint Integration :\t', (exact1 - numericalSingle)/numericalSingle)

print('\nExact Value Double Midpoint Integration :\t', exact2)
print('\tDouble Midpoint Integration :\t\t', numericalDouble)
print('\tTime for Double Midpoint :\t\t', timeDouble)
print('\tError Double Midpoint Integration :\t', (exact2 - numericalDouble)/numericalDouble)

print('\nExact Value Triple Midpoint Integration :\t', exact3)
print('\tTriple Midpoint Integration :\t\t', numericalTriple)
print('\tTime of Triple Midpoint :\t\t', timeTriple)
print('\tError Triple Midpoint Integration :\t', (exact3 - numericalTriple)/numericalTriple)

data = {'Single':timeSingle, 'Double':timeDouble, 'Triple':timeTriple}
parameter = list(data.keys())
value = list(data.values())
plt.bar(parameter, value, color='green', width=0.3)
plt.title('Computing Time Integration')
plt.xlabel('Level of Integral')
plt.ylabel('Komputing Time')
plt.show()
