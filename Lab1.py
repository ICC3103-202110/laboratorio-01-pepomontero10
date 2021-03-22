import random

print("Cuantas cartas quieres, jugador 1?")
cartas_1 = int(input())

a = int(cartas_1)

jugador_1 = []

while a != 0:
    x = random.randint(1,int(cartas_1))
    if x in jugador_1:
        jugador_1.remove(x)
        a += 1
    jugador_1.append(x)
    a -= 1
maso = []
for i in jugador_1:
    maso.append(i)
    maso.append(i)
print(jugador_1)
print(maso)




