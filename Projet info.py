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

