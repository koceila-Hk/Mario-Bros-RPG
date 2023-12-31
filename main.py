
# -------- function menu ---------

def menu():

     print("\n     Bienvenue sur Mario Bros!\n\n     Menu:\n\n  1. Create New Game\n  2. Load Saved Game\n  3. About\n  4. Exit\n")
     print("---------------------")
     answer = input("")
     

     while answer != "1" and answer != "2" and answer != "3" and answer != "4":
          print("Une entrée inconnue a été saisie : \n\n Réessayer")
          answer = input("")
          print("---------------")
     if answer == "1":
          CreateNewGame()

     elif answer == "2":
          LoadSaved()
     
     elif answer == "3":
          About()
    
     elif answer == "4":
          Exit()

# -------- function initialise ---------
          
def init(name):           # fonction 'init' retourne les caractéristiques du joueur
     joueur = {
          "nom" : name,
          "xp" : 0,
          "hp" : 100,
          "niveau" : 1,
          "attaque" : 10,
          "defense" : 5,
          "position" : [16, 16]
     }
     return joueur

# ------- function Create New Game ---------

def CreateNewGame():
      
    user = input("Enter your name: ")
    print("---------------------")
    print("Welcome!", user)
    print("---------------")

    joueur = init(user)               # la fonction 'init' est exécutée avec le nom fourni en argument

    print("Game created for player:", joueur["nom"])
    print("-------------")
    print("XP:", joueur["xp"])
    print("HP:", joueur["hp"])
    print("Niveau:", joueur["niveau"])
    print("Attaque:", joueur["attaque"])
    print("defense:", joueur["defense"])
    print("Position:", joueur["position"])

# --------- function About -----------
          
def About():

     print("histoire de Mario Bros...\n\n Voulez-vous revenir au menu \n\n - Oui -\n - Non -\n")
     print("------------------------")
     answer = input("")

     while answer != "oui" and answer != "Oui" and answer != "non" and answer != "Non":
          print("Une entrée inconnue a été saisie : \n\n Réessayer")       # if answer it's not true return false 
          answer = input("")
     
     if answer == "oui" or answer == "Oui":        # answer true return menu
          menu()
     elif answer == "non" or answer == "Non":
          About()

# --------- function of exit -----------
          
def Exit(): 

     print("Voulez-vous vraiment quitter le jeu ?\n\n - Oui -\n - Non -\n")
     print("--------------------")
     answer = input("")

     while answer != "oui" and answer != "Oui" and answer != "non" and answer != "Non": 
          print("Une entrée inconnue a été saisie : \n\n Réessayer")
          answer = input("")

     if answer == "oui" or answer == "Oui":       # quit game
          print("\nA bientôt sur Mario Bros!")    # Add history 
          exit 
     elif answer == "non" or answer == "Non":     # back to menu
          menu()



menu()


