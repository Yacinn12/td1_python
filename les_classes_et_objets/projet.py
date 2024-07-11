

class Client:
    def __init__(self, code, nom, téléphone, adresse, email):
        self.code = code
        self.nom = nom
        self.téléphone = téléphone
        self.adresse = adresse
        self.email = email
        self.solde = 0

    def afficher_info(self):
        print("Code client :", self.code)
        print("Nom :", self.nom)
        print("Téléphone :", self.téléphone)
        print("Adresse :", self.adresse)
        print("Email :", self.email)
        print("Solde :", self.solde)
        print()

    def modifier_info(self):
        self.nom = input("Nouveau nom : ")
        self.téléphone = input("Nouveau téléphone : ")
        self.adresse = input("Nouvelle adresse : ")
        self.email = input("Nouvel email : ")

class Transaction:
    def __init__(self, ref_paiement, code_emmeteur, code_recepteur, date_transaction, montant, canal):
        self.ref_paiement = ref_paiement
        self.code_emmeteur = code_emmeteur
        self.code_recepteur = code_recepteur
        self.date_transaction = date_transaction
        self.montant = montant
        self.canal = canal

transactions = []
clients = []

# Fonctions pour la gestion des clients

def afficher_clients():
    for client in clients:
        client.afficher_info()

def ajouter_client():
    code = input("Code client : ")
    if trouver_client(code):
        print("Ce code client est déjà utilisé.")
        return
    nom = input("Nom : ")
    téléphone = input("Téléphone : ")
    adresse = input("Adresse : ")
    email = input("Email : ")
    clients.append(Client(code, nom, téléphone, adresse, email))
    print("Le client a bien été ajouté.")

def supprimer_client():
    code = input("Code client : ")
    client = trouver_client(code)
    if not client:
        print("Ce code client n'existe pas.")
        return
    clients.remove(client)
    print("Le client a bien été supprimé.")

def modifier_info_client():
    code = input("Code client : ")
    client = trouver_client(code)
    if not client:
        print("Ce code client n'existe pas.")
        return
    client.modifier_info()
    print("Les informations ont bien été modifiées.")

def afficher_solde():
    code = input("Code client : ")
    client = trouver_client(code)
    if not client:
        print("Ce code client n'existe pas.")
        return
    print("Le solde de", client.nom, "est de", client.solde, "€.")

def trouver_client(code):
    for client in clients:
        if client.code == code:
            return client
    return None

# Fonctions pour la gestion des transactions

def afficher_transactions():
    for transaction in transactions:
        print("Référence paiement :", transaction.ref_paiement)
        print("Code émetteur :", transaction.code_emmeteur)
        print("Code récepteur :", transaction.code_recepteur)
        print("Date transaction :", transaction.date_transaction)
        print("Montant :", transaction.montant, "€")
        print("Canal :", transaction.canal)
        print()

def afficher_transactions_client():
    code = input("Code client : ")
    for transaction in transactions:
        if transaction.code_emmeteur == code or transaction.code_recepteur == code:
            print("Référence paiement :", transaction.ref_paiement)
            print("Code émetteur :", transaction.code_emmeteur)
            print("Code récepteur :", transaction.code_recepteur)
            print("Date transaction :", transaction.date_transaction)
            print("Montant :", transaction.montant, "€")
            print("Canal :", transaction.canal)
            print()

def ajouter_transaction():
    ref_paiement = input("Référence paiement : ")
    code_emmeteur = input("Code émetteur : ")
    if not trouver_client(code_emmeteur):
        print("Ce code émetteur n'existe pas.")
        return
    code_recepteur = input("Code récepteur : ")
    if not trouver_client(code_recepteur):
        print("Ce code récepteur n'existe pas.")
        return
    date_transaction = input("Date transaction : ")
    montant = float(input("Montant : "))
    canal = input("Canal : ")
    transactions.append(Transaction(ref_paiement, code_emmeteur, code_recepteur, date_transaction, montant, canal))
    incrementer_solde(code_recepteur, montant)
    decrementer_solde(code_emmeteur, montant)
    print("La transaction a bien été ajoutée.")

def incrementer_solde(code, montant):
    client = trouver_client(code)
    client.solde += montant

def decrementer_solde(code, montant):
    client = trouver_client(code)
    client.solde -= montant

# Menu

while True:
    print("Menu :")
    print("1 - Gestion des clients")
    print("2 - Gestion des transactions")
    print("3 - Sortir")

    choix = input("Votre choix : ")
    print()

    if choix == "1":
        print("Gestion des clients :")
        print("1 - Afficher la liste des clients")
        print("2 - Ajouter un client")
        print("3 - Supprimer un client")
        print("4 - Modifier les informations d'un client")
        print("5 - Afficher le solde d'un client")

        choix = input("Votre choix : ")
        print()

        if choix == "1":
            afficher_clients()
        elif choix == "2":
            ajouter_client()
        elif choix == "3":
            supprimer_client()
        elif choix == "4":
            modifier_info_client()
        elif choix == "5":
            afficher_solde()

    elif choix == "2":
        print("Gestion des transactions :")
        print("1 - Afficher toutes les transactions")
        print("2 - Afficher les transactions d'un client")
        print("3 - Ajouter la transaction entre deux clients")

        choix = input("Votre choix : ")
        print()

        if choix == "1":
            afficher_transactions()
        elif choix == "2":
            afficher_transactions_client()
        elif choix == "3":
            ajouter_transaction()

    elif choix == "3":
        break

    else:
        print("Choix invalide. Veuillez réessayer.")
        
        
        
        
      