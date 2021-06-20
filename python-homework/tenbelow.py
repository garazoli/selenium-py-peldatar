x = 0

while True:
    my_x = int(input("Kérem a következő számot: "))
    x = x + my_x
    if my_x >= 10:
        x = x-my_x
        break

print("A beolvasott egyjegyű számok összege: " + str(x))
