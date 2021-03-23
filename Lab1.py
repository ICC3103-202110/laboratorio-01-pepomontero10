import random

print("Cuantas cartas quieres?")
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

random.shuffle(maso)

real_maso = []
b = int((2 * int(cartas_1))**(0.5))
c = int(b) +1
n = 0
print(len(maso))
while c != 0:
    row = []
    for i in range(b):
        row.append(maso[n])
        n += 1
        if n == len(maso)-1 :
            c -= 1
    real_maso.append(row)
    c -= 1

for i in real_maso:
    print(i)




