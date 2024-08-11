#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x_sums = []
N = 5

for _ in range(10000):
    xs = []
    for n in range(N):
        x = np.random.rand() # 一様分布からの乱数
        xs.append(x) # [x^(1), x^(2), ..., x^(N)]_k (1 <= k <= 10000)を作成

    t = np.sum(xs) # x^(1)_k + x^(2)_k + ... + x^(N)_k 和を求める
    x_sums.append(t) # サンプル和の分布を求めるためにリストに追加する

# 正規分布
def normal(x, mu=0, sigma=1):
    y = 1 / (np.sqrt(2 * np.pi) * sigma) * np.exp(-(x - mu)**2 / (2 * sigma**2))
    return y

x_norm = np.linspace(-5, 5, 1000)
mu = N / 2
sigma = np.sqrt(N / 12)
y_norm = normal(x_norm, mu, sigma)

# グラフの描画
plt.hist(x_sums, bins='auto', density=True)
plt.plot(x_norm, y_norm)
plt.title(f'N={N}')
plt.xlim(-1, 6) # X軸の範囲を-1 ~ 6に設定
plt.show()




