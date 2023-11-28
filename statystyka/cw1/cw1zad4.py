import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("brain_size.csv", sep=";", index_col=0)

viq_mean = df['VIQ'].mean()
print(f"Średnia dla kolumny VIQ: {viq_mean}")

gender_counts = df['Gender'].value_counts()
print(f"Liczba kobiet: {gender_counts['Female']}")
print(f"Liczba mężczyzn: {gender_counts['Male']}")


df[['VIQ', 'PIQ', 'FSIQ']].hist()
plt.suptitle('Histogramy dla VIQ, PIQ, FSIQ')
plt.show()

df[df['Gender'] == 'Female'][['VIQ', 'PIQ', 'FSIQ']].hist()
plt.suptitle('Histogramy dla VIQ, PIQ, FSIQ tylko dla kobiet')
plt.show()