import csv
import statistics


with open('Wzrost.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(map(float, next(reader)))

mean_value = statistics.mean(data)
median_value = statistics.median(data)
variance_value = statistics.variance(data)
stdev_value = statistics.stdev(data)


print(f"Średnia: {mean_value}")
print(f"Mediana: {median_value}")
print(f"Wariancja: {variance_value}")

print(f"Odchylenie standardowe: {stdev_value}")