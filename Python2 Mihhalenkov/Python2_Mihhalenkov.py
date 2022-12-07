from math import * #kuidas see oli (import * from math) поменял местами.

print("Ruudu karakteristikud")
a=float(input('Sisesta ruudu külje pikkus => ')) #В начало добавил float
S=a**2
print("Ruudu pindala", round(S,1)) #round
P=4*a
print("Ruudu ümbermõõt", round(P,1)) #Заменил '' на ", round
di=a*sqrt(2) #убрал math и добавил t
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud") #Убрал лишнюю скобку
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) #Добавил float
c=float(input("Sisesta ristküliku 2. külje pikkus => ")) #Добавил float
S=b*c
print("Ristküliku pindala", round(S,1)) #Как было print(Ristküliku pindala', S) поменял знак ', round
P=2*(b+c) #поменял с и знак *
print("Ristküliku ümbermõõt", round(P,1)) #round
di=sqrt(b*2+c*2) #стираем math
print("Ristküliku diagonaal", round(di,1)) #Lisas скобку и ", round
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => ")) #Вместо ' поставил " и убрал лишнюю скобку)
d=2*r
print("Ringi läbimõõt", round(d,1)) #Вместо пробела и d Lisas " и скобку поставить , round
S=pi*r**2 #В квадрате
print("Ringi pindala", round(S,2)) #round
C=2*pi*r #добавил 2
print("Ringjoone pikkus", round(C,2)) #round