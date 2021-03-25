ch=input("Donner une chaîne")
nb=0
for i in ch :
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i== 'y':
        nb = nb + 1

print("Le nombre de voyelles dans la chaine ",ch," est ",nb)
