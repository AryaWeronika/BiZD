import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli, binom, poisson

wartosci = np.array([1, 2, 3, 4, 5, 6])
prawdopodobienstwo = np.array([1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

proby_bernoulli = bernoulli.rvs(p=prawdopodobienstwo[0], size=100)

proby_dwumianowe = binom.rvs(n=len(wartosci)-1, p=prawdopodobienstwo[1:], size=(100, len(wartosci)-1))

proby_poisson = poisson.rvs(mu=np.sum(wartosci * prawdopodobienstwo), size=100)

def rysuj_wykres_rozkładu(wartosci, prawdopodobienstwo, tytul, os_x, os_y):
    plt.bar(wartosci, prawdopodobienstwo, align='center', alpha=0.7)
    plt.title(tytul)
    plt.xlabel(os_x)
    plt.ylabel(os_y)
    plt.show()

rysuj_wykres_rozkładu(wartosci, prawdopodobienstwo, "Rozkład Bernoulliego", "Wartość", "Prawdopodobieństwo")

wartosci_dwumianowe = np.arange(0, len(wartosci)-1)

rysuj_wykres_rozkładu(wartosci_dwumianowe, prawdopodobienstwo[1:], "Rozkład Dwumianowy", "Liczba sukcesów", "Prawdopodobieństwo")

wartosci_poisson = np.arange(0, np.max(wartosci) * 2)
prawdopodobienstwo_poisson = poisson.pmf(wartosci_poisson, mu=np.sum(wartosci * prawdopodobienstwo))

rysuj_wykres_rozkładu(wartosci_poisson, prawdopodobienstwo_poisson, "Rozkład Poissona", "Liczba zdarzeń", "Prawdopodobieństwo")