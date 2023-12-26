import numpy as np
import pandas as pd
from scipy.stats import ttest_1samp, ttest_ind, levene

#Sprawdzić która zmienna w pliku napoje.csv wykazuje normalność
mean = 2
std_dev = 30
sample_size = 200
random_sample = np.random.normal(mean, std_dev, sample_size)

# Badanie hipotezy dla rozkładu normalnego
hypothesis_mean = 2.5
t_stat, p_value = ttest_1samp(random_sample, hypothesis_mean)
print(f"T-statistic: {t_stat}, p-value: {p_value}")

df = pd.read_csv('napoje.csv', delimiter=';')
df.columns = df.columns.str.strip()
print("Column names:", df.columns)

# Weryfikacja hipotez dotyczących średnich spożycia
means_to_test = {'piwo_lech': 60500, 'cola': 222000, 'piwo_regionalne': 43500}
for var, hypo_mean in means_to_test.items():
    try:
        t_stat, p_value = ttest_1samp(df[var], hypo_mean)
        print(f"{var}: T-statistic: {t_stat}, p-value: {p_value}")
    except KeyError:
        print(f"{var} not found in DataFrame.")

# Zbadanie równości średnich dla par okocim – lech, fanta – regionalne oraz cola – pepsi.
pairs_to_test = [('okocim', 'lech'), ('fanta', 'regionalne'), ('cola', 'pepsi')]
for pair in pairs_to_test:
    try:
        t_stat, p_value = ttest_ind(df[pair[0]], df[pair[1]], equal_var=False)
        print(f"{pair}: T-statistic: {t_stat}, p-value: {p_value}")
    except KeyError:
        print(f"At least one variable in {pair} not found in DataFrame.")

# Zbadanie równości wariancji pomiędzy okocim – lech, żywiec – fanta oraz regionalne – cola
var_pairs_to_test = [('okocim', 'lech'), ('żywiec', 'fanta'), ('regionalne', 'cola')]
for var_pair in var_pairs_to_test:
    try:
        stat, p_value = levene(df[var_pair[0]].dropna(), df[var_pair[1]].dropna())
        print(f"{var_pair}: p-value for Levene's test: {p_value}")
    except KeyError:
        print(f"At least one variable in {var_pair} not found in DataFrame.")

# Zbadanie równości średnich dla lat 2001 i 2015 dla piw regionalnych
try:
    regional_beers_2001 = df.loc[df['rok'] == 2001, 'piwo_regionalne'].dropna()
    regional_beers_2015 = df.loc[df['rok'] == 2015, 'piwo_regionalne'].dropna()
    t_stat, p_value = ttest_ind(regional_beers_2001, regional_beers_2015, equal_var=False)
    print(f"Równość średnich dla lat 2001 i 2015 dla piw regionalnych: T-statistic: {t_stat}, p-value: {p_value}")
except KeyError:
    print("'piwo_regionalne' not found in DataFrame.")
df_after_ad = pd.read_csv('napoje_po_reklamie.csv', delimiter=';')


df_after_ad.columns = df_after_ad.columns.str.strip()
print("Column names (after ad):", df_after_ad.columns)
# Zbadanie równości średnich dla wartości z roku 2016 oraz dla wartości z pliku napoje_po_reklamie.csv oddzielnie dla coli, fanty i pepsi.
variables_to_test_after_ad = ['cola', 'fanta', 'pepsi']
for var in variables_to_test_after_ad:
    try:
        t_stat, p_value = ttest_ind(df[var], df_after_ad[var], equal_var=False)
        print(f"Równość średnich dla {var}: T-statistic: {t_stat}, p-value: {p_value}")
    except KeyError:
        print(f"{var} not found in both DataFrames.")