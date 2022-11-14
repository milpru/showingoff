print("podaj wymiary matrycy n i m: ")
x = input("pamiętaj by oddzielić liczby spacją :) ")
list = x.split(" ")
n = int(list[0])
m = int(list[1])



from random import seed 
from random import randint
seed(123)

print("wersja podstawowa: ")

#tworzenie podstawowej matrycy a
#wymiary matrycy mozna zmienic dowolnie przez n i m
a = []
for i in range(n):
    a.append([0] * m)
    for j in range(m):
        a[i][j] = randint(0, 20)
    print(a[i])

print(" wersja transponowana: ")
 
#tworzenie transponowanej matrycy at 
at=[]
for i in range(len(a[0])):
    at.append([0]*len(a))
    for j in range(len(a)):
        at[i][j] = a[j][i]
    print(at[i])
