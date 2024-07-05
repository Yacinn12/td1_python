# : Créer un programme qui affiche les 10 premiers nombres pairs en utilisant
#une boucle For .

print("Les dix premiers nombres pairs : ")
i = 0
for i in range (0,20,2):
    print(i)
    
# Ensuite, utiliser une boucle while pour afficher les 10 premiers nombres
#impairs.
print("Les dix premiers nombres impairs :")
i = 1
n = 20

while i <= n:
    if i % 2 != 0:
        print(i)
    i += 1
    
#Créer un programme qui va demander un nombre à l’utilisateur, 
# va s’assurer que c’est bien un nombre qui a été inséré et 
# enfin va afficher les nombres entier entre le 1 et le nombre 
# fourni par l’utilisateur.
i = 1
nombre_choisi = input("Veuillez entrer un nombre : ")
while not nombre_choisi.isdigit():
    print("Entrez uniquement des nombres !!!!")
    nombre_choisi = input("Veuillez entrer un nombre : ") 

nombre_choisi = int(nombre_choisi)
for n in range ( 1,nombre_choisi):
    print(n) 