my_ev = int(input("Kérem az évszámot!: "))


def szokoev(ev):
    if ev % 400 == 0:
        print("Szökőév")
    elif ev % 4 == 0 and ev % 100 != 0:
        print("Szökőév")
    else:
        print("Nem szökőév")


szokoev(my_ev)
