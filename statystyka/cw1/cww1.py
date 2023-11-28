import requests

url = "https://extranet.who.int/tme/generateCSV.asp?ds=mdr_estimates"
response = requests.get(url)

with open("MDR_RR_TB_burden_estimates_2023-11-28.csv", "wb") as f:
    f.write(response.content)
import pandas as pd


df = pd.read_csv("MDR_RR_TB_burden_estimates_2023-11-28.csv")


selected_column = df['country']


basic_statistics = selected_column.describe()


print(basic_statistics)