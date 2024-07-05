# : Écrire un programme qui demande à l'utilisateur d'entrer une note.
# Selon la note, afficher un message indiquant la mention obtenue .

note_obtenue = input("Veuillez entrer votre note : ") 

while not note_obtenue.isdigit():
    print(" Erreur ") 
    note_obtenue =input("Veuillez entrer votre note : ")
    
note_obtenue =int(note_obtenue)
    

if note_obtenue > 20:
    print("Cette note n'existe pas !!!!") 
elif 18 <= note_obtenue <= 20:
    print("Excellent") 
elif 16<= note_obtenue < 18:
    print("Très bien ")
elif 14 <= note_obtenue < 16:
    print("Bien") 
elif 12 <= note_obtenue < 14:
    print("Satisfaisant") 
elif 10 <= note_obtenue < 12:
    print("Passable") 
else :
    print("Echec") 