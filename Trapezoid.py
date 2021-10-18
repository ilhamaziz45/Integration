# Import Package
import matplotlib.pyplot as plt
import time

# membuat fungsi integral
def funcSingle(x):
    return (5*x**7) - (9*x**4) + (4*x) - 2

def funcDouble(x, y):
    return (5*x**7) - (9*y**4) + (4*x) - 2

def funcTriple(x, y, z):
    return (5*x**7) - (9*y**4) + (4*z) - 2

# Nilai Exact
lipat1 = 234880.40
lipat2 = 328064.80
lipat3 = 656401.60

# mendeklarasikan rumus perhitungan
def trapezoidSingle(a, b, n):
    h = float(b-a)/n
    hA = h
    result = 0.5*funcSingle(a) + 0.5*funcSingle(b)
    for i in range(n):
        result += funcSingle(a + i*h)
    result *= hA
    return result

def trapezoidDouble(a, b, c, d, n):
    dx = (b - a) / n
    dy = (d - c) / n
    hA = dx * dy
    I = funcDouble(a, c) + funcDouble(b, d)
    for i in range(n):
        for j in range(n):
            xx = a + i * dx
            yy = c + j * dy
            I += funcDouble(xx, yy)
    I *= hA
    return I

def trapezoidTriple(a, b, c, d, g, h, n):
    dx = (b - a) / n
    dy = (d - c) / n
    dz = (h - g) / n
    hA = dx * dy * dz 
    I = funcTriple(a, c, g) + funcTriple(b, d, h)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                xx = a + i * dx
                yy = c + j * dy
                zz = g + k * dz
                I += funcTriple(xx, yy, zz)
    I *= hA
    return I

# Memanggil fungsi
mulaiSingleTrapezoid = time.time()
numericalSingleTrapezoid = trapezoidSingle(3, 5, 100)
stopSingleTrapezoid = time.time()
waktuSingleTrapezoid = stopSingleTrapezoid - mulaiSingleTrapezoid

mulaiDoubleTrapezoid = time.time()
numericalDoubleTrapezoid = trapezoidDouble(3, 5, 7, 9, 100)
stopDoubleTrapezoid = time.time()
waktuDoubleTrapezoid = stopDoubleTrapezoid - mulaiDoubleTrapezoid

mulaiTripleTrapezoid = time.time()
numericalTripleTrapezoid = trapezoidTriple(3, 5, 7, 9, 11, 13, 100)
stopTripleTrapezoid = time.time()
waktuTripleTrapezoid = stopTripleTrapezoid - mulaiTripleTrapezoid

print('\nSingle Trapezoid Integration :', numericalSingleTrapezoid)
print('Waktu Komputasi Single Trapezoid :', waktuSingleTrapezoid)
print('Error Single Trapezoid :', ((lipat1 - numericalSingleTrapezoid)/numericalSingleTrapezoid))

print('\nDouble Trapezoid Integration :', numericalDoubleTrapezoid)
print('Waktu Komputasi Double Trapezoid :', waktuDoubleTrapezoid)
print('Error Single Trapezoid :', ((lipat2 - numericalDoubleTrapezoid)/numericalDoubleTrapezoid))

print('\nDouble Trapezoid Integration :', numericalTripleTrapezoid)
print('Waktu Komputasi Triple Trapezoid :', waktuTripleTrapezoid)
print('Error Single Trapezoid :', ((lipat3 - numericalTripleTrapezoid)/numericalTripleTrapezoid))

# Plotting grafik komparasi waktu komputasi dengan jumlah N
data = {'Lipat-1':waktuSingleTrapezoid, 'Lipat-2':waktuDoubleTrapezoid, 'Lipat-3':waktuTripleTrapezoid}
parameter = list(data.keys())
nilai = list(data.values())
plt.bar(parameter, nilai, color='green', width=0.3)
plt.title('Grafik Waktu Komputasi Integrasi Metode Trapezoid')
plt.xlabel('Integal Lipat')
plt.ylabel('Waktu Komputasi')
plt.show()
