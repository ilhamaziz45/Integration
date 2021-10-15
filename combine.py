import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace
import pandas as pd
import time

print('=======   Mohammad Ilham Aziz   =======')
print('=======       2006574194        =======')
print('=======     Pemrogramman 01     =======')

df1 = pd.DataFrame(columns=['Jumlah N', 'Hasil Exact', 'Hasil Midpoint', 'Error Midpoint', 'Waktu Midpoint',
                            'Hasil Trapezoidal', 'Error Trapezoidal', 'Waktu Trapezoidal',
                            'Hasil Vec Midpoint', 'Error Vec Midpoint', 'Waktu Vec Midpoint',
                            'Hasil Vec Trapezoidal', 'Error Vec Trapezoidal', 'Waktu Vec Trapezoidal'])

df2 = pd.DataFrame(columns=['Jumlah N', 'Hasil Exact', 'Hasil Midpoint', 'Error Midpoint', 'Waktu Midpoint',
                            'Hasil Trapezoidal', 'Error Trapezoidal', 'Waktu Trapezoidal',
                            'Hasil Vec Midpoint', 'Error Vec Midpoint', 'Waktu Vec Midpoint',
                            'Hasil Vec Trapezoidal', 'Error Vec Trapezoidal', 'Waktu Vec Trapezoidal'])

df3 = pd.DataFrame(columns=['Jumlah N', 'Hasil Exact', 'Hasil Midpoint', 'Error Midpoint', 'Waktu Midpoint',
                            'Hasil Trapezoidal', 'Error Trapezoidal', 'Waktu Trapezoidal',
                            'Hasil Vec Midpoint', 'Error Vec Midpoint', 'Waktu Vec Midpoint',
                            'Hasil Vec Trapezoidal', 'Error Vec Trapezoidal', 'Waktu Vec Trapezoidal'])

df4 = pd.DataFrame(columns=['Jumlah N', 'Hasil Exact',
                            'Hasil Monte Carlo', 'Error Monte Carlo', 'Waktu Monte Carlo'])

def funcSingle(x):
    return (5*x**7) - (9*x**4) + (4*x) - 2

def funcDouble(x, y):
    return (5*x**7) - (9*y**4) + (4*x) - 2

def funcTriple(x, y, z):
    return (5*x**7) - (9*y**4) + (4*z) - 2

def mC(x, y):
    return (1 if (3 <= x <= 5 and 7 <= y <= 9) else -1)

# Nilai Exact
lipat1 = 234880.40
lipat2 = 328064.80
lipat3 = 656385.60

# INTEGRATION LEVEL 1 #
def midpointSingle(f, a, b, n):
    hx = float((b-a)/n)
    I = 0
    for i in range (n):
        xi = a+hx/2+i*hx
        I += hx*f(xi)
    return I

def trapezoidSingle(a, b, n):
    h = float(b-a)/n
    hA = h
    result = 0.5*funcSingle(a) + 0.5*funcSingle(b)
    for i in range(n):
        result += funcSingle(a + i*h)
    result *= hA
    return result

def SingleVectorizedMidpoint(f, a, b, n):
    hx = float(b - a) / n
    hA = hx
    xx = linspace(a+hx/2, b-hx/2, n)
    return hA*sum(f(xx))

def SingleVectorizedTrapezoid(f, a, b, n):
    hx = float(b - a)/n
    hA = hx
    x = linspace(a,b, n+1)
    hasil = sum(f(x)) - 0.5*f(a) - 0.5*f(b)
    return hA*hasil

# INTEGRATION LEVEL 2 #
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

def DoubleVectorizedMidpoint(f, a, b, c, d, n):
    hx = float(b - a) / (n)
    hy = float(d - c) / (n)
    hA = hx*hy
    xx = linspace(a+hx/2, b-hx/2, n)
    yy = linspace(c+hy/2, d-hy/2, n)
    return hA*sum(f(xx,yy))*n

def DoubleVectorizedTrapezoid(f, a, b, c, d, n):
    hx = float(b - a) / n
    hy = float(d - c) / n
    hA = hx*hy
    x = linspace(a, b, n + 1)
    y = linspace(c, d, n + 1)
    hasil = sum(f(x, y)) - (0.5*f(a, c)) - (0.5*f(b, d))
    return hA*hasil*n

# INTEGRATION LEVEL 3 #
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

def TripleVectorizedMidpoint(f, a, b, c, d, g, h, n):
    hx = float(b - a) / (n)
    hy = float(d - c) / (n)
    hz = float(h - g) / (n)
    hA = hx*hy*hz
    xx = linspace(a+hx/2, b-hx/2, n)
    yy = linspace(c+hy/2, d-hy/2, n)
    zz = linspace(h+hz/2, g-hz/2, n)
    return hA*sum(f(xx,yy,zz))*(n**2)

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

# MOONTE CARLO #
def monteCarlo(a, b, c, d, n):
    x = np.random.uniform(a, b, n)
    y = np.random.uniform(c, d, n)
    f_avg = 0
    num_inside = 0
    for i in range(len(x)):
        for j in range(len(y)):
            if mC(x[i], y[j]) >= 0:
                num_inside += 1
                f_avg += funcDouble(x[i], y[j])
    f_avg = f_avg/float(num_inside)
    area = num_inside/float(n**2)*(b - a)*(d - c)
    return area*f_avg


for i in range(1, 5):
    nn = int(input('\n\n\n------------->>> Masukkan jumlah N : '))
    # PERHITUNGAN INTEGRAL LEVEL 1 #
    mulaiSingle = time.time()
    numericalSingle = midpointSingle(funcSingle, 3, 5, nn)
    stopSingle = time.time()
    waktuSingle = stopSingle - mulaiSingle
    errorSingle = abs(lipat1 - numericalSingle)/lipat1

    mulaiSingleTrapezoid = time.time()
    numericalSingleTrapezoid = trapezoidSingle(3, 5, nn)
    stopSingleTrapezoid = time.time()
    waktuSingleTrapezoid = stopSingleTrapezoid - mulaiSingleTrapezoid
    errorSingleTrapezoid = abs(lipat1 - numericalSingleTrapezoid)/lipat1

    mulaiSingleVectorizedMidpoint = time.time()
    numericalSingleVectorizedMidpoint = SingleVectorizedMidpoint(funcSingle, 3, 5, nn)
    stopSingleVectorizedMidpoint = time.time()
    waktuSingleVectorizedMipoint = stopSingleVectorizedMidpoint - mulaiSingleVectorizedMidpoint
    errorSingleVectorizedMidpoint = abs(lipat1 - numericalSingleVectorizedMidpoint)/lipat1

    mulaiSingleVectorizedTrapezoid = time.time()
    numericalSingleVectorizedTrapezoid = SingleVectorizedTrapezoid(funcSingle, 3, 5, nn)
    stopSingleVectorizedTrapezoid = time.time()
    waktuSingleVectorizedTrapezoid = stopSingleVectorizedTrapezoid - mulaiSingleVectorizedTrapezoid
    errorSingleVectorizedTrapezoid = abs(lipat1 - numericalSingleVectorizedTrapezoid)/lipat1

    # PERHITUNGAN INTEGRAL LEVEL 2 #
    mulaiDouble = time.time()
    numericalDouble = (midpointDouble(funcDouble, 3, 5, 7, 9, nn))
    stopDouble = time.time()
    waktuDouble = stopDouble - mulaiDouble
    errorDouble = abs(lipat2 - numericalDouble)/lipat2

    mulaiDoubleTrapezoid = time.time()
    numericalDoubleTrapezoid = trapezoidDouble(3, 5, 7, 9, nn)
    stopDoubleTrapezoid = time.time()
    waktuDoubleTrapezoid = stopDoubleTrapezoid - mulaiDoubleTrapezoid
    errorDoubleTrapezoid = abs(lipat2 - numericalDoubleTrapezoid)/lipat2

    mulaiDoubleVectorizedMidpoint = time.time()
    numericalDoubleVectorizedMidpoint = DoubleVectorizedMidpoint(funcDouble, 3, 5, 7, 9, nn)
    stopDoubleVectorizedMidpoint = time.time()
    waktuDoubleVectorizedMipoint = stopDoubleVectorizedMidpoint - mulaiDoubleVectorizedMidpoint
    errorDoubleVectorizedMidpoint = abs(lipat2 - numericalDoubleVectorizedMidpoint)/lipat2

    mulaiDoubleVectorizedTrapezoid = time.time()
    numericalDoubleVectorizedTrapezoid = DoubleVectorizedTrapezoid(funcDouble, 3, 5, 7, 9, nn)
    stopDoubleVectorizedTrapezoid = time.time()
    waktuDoubleVectorizedTrapezoid = stopDoubleVectorizedTrapezoid - mulaiDoubleVectorizedTrapezoid
    errorDoubleVectorizedTrapezoid = abs(lipat2 - numericalDoubleVectorizedTrapezoid)/lipat2

    # PERHITUNGAN INTEGRAL LEVEL 3 #
    mulaiTriple = time.time()
    numericalTriple = (midpointTriple(funcTriple, 3, 5, 7, 9, 11, 13, nn))
    stopTriple = time.time()
    waktuTriple = stopTriple - mulaiTriple
    errorTriple = abs(lipat3 - numericalTriple)/lipat3

    mulaiTripleTrapezoid = time.time()
    numericalTripleTrapezoid = trapezoidTriple(3, 5, 7, 9, 11, 13, nn)
    stopTripleTrapezoid = time.time()
    waktuTripleTrapezoid = stopTripleTrapezoid - mulaiTripleTrapezoid
    errorTripleTrapezoid = abs(lipat3 - numericalTripleTrapezoid)/lipat3

    mulaiTripleVectorizedMidpoint = time.time()
    numericalTripleVectorizedMidpoint = TripleVectorizedMidpoint(funcTriple, 3, 5, 7, 9, 11, 13, nn)
    stopTripleVectorizedMidpoint = time.time()
    waktuTripleVectorizedMipoint = stopTripleVectorizedMidpoint - mulaiTripleVectorizedMidpoint
    errorTripleVectorizedMidpoint = abs(lipat3 - numericalTripleVectorizedMidpoint)/lipat3

    mulaiTripleVectorizedTrapezoid = time.time()
    numericalTripleVectorizedTrapezoid = TripleVectorizedTrapezoid(funcTriple, 3, 5, 7, 9, 11, 13, nn)
    stopTripleVectorizedTrapezoid = time.time()
    waktuTripleVectorizedTrapezoid = stopTripleVectorizedTrapezoid - mulaiTripleVectorizedTrapezoid
    errorTripleVectorizedTrapezoid = abs(lipat3 - numericalTripleVectorizedTrapezoid)/lipat3

    # PERHITUNGAN MONTE CARLO #
    mulaiMonteCarlo = time.time()
    numericalMonteCarlo = monteCarlo(3, 5, 7, 9, nn)
    stopMonteCarlo = time.time()
    waktuMonteCarlo = stopMonteCarlo - mulaiMonteCarlo
    errorMonteCarlo = abs(lipat2 - numericalMonteCarlo)/lipat2

    # MEMASUKKAN ITEM INTEGRAL LEVEL 1 KE DATA FRAME PANDAS #
    df1.at[i, 'Jumlah N'] = nn
    df1.at[i, 'Hasil Exact'] = lipat1

    df1.at[i, 'Hasil Midpoint'] = numericalSingle
    df1.at[i, 'Error Midpoint'] = errorSingle
    df1.at[i, 'Waktu Midpoint'] = waktuSingle

    df1.at[i, 'Hasil Trapezoidal'] = numericalSingleTrapezoid
    df1.at[i, 'Error Trapezoidal'] = errorSingleTrapezoid
    df1.at[i, 'Waktu Trapezoidal'] = waktuSingleTrapezoid
    
    df1.at[i, 'Hasil Vec Midpoint'] = numericalSingleVectorizedMidpoint
    df1.at[i, 'Error Vec Midpoint'] = errorSingleVectorizedMidpoint
    df1.at[i, 'Waktu Vec Midpoint'] = waktuSingleVectorizedMipoint

    df1.at[i, 'Hasil Vec Trapezoidal'] = numericalSingleVectorizedTrapezoid
    df1.at[i, 'Error Vec Trapezoidal'] = errorSingleVectorizedTrapezoid
    df1.at[i, 'Waktu Vec Trapezoidal'] = waktuSingleVectorizedTrapezoid
    
    # MEMASUKKAN ITEM INTEGRAL LEVEL 2 KE DATA FRAME PANDAS #
    df2.at[i, 'Jumlah N'] = nn
    df2.at[i, 'Hasil Exact'] = lipat2

    df2.at[i, 'Hasil Midpoint'] = numericalDouble
    df2.at[i, 'Error Midpoint'] = errorDouble
    df2.at[i, 'Waktu Midpoint'] = waktuDouble

    df2.at[i, 'Hasil Trapezoidal'] = numericalDoubleTrapezoid
    df2.at[i, 'Error Trapezoidal'] = errorDoubleTrapezoid
    df2.at[i, 'Waktu Trapezoidal'] = waktuDoubleTrapezoid
    
    df2.at[i, 'Hasil Vec Midpoint'] = numericalDoubleVectorizedMidpoint
    df2.at[i, 'Error Vec Midpoint'] = errorDoubleVectorizedMidpoint
    df2.at[i, 'Waktu Vec Midpoint'] = waktuDoubleVectorizedMipoint

    df2.at[i, 'Hasil Vec Trapezoidal'] = numericalDoubleVectorizedTrapezoid
    df2.at[i, 'Error Vec Trapezoidal'] = errorDoubleVectorizedTrapezoid
    df2.at[i, 'Waktu Vec Trapezoidal'] = waktuDoubleVectorizedTrapezoid

    # MEMASUKKAN ITEM INTEGRAL LEVEL 3 KE DATA FRAME PANDAS #
    df3.at[i, 'Jumlah N'] = nn
    df3.at[i, 'Hasil Exact'] = lipat3

    df3.at[i, 'Hasil Midpoint'] = numericalTriple
    df3.at[i, 'Error Midpoint'] = errorTriple
    df3.at[i, 'Waktu Midpoint'] = waktuTriple

    df3.at[i, 'Hasil Trapezoidal'] = numericalTripleTrapezoid
    df3.at[i, 'Error Trapezoidal'] = errorTripleTrapezoid
    df3.at[i, 'Waktu Trapezoidal'] = waktuTripleTrapezoid
    
    df3.at[i, 'Hasil Vec Midpoint'] = numericalTripleVectorizedMidpoint
    df3.at[i, 'Error Vec Midpoint'] = errorTripleVectorizedMidpoint
    df3.at[i, 'Waktu Vec Midpoint'] = waktuTripleVectorizedMipoint

    df3.at[i, 'Hasil Vec Trapezoidal'] = numericalTripleVectorizedTrapezoid
    df3.at[i, 'Error Vec Trapezoidal'] = errorTripleVectorizedTrapezoid
    df3.at[i, 'Waktu Vec Trapezoidal'] = waktuTripleVectorizedTrapezoid

    # MEMASUKKAN ITEM MONTE CARLO KE DATA FRAME PANDAS #
    df4.at[i, 'Jumlah N'] = nn
    df4.at[i, 'Hasil Exact'] = lipat2
    
    df4.at[i, 'Hasil Monte Carlo'] = numericalMonteCarlo
    df4.at[i, 'Error Monte Carlo'] = errorMonteCarlo
    df4.at[i, 'Waktu Monte Carlo'] = waktuMonteCarlo

    # DISPLAY HASIL INTEGRAL LEVEL 1
    print('\n\n============== INTEGRAL LIPAT 1 ==============\n\n')
    print('\nSingle Midpoint Integration :\t\t\t\t', numericalSingle)
    print('\tWaktu Komputasi Single Midpoint :\t\t', waktuSingle)
    print('\tError Single Midpoint Integration :\t\t', abs(lipat1 - numericalSingle)/lipat1)

    print('\nSingle Trapezoid Integration :\t\t\t\t', numericalSingleTrapezoid)
    print('\tWaktu Komputasi Single Trapezoid :\t\t', waktuSingleTrapezoid)
    print('\tError Single Trapezoid :\t\t\t', abs(lipat1 - numericalSingleTrapezoid)/lipat1)

    print('\nSingle Vectorized Midpoint :\t\t\t\t', numericalSingleVectorizedMidpoint)
    print('\tWaktu Komputasi Single Vectorized Midpoint :\t', waktuSingleVectorizedMipoint)
    print('\tError Single Vectorized Midpoint :\t\t', abs(lipat1 - numericalSingleVectorizedMidpoint)/lipat1)

    print('\nSingle Vectorized Midpoint :\t\t\t\t', numericalSingleVectorizedTrapezoid)
    print('\tWaktu Komputasi Single Vectorized Trapezoid :\t', waktuSingleVectorizedTrapezoid)
    print('\tError Single Vectorized Trapezoid :\t\t', abs(lipat1 - numericalSingleVectorizedTrapezoid)/lipat1)

    # DISPLAY HASIL INTEGRAL LEVEL 2 #
    print('\n\n============== INTEGRAL LIPAT 2 ==============\n\n')
    print('\nDouble Midpoint Integration :\t\t\t\t', numericalDouble)
    print('\tWaktu Komputasi Double Midpoint :\t\t', waktuDouble)
    print('\tError Double Midpoint Integration :\t\t', abs(lipat2 - numericalDouble)/lipat2)

    print('\nDouble Trapezoid Integration :\t\t\t\t', numericalDoubleTrapezoid)
    print('\tWaktu Komputasi Double Trapezoid :\t\t', waktuDoubleTrapezoid)
    print('\tError Single Trapezoid :\t\t\t', abs(lipat2 - numericalDoubleTrapezoid)/lipat2)

    print('\nDouble Vectorized Midpoint :\t\t\t\t', numericalDoubleVectorizedMidpoint)
    print('\tWaktu Komputasi Double Vectorized Midpoint :\t', waktuDoubleVectorizedMipoint)
    print('\tError Double Vectorized Midpoint :\t\t', abs(lipat2 - numericalDoubleVectorizedMidpoint)/lipat2)

    print('\nDouble Vectorized Midpoint :\t\t\t\t', numericalDoubleVectorizedTrapezoid)
    print('\tWaktu Komputasi Double Vectorized Trapezoid\t', waktuDoubleVectorizedTrapezoid)
    print('\tError Double Vectorized Trapezoid :\t\t', abs(lipat2 - numericalDoubleVectorizedTrapezoid)/lipat2)

    # DISPLAY HASIL INTEGRAL LEVEL 3 #
    print('\n\n============== INTEGRAL LIPAT 3 ==============\n\n')
    print('\nTriple Midpoint Integration :\t\t\t\t', numericalTriple)
    print('\tWaktu Komputasi Triple Midpoint :\t\t', waktuTriple)
    print('\tError Triple Midpoint Integration :\t\t', abs(lipat3 - numericalTriple)/lipat3)

    print('\nTriple Trapezoid Integration :\t\t\t\t', numericalTripleTrapezoid)
    print('\tWaktu Komputasi Triple Trapezoid :\t\t', waktuTripleTrapezoid)
    print('\tError Single Trapezoid :\t\t\t', abs(lipat3 - numericalTripleTrapezoid)/lipat3)

    print('\nTriple Vectorized Midpoint :\t\t\t\t', numericalTripleVectorizedMidpoint)
    print('\tWaktu Komputasi Triple Vectorized Midpoint :\t', waktuTripleVectorizedMipoint)
    print('\tError Triple Vectorized Midpoint :\t\t', abs(lipat3 - numericalTripleVectorizedMidpoint)/lipat3)

    print('\nTriple Vectorized Midpoint :\t\t\t\t', numericalTripleVectorizedTrapezoid)
    print('\tWaktu Komputasi Triple Vectorized Trapezoid :\t', waktuTripleVectorizedTrapezoid)
    print('\tError Triple Vectorized Trapezoid :\t\t', abs(lipat3 - numericalTripleVectorizedTrapezoid)/lipat3)

    # DISPLAY HASIL MONTE CARLO #
    print('\n\n============== MONTE CARLO ==============\n\n')
    print('\nHasil Monte Carlo :\t\t\t\t\t', numericalMonteCarlo)
    print('\tWaktu Komputasi Monte Carlo :\t\t\t', waktuMonteCarlo)
    print('\tError Metode Monte Carlo :\t\t\t', abs(lipat2 - numericalMonteCarlo)/lipat2)

# SAVE EXCEL VIA PANDAS #
writter = pd.ExcelWriter('Tugas 6.xlsx')

df1.to_excel(writter, sheet_name='Integral Single', index=False, na_rep='NaN')
for columns in df1:
    columns_width = max(df1[columns].astype(str).map(len).max(), len(columns))
    col_idx = df1.columns.get_loc(columns)
    writter.sheets['Integral Single'].set_column(col_idx, col_idx, 50)

df2.to_excel(writter, sheet_name='Integral Double', index=False, na_rep='NaN')
for columns in df2:
    columns_width = max(df2[columns].astype(str).map(len).max(), len(columns))
    col_idx = df2.columns.get_loc(columns)
    writter.sheets['Integral Double'].set_column(col_idx, col_idx, 50)

df3.to_excel(writter, sheet_name='Integral Triple', index=False, na_rep='NaN')
for columns in df3:
    columns_width = max(df3[columns].astype(str).map(len).max(), len(columns))
    col_idx = df3.columns.get_loc(columns)
    writter.sheets['Integral Triple'].set_column(col_idx, col_idx, 50)

df4.to_excel(writter, sheet_name='Monte Carlo', index=False, na_rep='NaN')
for columns in df4:
    columns_width = max(df4[columns].astype(str).map(len).max(), len(columns))
    col_idx = df4.columns.get_loc(columns)
    writter.sheets['Monte Carlo'].set_column(col_idx, col_idx, 50)
    
writter.save()

# MENAMPILKAN DATA FRAME PANDAS #
print('\n\n===== Data Frame Integral Level 1 =====\n')
print(df1)

print('\n\n===== Data Frame Integral Level 2 =====\n')
print(df2)

print('\n\n===== Data Frame Integral Level 3 =====\n')
print(df3)

print('\n\n===== Data Frame Monte Carlo =====\n')
print(df4)

# PLOTTING GRAFIK ERROR #
plt.title('Grafik Perbandingan Error Integral Level 1')
plt.plot(df1['Jumlah N'], df1['Error Midpoint'], 's-', label='Metode Midpoint')
plt.plot(df1['Jumlah N'], df1['Error Trapezoidal'], 'p--', label='Metode Trapezoidal')
plt.plot(df1['Jumlah N'], df1['Error Vec Midpoint'], 'h-.', label='Metode Vec Trapezoidal')
plt.plot(df1['Jumlah N'], df1['Error Vec Trapezoidal'], '8:', label='Metode Vec Trapezoidal')
plt.xlabel('Jumlah N')
plt.ylabel('Error')
plt.legend(shadow=True, fancybox=True)
plt.grid(True)
plt.show()

plt.title('Grafik Perbandingan Error Integral Level 2')
plt.plot(df2['Jumlah N'], df2['Error Midpoint'], 's-', label='Metode Midpoint')
plt.plot(df2['Jumlah N'], df2['Error Trapezoidal'], 'p--', label='Metode Trapezoidal')
plt.plot(df2['Jumlah N'], df2['Error Vec Midpoint'], 'h-.', label='Metode Vec Trapezoidal')
plt.plot(df2['Jumlah N'], df2['Error Vec Trapezoidal'], '8:', label='Metode Vec Trapezoidal')
plt.xlabel('Jumlah N')
plt.ylabel('Error')
plt.legend(shadow=True, fancybox=True)
plt.grid(True)
plt.show()

plt.title('Grafik Perbandingan Error Integral Level 3')
plt.plot(df3['Jumlah N'], df3['Error Midpoint'], 's-', label='Metode Midpoint')
plt.plot(df3['Jumlah N'], df3['Error Trapezoidal'], 'p--', label='Metode Trapezoidal')
plt.plot(df3['Jumlah N'], df3['Error Vec Midpoint'], 'h-.', label='Metode Vec Trapezoidal')
plt.plot(df3['Jumlah N'], df3['Error Vec Trapezoidal'], '8:', label='Metode Vec Trapezoidal')
plt.xlabel('Jumlah N')
plt.ylabel('Error')
plt.legend(shadow=True, fancybox=True)
plt.grid(True)
plt.show()

plt.title('Grafik Perbandingan Error Monte Carlo')
plt.plot(df4['Jumlah N'], df4['Error Monte Carlo'], 's:', label='Metode Monte Carlo')
plt.xlabel('Jumlah N')
plt.ylabel('Error')
plt.legend(shadow=True, fancybox=True)
plt.grid(True)
plt.show()

# PLOTTING GRAFIK WAKTU KOMPUTASI #
plt.title('Grafik Perbandingan Waktu Komputasi Integral Level 1')
plt.plot(df1['Jumlah N'], df1['Waktu Midpoint'], 's-', label='Metode Midpoint')
plt.plot(df1['Jumlah N'], df1['Waktu Trapezoidal'], 'p--', label='Metode Trapezoidal')
plt.plot(df1['Jumlah N'], df1['Waktu Vec Midpoint'], 'h-.', label='Metode Vec Trapezoidal')
plt.plot(df1['Jumlah N'], df1['Waktu Vec Trapezoidal'], '8:', label='Metode Vec Trapezoidal')
plt.xlabel('Jumlah N')
plt.ylabel('Waktu Komputasi')
plt.legend(shadow=True, fancybox=True)
plt.grid(True)
plt.show()

plt.title('Grafik Perbandingan Waktu Komputasi Integral Level 2')
plt.plot(df2['Jumlah N'], df2['Waktu Midpoint'], 's-', label='Metode Midpoint')
plt.plot(df2['Jumlah N'], df2['Waktu Trapezoidal'], 'p--', label='Metode Trapezoidal')
plt.plot(df2['Jumlah N'], df2['Waktu Vec Midpoint'], 'h-.', label='Metode Vec Trapezoidal')
plt.plot(df2['Jumlah N'], df2['Waktu Vec Trapezoidal'], '8:', label='Metode Vec Trapezoidal')
plt.xlabel('Jumlah N')
plt.ylabel('Waktu Komputasi')
plt.legend(shadow=True, fancybox=True)
plt.grid(True)
plt.show()

plt.title('Grafik Perbandingan Waktu Komputasi Integral Level 3')
plt.plot(df3['Jumlah N'], df3['Waktu Midpoint'], 's-', label='Metode Midpoint')
plt.plot(df3['Jumlah N'], df3['Waktu Trapezoidal'], 'p--', label='Metode Trapezoidal')
plt.plot(df3['Jumlah N'], df3['Waktu Vec Midpoint'], 'h-.', label='Metode Vec Trapezoidal')
plt.plot(df3['Jumlah N'], df3['Waktu Vec Trapezoidal'], '8:', label='Metode Vec Trapezoidal')
plt.xlabel('Jumlah N')
plt.ylabel('Waktu Komputasi')
plt.legend(shadow=True, fancybox=True)
plt.grid(True)
plt.show()

plt.title('Grafik Perbandingan Waktu Komputasi Monte Carlo')
plt.plot(df4['Jumlah N'], df4['Waktu Monte Carlo'], 's:', label='Metode Monte Carlo')
plt.xlabel('Jumlah N')
plt.ylabel('Waktu Komputasi')
plt.legend(shadow=True, fancybox=True)
plt.grid(True)
plt.show()
