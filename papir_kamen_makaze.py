import random
dogadjaji = ["papir", "kamen", "makaze"]
ja_score = 0
kompa_score = 0
while True:
    ja = input("Unesi papir kamen ili makaze:  ").lower()
    if ja not in dogadjaji:
        print("Niste dobro uneli. Unesite ponovo.")
        continue
    racunar = random.randint(0,2)
    izbor_kompjutera = dogadjaji[racunar]
    print("Kompjuter je odabrao:",izbor_kompjutera)
    if ja == izbor_kompjutera:
        print("Nereseno.")
        continue
    if ja == "papir" and izbor_kompjutera == "kamen":
        ja_score += 1
    elif ja == "kamen" and izbor_kompjutera == "makaze":
        ja_score += 1
    elif ja == "makaze" and izbor_kompjutera == "papir":
        ja_score += 1
    else:
        kompa_score += 1
    if ja_score == 3 or kompa_score == 3:
        break
if ja_score>kompa_score:
    print("CESTITAM, pobedili ste rezultatom {} naprema {}.".format(ja_score,kompa_score))
else:
     print("IZGUBILI STE, kompjuter je pobedio rezultatom {} naprema {}.".format(kompa_score,ja_score))