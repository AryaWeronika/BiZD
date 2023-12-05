import numpy as np
from scipy.stats import bernoulli, binom, poisson

wartosci = np.array([1, 2, 3, 4, 5, 6])
prawdopodobienstwo = np.array([1/6, 1/6, 1/6, 1/6, 1/6, 1/6])


srednia = np.sum(wartosci * prawdopodobienstwo)
wariancja = np.sum((wartosci - srednia)**2 * prawdopodobienstwo)
odchylenie_standardowe = np.sqrt(wariancja)

print(f"Średnia: {srednia}")
print(f"Wariancja: {wariancja}")
print(f"Odchylenie standardowe: {odchylenie_standardowe}")

proby_bernoulli = bernoulli.rvs(p=prawdopodobienstwo[0], size=100)

proby_dwumianowe = binom.rvs(n=len(wartosci)-1, p=prawdopodobienstwo[1:], size=(100, len(wartosci)-1))

proby_poisson = poisson.rvs(mu=srednia, size=100)


print("\nPróby dla rozkładu Bernoulliego:")
print(proby_bernoulli)

print("\nPróby dla rozkładu dwumianowego:")
print(proby_dwumianowe)

print("\nPróby dla rozkładu Poissona:")
print(proby_poisson)