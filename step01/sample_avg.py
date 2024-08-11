#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x_means = []
N = 1 # 先ずはサンプルサイズが１の場合を考える。
# N = 2
# N = 4
# N = 10
# N = 1000

for _ in range(10000):
    xs = []
    for n in range(N):
        x = np.random.rand() # 一様分布からのサンプル
        xs.append(x)
    mean = np.mean(xs)
    x_means.append(mean)

# グラフの描画
plt.hist(x_means, bins='auto', density=True)
plt.title(f'N={N}')
plt.xlabel('x')
plt.ylabel('Probability Density') # Y軸は「確率密度」
plt.xlim(-0.05, 1.05)
plt.ylim(0, 5)
plt.show()



