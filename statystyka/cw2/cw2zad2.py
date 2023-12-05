import pandas as pd
import matplotlib.pyplot as plt
rs = pd.read_csv('iris.txt', sep = '\t', header = None)
typ = pd.read_csv('iris-type.txt', sep = '\t', header = None)
print(rs[4][0])
klasy = []
klasy2 = []
klasy3 = []
#print(klasy[4][0])
#ma 149 linii
def PrzydzKlasy(data):
    for d in range (0,149,1):
        if data[4][d] == 3:
            klasy.append(data[0][d])
            klasy.append(data[1][d])
            klasy.append(data[2][d])
            klasy.append(data[3][d])
        if data[4][d] == 2:
            klasy2.append(data[0][d])
            klasy2.append(data[1][d])
            klasy2.append(data[2][d])
            klasy2.append(data[3][d])
        if data[4][d] == 1:
            klasy3.append(data[0][d])
            klasy3.append(data[1][d])
            klasy3.append(data[2][d])
            klasy3.append(data[3][d])
#Na pierwszej przestrzeni osią x są wartości atrybutu 3-go próbek, a osią y są wartości atrybutu 4-tego (licząc od 1, nie od 0)
xs1 = []
ys1 = []
xs2 = []
ys2 = []
xs3 = []
def x1(data):
    for d in range (0,149,1):#3 atrybut
        xs1.append(data[2][d])
    for d in range (0,149,1):#4 atrybut
        ys1.append(data[3][d])
    for d in range (0,149,1):#2 atrybut
        xs2.append(data[1][d])
    for d in range (0,149,1):#1 atrybut
        xs3.append(data[0][d])

PrzydzKlasy(rs)
print(klasy)
x1(rs)
print(xs1)
print(ys1)
plt.subplot(2,2,1)
plt.plot(xs1,ys1,klasy, label = 'Virginica', color = 'blue')
plt.plot(xs1,ys1,klasy2, label = 'Versicolour', color = 'green')
plt.plot(xs1,ys1,klasy3, label = 'Setosa', color = 'orange')
plt.xlabel('3 atrybut')
plt.ylabel('4 atrybut')
plt.subplot(2,2,2)
plt.plot(xs2,ys1,klasy, label = 'Virginica', color = 'blue')
plt.plot(xs2,ys1, klasy2, label = 'Versicolour', color = 'green')
plt.plot(xs2,ys1, klasy3, label = 'Setosa', color = 'orange')
plt.xlabel('2 atrybut')
plt.ylabel('4 atrybut')
plt.subplot(2,2,3)
plt.plot(xs3,ys1,klasy,label = 'Virginica', color = 'blue')
plt.plot(xs3,ys1,klasy2, label = 'Versicolour', color = 'green')
plt.plot(xs3,ys1,klasy3, label = 'Setosa', color = 'orange')
plt.xlabel('1 atrybut')
plt.ylabel('4 atrybut')
plt.subplot(2,2,4)
plt.plot(xs2,xs1, klasy,label = 'Virginica', color = 'blue')
plt.plot(xs2,xs1, klasy2, label = 'Versicolour', color = 'green')
plt.plot(xs2,xs1, klasy3, label = 'Setosa', color = 'orange')
plt.xlabel('2 atrybut')
plt.ylabel('3 atrybut')
to = ['Virginica','Versicolour','Setosa']
plt.legend(to, loc='upper center', bbox_to_anchor=(1.5, -0.1), ncol=3)
plt.show()

