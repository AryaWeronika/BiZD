import numpy as np
from scipy.stats import binom

n = 20
p = 0.4

k_values = np.arange(0, 21)

rozkład_dwumianowy = binom.pmf(k_values, n, p)

for k, prawdopodobienstwo in zip(k_values, rozkład_dwumianowy):
    print(f"P({k}) = {prawdopodobienstwo}")

suma_prawdopodobienstw = np.sum(rozkład_dwumianowy)
print(f"\nSuma prawdopodobieństw: {suma_prawdopodobienstw}")

epsilon = 1e-10
if np.abs(suma_prawdopodobienstw - 1) < epsilon:
    print("Suma prawdopodobieństw jest równa 1.")
else:
    print("Suma prawdopodobieństw nie jest równa 1.")