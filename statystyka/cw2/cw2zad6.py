import numpy as np
from scipy.stats import describe

srednia_teoretyczna = 0
odchylenie_standardowe_teoretyczne = 2

dane = np.random.normal(srednia_teoretyczna, odchylenie_standardowe_teoretyczne, 100)

statystyki_opisowe = describe(dane)

print("Statystyki opisowe dla 100 danych:")
print(statystyki_opisowe)

print("\nPorównanie z wartościami teoretycznymi:")
print(f"Średnia teoretyczna: {srednia_teoretyczna}")
print(f"Odchylenie standardowe teoretyczne: {odchylenie_standardowe_teoretyczne}")

rozmiary_probek = [100, 1000, 10000]

for rozmiar_probki in rozmiary_probek:
    dane_probka = np.random.normal(srednia_teoretyczna, odchylenie_standardowe_teoretyczne, rozmiar_probki)
    statystyki_probka = describe(dane_probka)

    print(f"\nStatystyki opisowe dla {rozmiar_probki} danych:")
    print(statystyki_probka)

    print("\nPorównanie z wartościami teoretycznymi:")
    print(f"Średnia teoretyczna: {srednia_teoretyczna}")
    print(f"Odchylenie standardowe teoretyczne: {odchylenie_standardowe_teoretyczne}")