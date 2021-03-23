import random
print("How many card do you want?")
cards_1 = int(input())
a = int(cards_1)
player_1 = []

while a != 0:
    x = random.randint(1,int(cards_1))
    if x in player_1:
        player_1.remove(x)
        a += 1
    player_1.append(x)
    a -= 1
deck = []
for i in player_1:
    deck.append(i)
    deck.append(i)

random.shuffle(deck)
#matriz
real_deck = []
b = int((2 * int(cards_1))**(0.5))
c = int(b)+1
n = 0
while c != 0:
    row = []
    for i in range(b):
        if n >= (int(cards_1)*2):
            break
        row.append(deck[n])
        n += 1
    real_deck.append(row)
    c -= 1

if len(row) == 0:
    real_deck.pop()
    
game_deck = []
b = int((2 * int(cards_1))**(0.5))
c = int(b)+1
n = 0
while c != 0:
    row = []
    for i in range(b):
        if n >= (int(cards_1)*2):
            break
        row.append("*")
        n += 1
    game_deck.append(row)
    c -= 1

if len(row) == 0:
    game_deck.pop()

for i in real_deck:
    print(i)

print ("") 

for i in game_deck:
    print(i)

done = 0

while done != 1:
    print("hola")

    if game_deck == real_deck:
        print("Winner!!")
        done += 1
