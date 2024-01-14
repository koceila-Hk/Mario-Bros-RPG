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
          exit()

#----------limite position-----------------------

def check_boundaries(position, map_size):
    position[0] = max(-map_size[0], min(position[0], map_size[0]))
    position[1] = max(-map_size[1], min(position[1], map_size[1]))

# -------- function initialise ----------------
          
def init(user):           # fonction 'init' retourne les caractéristiques du joueur
     joueur = {
          "nom" : user,
          "hp" : 100,
          "position" : [0, 0]
     }
     return joueur

# --------- function init_map ----------------

def init_map(size):
    game_map = [[" "] * size[0] for _ in range(size[1])]

    return game_map

# --------- function monster ----------------

def create_monster(position):
    monster = {
        "hp": random.randint(20, 50),
        "position": position
    }
    return monster

# --------- function final boss -------------

def create_final_boss(position):
     final_boss = {
          "hp" : 115,
          "position" : position
     }
     return final_boss

# ----------- function hp --------------------

def create_hp (position):
     hp_boost = {
          "hp_value" : random.randint(10, 25),
          "position" : position
     }
     return hp_boost

# --------- function combat ----------------

def combat(user, monster):
    print("\nCombat starts!")
    while user["hp"] > 0 and monster["hp"] > 0:
        player_attack = random.randint(10, 25)
        monster_attack = random.randint(5, 15)

        print(f"\nPlayer HP: {user['hp']}  Monster HP: {monster['hp']}")
        print("1. Attaquer\n2. Fuir")
        choice = input("Choisissez votre action (1/2): ")

        if choice == "1":
            print(f"\n{user['nom']} attaque le monstre et lui inflige des dégâts. {player_attack} damage.")
            monster["hp"] -= player_attack
            if monster["hp"] <= 0:
                print("Vous avez vaincu le monstre !")
            else:
                print(f"Contre-attaques et infliges de monstres {monster_attack} damage.")
                user["hp"] -= monster_attack
                if user["hp"] <= 0:
                    print("Vous avez été vaincue par le monstre.")
        elif choice == "2":
            print("Vous fuyez le monstre.")
            break
        else:
            print("Choix non valide. Réessayez.")


# ------- function Create New Game -----------

def CreateNewGame():
      
    user = input("Entrez votre nom: ")
    print("---------------------")
    print("Bienvenue!", user)
    print("---------------")

    joueur = init(user)               # la fonction 'init' est exécutée avec le nom fourni en argument

    print("Jeu créé pour le joueur:", joueur["nom"])
    print("HP:", joueur["hp"])
    print("Position:", joueur["position"])
    print("-----------------")
    print("Game Map:")

    move = input("Voulez-vous bouger?  (Oui/Non) : ")

    while move.lower() == "oui":
         direction = input("Entrer une direction (Nord/Sud/Ouest/Est): ")
         print("-------------------------")

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
         check_boundaries(joueur["position"], (6, 6))

        # Afficher la nouvelle position du joueur
         print("New Position:", joueur["position"])
         print("============  ======")

        # Create a monster in the game
         monster_position = [1, 1]
         monster = create_monster(monster_position)
         print(f"\nMonster appears at position: {monster['position']}")
         print("------------------")

         # Monstre final position
         final_boss_position = [5, 5]
         final_boss = create_final_boss(final_boss_position)
         print(f"\nFinal Boss appears at position: {final_boss['position']}")
         print("-------------------")

        # Start combat
         if joueur["position"] == monster["position"]:
              combat(joueur, monster)
         elif joueur["position"] == final_boss["position"]:
              combat(joueur, final_boss)

        #Créer un bonus de points de vie 
         hp_boost_position = [3, 3]
         hp_boost = create_hp(hp_boost_position)
         print(f"\nHp boost appears at position: {hp_boost['position']}")
         print("-------------------")

        # Hp boost
         if joueur["position"] == hp_boost["position"]:
            joueur["hp"] += hp_boost["hp_value"]
            print(f"You gained {hp_boost['hp_value']} HP. Your current HP: {joueur['hp']}")

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
          
def exit(): 

     print("Voulez-vous vraiment quitter le jeu ?\n")
     print("--------------------")
     answer = input("Oui/Non : ")

     while answer.lower() not in ["oui", "non"]: 
          print("Une entrée inconnue a été saisie : \n\n Réessayer")
          answer = input("")
     if answer.lower() == "oui":       # quit game
          print("\nA bientôt sur Mario Bros!")    # Add history 
          exit()
     elif answer.lower() == "non":     # back to menu
          menu()

menu()

