# Créez une liste vide pour le panier
panier = []

while True:
    print("""
        Choisissez parmi les 5 options suivantes:
            1- Ajouter un article dans le panier
            2- Supprimer un article du panier
            3- Afficher tous les articles
            4- Vider le panier
            5- Quitter""")

    choix = input("Quel est votre choix : ") 
    while not choix.isdigit():
        print("Choisissez uniquement l'une des options existante !!!")
        choix = input("Quel est votre choix : ") 
        
    choix = int(choix)
 
    if choix == 1:
        # Demandez à l'utilisateur d'entrer un article et son prix
        article = input("Entrez le nom de l'article : ")
        prix = float(input("Entrez le prix de l'article : "))

        # Créez un dictionnaire avec les informations de l'article
        nouvel_article = {"name": article, "price": prix}

        # Ajoutez le dictionnaire au panier
        panier.append(nouvel_article)
        print(f"{article} a été ajouté au panier.")

    elif choix == 2:
        # Demandez à l'utilisateur le nom de l'article à supprimer
        article_supprime = input("Entrez le nom de l'article à supprimer : ")

        # Parcourez le panier et supprimez l'article s'il existe
        article_trouve = False
        for article in panier:
            if article["name"] == article_supprime:
                panier.remove(article)
                article_trouve = True
                print(f"{article_supprime} a été supprimé du panier.")
                

        if not article_trouve:
            print("Aucun article avec ce nom dans le panier.")

    elif choix == 3:
        # Affichez tous les articles dans le panier
        for article in panier:
            print(f"{article['name']} - Prix : {article['price']}")

    elif choix == 4:
        # Videz le panier
        panier.clear()
        print("Le panier a été vidé.")

    elif choix == 5:
        # Quittez le programme
        print("Fin du programme.")
        

    else:
        print("Choix invalide. Veuillez sélectionner une option valide.")
