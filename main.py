import numpy as np
import matplotlib.pyplot as plt

#plt.interactive(False)
g = 9.80665 # 重力加速度(m/s^2)
k = 0.1  # 空気抵抗係数(kg/m)
m = 10.0  # ボール重さ(kg)

def f(v):  # 関数の定義
    return (m * g - k * v**2) / m
    #return g

def rungekutta(dt,v):
    k1 = dt * f(v)
    k2 = dt * f(v + 0.5 * k1)
    k3 = dt * f(v + 0.5 * k2)
    k4 = dt * f(v + k3)
    v = v + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return v

varray = [0.0]  # 速度のtrajectory配列
xarray = [1000.0]  # 位置の配列
tarray = [0.0]  # 時間発展配列

v = varray[0]  # 初期速度
x = xarray[0]  # 初期位置
t = tarray[0]  # 初期時間
dt = 0.01  # ルンゲクッタ法の刻み幅

# ルンゲクッタ法のメイン計算
while x >= 0.0e0:
    v=rungekutta(dt,v)
    x = x - v * dt
    t = t + dt
    varray = np.append(varray, v)
    xarray = np.append(xarray, x)
    tarray = np.append(tarray, t)

# グラフ描写
plt.plot(tarray, varray)
plt.plot(tarray, xarray)
plt.show()
