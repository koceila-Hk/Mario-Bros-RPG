import random


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

# ------ function handle_movement_event --------
          
def handle_movement_event(joueur, game_map):
     event_chance = random.random()

     if event_chance < 0.2:
          print("Vous avez trouvé un trésor !")
          joueur["xp"] += 20  # gagne de l'expérience en trouvant un trésor
     elif event_chance < 0.4:
          print("Vous entrez dans un combat !")
          combat(joueur)    # Fonction à implémenter pour gérer les combats   
     else:
          print("Vous continuez votre chemin")

     check_level_up(joueur)  # Vérifie si le joueur a gagné assez d'expérience pour monter de niveau

# --------- function check_level_up ----------

def check_level_up(joueur):
    if joueur["xp"] >= 100:  # Par exemple, le joueur monte de niveau après avoir atteint 100 points d'expérience
        joueur["niveau"] += 1
        joueur["xp"] = 0  # Réinitialise l'expérience pour le prochain niveau
        joueur["attaque"] += 5  # Augmente l'attaque à chaque niveau
        joueur["defense"] += 3  # Augmente la défense à chaque niveau
        print(f"Bravo ! Vous êtes maintenant niveau {joueur['niveau']}.")


# --------- function combat -----------

def combat(joueur):
    ennemi_difficulte = random.randint(1, joueur["niveau"] + 2)              # Fonction à implémenter pour gérer les combats
    ennemi_force = 10 + ennemi_difficulte * 3                                  # Vous pouvez définir la logique des combats ici et ajuster les points d'expérience gagnés en conséquence
    print(f"Combat en cours contre un ennemi de difficulté {ennemi_difficulte}.")

# --------- function init_map -----------

def init_map(size):
# Initialiser une carte vide de la taille spécifiée
     return [[0] * size[0] for _ in range(size[1])]

#--------------------
def check_boundaries(position, map_size):
    # Vérifier si le joueur est dans les limites de la carte
     position[0] = max(0, min(position[0], map_size[0] - 1))
     position[1] = max(0, min(position[1], map_size[1] - 1))


def print_map(game_map):
    # Afficher la carte
    for row in game_map:
        print(row)

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
    game_map = init_map((16, 16))      # Initialiser une carte de dimensions [16, 16]

    print("Game created for player:", joueur["nom"])
    print("-------------")
    print("XP:", joueur["xp"])
    print("HP:", joueur["hp"])
    print("Niveau:", joueur["niveau"])
    print("Attaque:", joueur["attaque"])
    print("defense:", joueur["defense"])
    print("Position:", joueur["position"])
    print("-----------------")
    print("Game Map:")

    move = input("Voulez-vous bouger?  (Oui/Non) : ")

    while move.lower() == "oui":
         direction = input("Entrer une direction (Nord/Sud/Ouest/Est): ")

         if direction.lower() == "nord":
              joueur["position"][1] -= 1
         elif direction.lower() == "sud":
              joueur["position"][1] += 1
         elif direction.lower() == "est":
              joueur["position"][0] += 1
         elif direction.lower() == "ouest":
              joueur["position"][0] -= 1
         else:
            print("direction invalide. Try again.")


     
        # Vérifier si le joueur est toujours dans les limites de la carte
         check_boundaries(joueur["position"], (32, 32))

        # Afficher la nouvelle position du joueur
         print("New Position:", joueur["position"])

         # Gérez les événements du mouvement
         handle_movement_event(joueur, game_map)

        # Ajustez la difficulté des événements en fonction du niveau du joueur
         joueur_difficulte = joueur["niveau"] * 0.02
         event_difficulte = random.random() - joueur_difficulte

        # Vérifie si le joueur a gagné assez d'expérience pour monter de niveau
         check_level_up(joueur)
 
        # Afficher la carte mise à jour

         move = input("Voulez-vous bouger encore ? (Oui/Non) : ")
               

# --------- function About -----------
          
def About():

     print("histoire de Mario Bros...\n\n Voulez-vous revenir au menu \n")
     print("------------------------")
     answer = input("Oui/Non : ")

     while answer.lower() not in ["oui", "non"]:
          print("Une entrée inconnue a été saisie : \n\n Réessayer")       # if answer it's not true return false 
          answer = input("")
     
     if answer.lower() == "oui":        # answer true return menu
          menu()
     elif answer.lower() == "non":
          About()

# --------- function of exit -----------
          
def Exit(): 

     print("Voulez-vous vraiment quitter le jeu ?\n")
     print("--------------------")
     answer = input("Oui/Non : ")

     while answer.lower() not in ["oui", "non"]: 
          print("Une entrée inconnue a été saisie : \n\n Réessayer")
          answer = input("")

     if answer.lower() == "oui":       # quit game
          print("\nA bientôt sur Mario Bros!")    # Add history 
          exit 
     elif answer.lower() == "non":     # back to menu
          menu()

menu()



