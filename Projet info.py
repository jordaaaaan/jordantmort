
def display_map(m, d):
    for row in m:
        for x in row:
            print(d[x], end=' ')
        print()
mapp=[[0,0,1],[0,1,1],[0,1,0]]
legende={0:' ',1:'#'}
display_map(mapp,legende)
def create_perso(pos):
    P={"char":"o","x":pos[0],"y":pos[1]}
    return P
create_perso((0,0))  
def display_map_and_char(m, d, p):
    map2= [ligne.copy() for ligne in m]
    map2[p["y"]][p["x"]] = p["char"]
    for ligne in map2:
        for x in ligne:
            print(d[x], end=' ')
        print()
mapp = [[0, 0, 1], [0, 1, 1], [0, 1, 0]]
legende = {0: ' ', 1: '#'}
perso = create_perso((0, 0))
display_map_and_char(mapp, legende, perso)
def update_p(lettre, p,m):
    if lettre.lower() in ["z", "q", "s", "d"]:
        posi = p.get("x""y", (0, 0))
        x, y = posi
        if lettre.lower() == "z" and x-1>=0:  
            posf= (x - 1, y)
        elif lettre.lower() == "q":
            posf = (x + 1, y)
        elif lettre.lower() == "s":
            posf = (x, y + 1)
        elif lettre.lower() == "d":
            posf = (x, y - 1)
        p["position"] =posf
    else:
        print("direction innaccessible utilisez 'z' 'q'  's' ou 'd' .")
perso={"position":(1,1)}
m=[[0,0,1],[0,1,1],[0,1,0]]
dico = {"joueur": "o"}

while True:
    display_map_and_char(m,perso,dico)
    direc= input("Choisissez une direction (z, q, s, d) ou 'a' pour quitter : ")
    if direc.lower()=='a':
        break
    else:
        update_p(direc,p,m)
    
