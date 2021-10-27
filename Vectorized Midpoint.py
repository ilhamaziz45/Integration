from numpy import linspace #linspace adalah ciri-ciri dari vectorized, dimana data diurutkan dari kecil ke besar
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

def SingleVectorizedMidpoint(f, a, b, n):
    hx = float(b - a) / n
    hA = hx
    xx = linspace(a+hx/2, b-hx/2, n)
    return hA*sum(f(xx))

def DoubleVectorizedMidpoint(f, a, b, c, d, n):
    hx = float(b - a) / (n)
    hy = float(d - c) / (n)
    hA = hx*hy
    xx = linspace(a+hx/2, b-hx/2, n)
    yy = linspace(c+hy/2, d-hy/2, n)
    return hA*sum(f(xx,yy))*n

def TripleVectorizedMidpoint(f, a, b, c, d, g, h, n):
    hx = float(b - a) / (n)
    hy = float(d - c) / (n)
    hz = float(h - g) / (n)
    hA = hx*hy*hz
    xx = linspace(a+hx/2, b-hx/2, n)
    yy = linspace(c+hy/2, d-hy/2, n)
    zz = linspace(h+hz/2, g-hz/2, n)
    return hA*sum(f(xx,yy,zz))*(n**2)

mulaiSingleVectorizedMidpoint = time.time()
numericalSingleVectorizedMidpoint = SingleVectorizedMidpoint(funcSingle, 3, 5, 50)
stopSingleVectorizedMidpoint = time.time()
waktuSingleVectorizedMipoint = stopSingleVectorizedMidpoint - mulaiSingleVectorizedMidpoint

mulaiDoubleVectorizedMidpoint = time.time()
numericalDoubleVectorizedMidpoint = DoubleVectorizedMidpoint(funcDouble, 3, 5, 7, 9, 50)
stopDoubleVectorizedMidpoint = time.time()
waktuDoubleVectorizedMipoint = stopDoubleVectorizedMidpoint - mulaiDoubleVectorizedMidpoint

mulaiTripleVectorizedMidpoint = time.time()
numericalTripleVectorizedMidpoint = TripleVectorizedMidpoint(funcTriple, 3, 5, 7, 9, 11, 13, 50)
stopTripleVectorizedMidpoint = time.time()
waktuTripleVectorizedMipoint = stopTripleVectorizedMidpoint - mulaiTripleVectorizedMidpoint

print('Single Vectorized Midpoint :', numericalSingleVectorizedMidpoint)
print('Waktu Komputasi Single Vectorized Midpoint :', waktuSingleVectorizedMipoint)
print('Error Single Vectorized Midpoint :', (lipat1 - numericalSingleVectorizedMidpoint)/numericalSingleVectorizedMidpoint)

print('\nDouble Vectorized Midpoint :', numericalDoubleVectorizedMidpoint)
print('Waktu Komputasi Double Vectorized Midpoint :', waktuDoubleVectorizedMipoint)
print('Error Double Vectorized Midpoint :', (lipat2 - numericalDoubleVectorizedMidpoint)/numericalDoubleVectorizedMidpoint)

print('\nTriple Vectorized Midpoint :', numericalTripleVectorizedMidpoint)
print('Waktu Komputasi Triple Vectorized Midpoint :', waktuTripleVectorizedMipoint)
print('Error Triple Vectorized Midpoint :', (lipat3 - numericalTripleVectorizedMidpoint)/numericalTripleVectorizedMidpoint)
