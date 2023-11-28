import pandas as pd
import numpy as np
from scipy import stats


df = pd.read_csv("MDR_RR_TB_burden_estimates_2023-11-28.csv")


selected_column = df['e_rr_pct_new']


mean_value = np.mean(selected_column)
median_value = np.median(selected_column)
mode_value = stats.mode(selected_column)


print(f"Średnia: {mean_value}")
print(f"Mediana: {median_value}")
print(f"Moda: {mode_value.mode} (counts: {mode_value.count})")