import numpy as np
from scipy.stats import bernoulli, binom, poisson, describe, kurtosis, skew

# Dane z tabeli
wartosci = np.array([1, 2, 3, 4, 5, 6])
prawdopodobienstwo = np.array([1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

# Podstawowe statystyki
srednia = np.sum(wartosci * prawdopodobienstwo)
wariancja = np.sum((wartosci - srednia)**2 * prawdopodobienstwo)
odchylenie_standardowe = np.sqrt(wariancja)

print(f"Średnia: {srednia}")
print(f"Wariancja: {wariancja}")
print(f"Odchylenie standardowe: {odchylenie_standardowe}")

# Generowanie prób dla rozkładu Bernoulliego
proby_bernoulli = bernoulli.rvs(p=prawdopodobienstwo[0], size=100)

# Generowanie prób dla rozkładu dwumianowego
proby_dwumianowe = binom.rvs(n=len(wartosci)-1, p=prawdopodobienstwo[1:], size=(100, len(wartosci)-1))

# Generowanie prób dla rozkładu Poissona
proby_poisson = poisson.rvs(mu=srednia, size=100)

# Statystyki podstawowe
def oblicz_statystyki(proby):
    opis = describe(proby)
    kurtoza = kurtosis(proby)
    skosnosc = skew(proby)

    print(f"\nStatystyki podstawowe:")
    print(f"Średnia: {opis.mean}")
    print(f"Wariancja: {opis.variance}")
    print(f"Kurtoza: {kurtoza}")
    print(f"Skośność: {skosnosc}")

# Wyświetlenie wyników
print("\nPróby dla rozkładu Bernoulliego:")
oblicz_statystyki(proby_bernoulli)

print("\nPróby dla rozkładu dwumianowego:")
oblicz_statystyki(proby_dwumianowe)

print("\nPróby dla rozkładu Poissona:")
oblicz_statystyki(proby_poisson)