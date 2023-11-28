def display_map(m, d):
    for i in m:
        for j in i:
            print(d[j], end=' ')
        print()
mapp=[[0,0,1],[0,1,1],[0,1,0]]
legende={0:' ',1:'#'}



def create_perso(pos):
    P={"char":"o","x":pos[0],"y":pos[1]}
    return P
create_perso((0,0))  


def display_map_and_char(m, d, p):
    copy_map= [i.copy() for i in m]
    copy_map[p["y"]][p["x"]] = p["char"]
    for i in copy_map:
        for j in i:
            print(d[j], end=' ')
        print()

# Le keys error est dû au fait qu'il y ait une confusion dans le dictionnaire de légende. Il est défini comme {0: ' ', 1: '#'}, ce qui signifie que le caractère 'o' n'est pas défini dans la légende.
# Pour résoudre le problème,on ajoute une entrée pour le caractère 'o' dans le dictionnaire de légende.

perso = create_perso((1, 2))


# question 2.3 et 2.4
def update_p(letter, p):
    if letter == "z" and p["y"] > 0:  # Haut
        p["y"] -= 1
    elif letter == "q" and p["x"] > 0:  # Gauche
        p["x"] -= 1
    elif letter == "s" and p["y"] < len(mapp) - 1:  # Bas
        p["y"] += 1
    elif letter == "d" and p["x"] < len(mapp[0]) - 1:  # Droite
        p["x"] += 1
    else:
        print("Direction invalide. Utilisez 'z' pour haut, 'q' pour gauche, 's' pour bas, 'd' pour droite.")


#while True: 
   # display_map_and_char(mapp, legende, perso)
   # direction = input("Quel déplacement ? ")
   # update_p(direction, perso)
#nous devons faire appel aux fonctions qu'après avoir finis tout le code car les boucles while sont infinis et donc la suite n'est jamais lu


# question 3.1
def update_p(letter, p, m):
    """
    Met à jour la position du joueur en fonction de la lettre de direction.
    """
    if letter == "z" and p["y"] > 0 and m[p["y"] - 1][p["x"]] != 1:  # Haut
        p["y"] -= 1
    elif letter == "q" and p["x"] > 0 and m[p["y"]][p["x"] - 1] != 1:  # Gauche
        p["x"] -= 1
    elif letter == "s" and p["y"] < len(m) - 1 and m[p["y"] + 1][p["x"]] != 1:  # Bas
        p["y"] += 1
    elif letter == "d" and p["x"] < len(m[0]) - 1 and m[p["y"]][p["x"] + 1] != 1:  # Droite
        p["x"] += 1
    else:
        print("Direction invalide ou sortie de la carte. Utilisez 'z' pour haut, 'q' pour gauche, 's' pour bas, 'd' pour droite.")

# Initialisation des variables

#while True:
    #display_map_and_char(mapp, legende, perso)
  #  direction = input("Quel déplacement ? ")
  #  update_p(direction, perso, mapp)



#3.2 
# pour vérifier si la case suivante dans la direction demandée contient un mur, elle est représenté par 1.
def update_p(letter, p, m):
    next_x,next_y=p["x"],p["y"]
    if letter == "z":
        next_y -= 1
    elif letter == "q":
        next_x -= 1
    elif letter == "s":
        next_y += 1
    elif letter == "d":
        next_x += 1
    else:
        print("Direction invalide. Utilisez 'z' pour haut, 'q' pour gauche, 's' pour bas, 'd' pour droite.")
        return

    if 0 <= next_y < len(m) and 0 <= next_x < len(m[0]) and m[next_y][next_x] != 1:
        p["y"], p["x"] = next_y, next_x
    else:
        print("Déplacement impossible. Il y a un mur. Utilisez 'z' pour haut, 'q' pour gauche, 's' pour bas, 'd' pour droite.")



#while True:
    #display_map_and_char(mapp, legende, perso)
   # direction = input("Quel déplacement ? ")
  #  update_p(direction, perso, mapp)
    
# 3.4
import random
def create_objects(nb_objects, m):
    objects=set()
    ligne,colone= len(m), len(m[0])
    
    while len(objects) < nb_objects:
        x, y = random.randint(0, colone - 1), random.randint(0, ligne - 1)
        if m[y][x] == 0:
            objects.add((x, y))
    return objects

def display_map_char_and_objects(m, d, p, objects):
    copy_map = [i.copy() for i in m]
    copy_map[p["y"]][p["x"]] = p["char"]
    for obj in objects:
        x,y=obj
        copy_map[y][x] = '.'
    for ligne in copy_map:
        for cell in ligne:
            print(d[cell], end=' ')
        print()

mapp = [[0, 0, 1], [0, 1, 1], [0, 1, 0]]
legende = {0: ' ', 1: '#', 'o': 'o', '.': '.'}
perso = create_perso((1, 2))
objects = create_objects(3, mapp)



# 3.5
def update_objects(p, objects):
    if (p["x"], p["y"]) in objects:
        objects.remove((p["x"], p["y"]))

while True:
    display_map_char_and_objects(mapp, legende, perso, objects)
    direction = input("Quel déplacement ? ")
    update_p(direction, perso, mapp)
    update_objects(perso, objects)

# 3.6
def create_perso(pos):
    P = {"char": "o", "x": pos[0], "y": pos[1], "score": 0}
    return P

def update_objects(p, objects):
    if (p["x"], p["y"]) in objects:
        objects.remove((p["x"], p["y"]))

def display_map_char_and_objects(m, d, p, objects):
    copy_map = [i.copy() for i in m]
    copy_map[p["y"]][p["x"]] = p["char"]

    for obj in objects:
        x, y = obj
        copy_map[y][x] = '.'

    for row in copy_map:
        for cell in row:
            print(d[cell], end=' ')
        print()

    print(f"Score: {p['score']}")

while True:
    display_map_char_and_objects(mapp, legende, perso, objects)
    direction = input("Quel déplacement ? ")
    update_p(direction, perso, mapp)
    update_objects(perso, objects)


