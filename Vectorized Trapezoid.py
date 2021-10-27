from numpy import linspace
import time

def funcSingle(x):
    return (5*x**7) - (9*x**4) + (4*x) - 2

def funcDouble(x, y):
    return (5*x**7) - (9*y**4) + (4*x) - 2

def funcTriple(x, y, z):
    return (5*x**7) - (9*y**4) + (4*z) - 2

# Nilai Exact
lipat1 = 234880.40
lipat2 = 328064.80
lipat3 = 656385.60

def SingleVectorizedTrapezoid(f, a, b, n):
    hx = float(b - a)/n
    hA = hx
    x = linspace(a,b, n+1)
    hasil = sum(f(x)) - 0.5*f(a) - 0.5*f(b)
    return hA*hasil

def DoubleVectorizedTrapezoid(f, a, b, c, d, n):
    hx = float(b - a) / n
    hy = float(d - c) / n
    hA = hx*hy
    x = linspace(a, b, n + 1)
    y = linspace(c, d, n + 1)
    hasil = sum(f(x, y)) - (0.5*f(a, c)) - (0.5*f(b, d))
    return hA*hasil*n

def TripleVectorizedTrapezoid(f, a, b, c, d, g, h, n):
    hx = float(b - a) / n
    hy = float(d - c) / n
    hz = float(h - g) / n
    hA = hx*hy*hz
    x = linspace(a, b, n + 1)
    y = linspace(c, d, n + 1)
    z = linspace(h, g, n + 1)
    hasil = sum(f(x, y, z)) - (0.5*f(a, c, g)) - (0.5*f(b, d, h))
    return hA*hasil*(n**2)

mulaiSingleVectorizedTrapezoid = time.time()
numericalSingleVectorizedTrapezoid = SingleVectorizedTrapezoid(funcSingle, 3, 5, 50)
stopSingleVectorizedTrapezoid = time.time()
waktuSingleVectorizedTrapezoid = stopSingleVectorizedTrapezoid - mulaiSingleVectorizedTrapezoid

mulaiDoubleVectorizedTrapezoid = time.time()
numericalDoubleVectorizedTrapezoid = DoubleVectorizedTrapezoid(funcDouble, 3, 5, 7, 9, 50)
stopDoubleVectorizedTrapezoid = time.time()
waktuDoubleVectorizedTrapezoid = stopDoubleVectorizedTrapezoid - mulaiDoubleVectorizedTrapezoid

mulaiTripleVectorizedTrapezoid = time.time()
numericalTripleVectorizedTrapezoid = TripleVectorizedTrapezoid(funcTriple, 3, 5, 7, 9, 11, 13, 50)
stopTripleVectorizedTrapezoid = time.time()
waktuTripleVectorizedTrapezoid = stopTripleVectorizedTrapezoid - mulaiTripleVectorizedTrapezoid

print('\nSingle Vectorized Midpoint :', numericalSingleVectorizedTrapezoid)
print('Waktu Komputasi Single Vectorized Trapezoid :', waktuSingleVectorizedTrapezoid)
print('Error Single Vectorized Midpoint :', abs(lipat1 - numericalSingleVectorizedTrapezoid)/numericalSingleVectorizedTrapezoid)

print('\nDouble Vectorized Midpoint :', numericalDoubleVectorizedTrapezoid)
print('Waktu Komputasi Double Vectorized Trapezoid', waktuDoubleVectorizedTrapezoid)
print('Error Double Vectorized Midpoint :', abs(lipat2 - numericalDoubleVectorizedTrapezoid)/numericalDoubleVectorizedTrapezoid)

print('\nTriple Vectorized Midpoint :', numericalTripleVectorizedTrapezoid)
print('Waktu Komputasi Triple Vectorized Trapezoid :', waktuTripleVectorizedTrapezoid)
print('Error Triple Vectorized Midpoint :', abs(lipat3 - numericalTripleVectorizedTrapezoid)/numericalTripleVectorizedTrapezoid)
