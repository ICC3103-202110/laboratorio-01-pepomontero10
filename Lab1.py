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
    for i in range(b+1):
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
    for i in range(b+1):
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

def deck_print(a):
    for i in a:
    print(i)

def Coordinates(coordinate_1,coordinate_2):
    x = 2
    while x != 0:
        coordinate_1[x-1]= int(coordinate_1[x-1])
        coordinate_2[x-1]= int(coordinate_2[x-1])
        x -= 1
def Verification (coordinate_1,coordinate_2):   
    if coordinate_1[0] <= len(game_deck)-1 and coordinate_1[1] < len(game_deck[0]) and coordinate_2[0] <= len(game_deck)-1 and coordinate_2[1] < len(game_deck[0]):
        return True

done = 0
start = 0
player_1 = 0
player_2 = 0
while done != 1:
    print("Player 1, First Coordinates (row,column)")
    coordinate_1 = input()
    coordinate_1 = coordinate_1.split(",")
    print("Player 1, Second Coordinates (row,column)")
    coordinate_2 = input()
    coordinate_2 = coordinate_2.split(",")
    Coordinates(coordinate_1,coordinate_2)
    if Verification(coordinate_1,coordinate_2) == True:
        print("hola")


    else:
        print("You lost your turn, because your coordinates are invalid")


    print("Player 2, First Coordinates (row,column)")
    coordinate_1 = input()
    coordinate_1 = coordinate_1.split(",")
    print("Player 2, Second Coordinates (row,column)")
    coordinate_2 = input()
    coordinate_2 = coordinate_2.split(",")
    Coordinates(coordinate_1,coordinate_2)

    if game_deck == real_deck:
        print("Winner!!")
        done += 1