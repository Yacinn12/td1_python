# Créez une liste vide pour le panier
panier = []

# Fonction pour afficher le menu
def afficher_menu():
    print("""Choisissez parmi les 5 options suivantes:
                1- Ajouter un article dans le panier
                2- Supprimer un article du panier
                3- Afficher tous les articles
                4- Vider le panier
                5- Quitter""")
    


# Fonction pour ajouter un article au panier
def ajouter_article():
    article = input("Entrez le nom de l'article : ")
    prix = float(input("Entrez le prix de l'article : "))
    nouvel_article = {"name": article, "price": prix}
    panier.append(nouvel_article)
    print(f"{article} a été ajouté au panier.")

# Fonction pour supprimer un article du panier
def supprimer_article():
    article_supprime = input("Entrez le nom de l'article à supprimer : ")
    article_trouve = False
    for article in panier:
        if article["name"] == article_supprime:
            panier.remove(article)
            article_trouve = True
            print(f"{article_supprime} a été supprimé du panier.")
            
    if not article_trouve:
        print("Aucun article avec ce nom dans le panier.")

# Fonction pour afficher tous les articles du panier
def afficher_articles():
    for article in panier:
        print(f"{article['name']} - Prix : {article['price']}")

# Fonction pour vider le panier
def vider_panier():
    panier.clear()
    print("Le panier a été vidé.")

# Boucle principale du programme
while True:
    afficher_menu()
    choix = input("Quel est votre choix : ")

while not choix.isdigit():
    print("Choisissez uniquement un élément existant !!!")
    print("Quel est votre choix : ")

choix = int(choix) 

if choix == 1:
        ajouter_article()
elif choix == 2:
            supprimer_article()
elif choix == 3:
            afficher_articles()
elif choix == 4:
            vider_panier()
elif choix == 5:
            print("Fin du programme.")
            
else:
            print("Choix invalide. Veuillez sélectionner une option valide.")
