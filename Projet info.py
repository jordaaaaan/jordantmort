
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
    copy_map= [i.copy() for i in m]
    copy_map[p["y"]][p["x"]] = p["char"]
    for i in copy_map:
        for j in i:
            print(d[j], end=' ')
        print()
mapp = [[0, 0, 1], [0, 1, 1], [0, 1, 0]]
legende = {0:'',1:'#', 'o': 'o'}
perso = create_perso((0, 0))
display_map_and_char(mapp, legende, perso)
