import random

print("🎯 Vítej ve hře Hádej číslo!")
print("Myslím si číslo od 1 do 100.")
print("Zkus ho uhodnout!\n")

tajne_cislo = random.randint(1, 100)
pokusy = 0

while True:
    tip = input("Tvůj tip: ")
    if not tip.isdigit():
        print("Zadej prosím celé číslo.")
        continue

    tip = int(tip)
    pokusy += 1

    if tip < tajne_cislo:
        print("Je to víc!")
    elif tip > tajne_cislo:
        print("Je to míň!")
    else:
        print(f"✅ Uhodl jsi číslo {tajne_cislo} po {pokusy} pokusech!")
        break

print("\nDíky za hraní! 🧩")