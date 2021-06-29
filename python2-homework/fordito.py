my_list = []

while True:
    my_x = int(input('Kérem a következő számot!: '))
    my_list.append(my_x)
    if my_x == 0:
        break
print(my_list[::-1])
