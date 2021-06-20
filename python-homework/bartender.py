kor = input("Kérem az életkorát: ")
ital = input("Mit iszik?")
ital_1 = "kóla"
ital_2 = "sör"

if int(kor) < 18 and ital == ital_2:
    print("Sajnos nem szogálhatom ki.")
elif int(kor) < 60 and ital == ital_1:
    print("Parancsoljon, a kólája!")
elif int(kor) >= 60 and ital == ital_1:
    print("A koffein megemelheti a vérnyomását!")
elif int(kor) >= 18 and ital == ital_2:
    print("Parancsoljon, a söre!")
else:
    print("Csak sört és kólát tudunk adni!")
