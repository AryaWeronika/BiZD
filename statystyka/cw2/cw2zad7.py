import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

srednia1 = 1
odchylenie1 = 2

srednia2 = -1
odchylenie2 = 0.5

dane = np.random.normal(srednia1, odchylenie1, 1000)

x = np.linspace(-5, 5, 1000)

plt.hist(dane, bins=30, density=True, alpha=0.7, color='blue', label='Rozkład normalny (1, 2)')
plt.plot(x, norm.pdf(x), color='red', label='Rozkład standardowy')
plt.plot(x, norm.pdf(x, loc=srednia2, scale=odchylenie2), color='green', linestyle='dashed', label='Rozkład normalny (-1, 0.5)')

plt.title('Histogram i wykresy gęstości')
plt.xlabel('Wartość')
plt.ylabel('Prawdopodobieństwo')
plt.legend()

plt.show()