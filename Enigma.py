plug=[["E","K"],["N","J"],["I","P"],["G","Y"],["M","O"],["A","W"]]
rot1=["EKMFLGDQVZNTOWYHXUSPAIBRCJ","ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
rot2=["AJDKSIRUXBLHWTMCQGZNPYFVOE","ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
rot3=["BDFHJLCPRTXVZNYEIWGAKMUSQO","ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
reflec=[["A","Y"],["B","R"],["C","U"],["D","H"],["E","Q"],["F","S"],["G","L"],["H","D"],["I","P"],["J","X"],["K","N"],["L","G"],["M","O"],["N","K"],["O","M"],["P","I"],["Q","E"],["R","B"],["S","F"],["T","Z"],["U","C"],["V","W"],["W","V"],["X","J"],["Y","A"],["Z","T"]]
key="CTY"
#pl="ILOVEANAPPLE"
pl="A"
cipher=""
rots=[rot2,rot3,rot1]
def Alpha(tx):
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for x in range(len(alpha)):
        if alpha[x]==tx:
            return x
def Mod(ind):
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    tmp=alpha[ind]
    return tmp
def Plug(tx,_plug):
    tmp=""
    for x in range(len(tx)):
        check=False
        for y in range(len(_plug)):
            _break=False
            for z in range(2):
                if tx[x]==_plug[y][z]:
                    if z==0:
                        tmp+=_plug[y][1]
                    elif z==1:
                        tmp+=_plug[y][0]
                    check=True
                    _break=True
                    break
            if _break==True:
                break
        if check==False:
            tmp+=tx[x]
    return tmp
def Ref(ind,ref):
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for x in range(len(ref)):
        for y in range(2):
            if alpha[ind]==ref[x][y]:
                if y==0:
                    return ref[x][1]
                elif y==1:
                    return ref[x][0]
    
def Rot(ind,rot):
    for x in range(len(rot[1])):
#        print(rot[0][ind],",",rot[1][x])
        if rot[0][ind]==rot[1][x]:
            return x
def RotI(ind,rot):
    for x in range(len(rot[0])):
#        print(rot[0][ind],",",rot[1][x])
        if rot[0][x]==rot[1][ind]:
            return x
def RotRot():
    global rots
    if rots[0][1][-1]=="A":
        rots[0]=[rots[0][0][-1]+rots[0][0][0:len(rots[0][0])-1],rots[0][1][-1]+rots[0][1][0:len(rots[0][1])-1]]
        rots[1]=[rots[1][0][-1]+rots[1][0][0:len(rots[1][0])-1],rots[1][1][-1]+rots[1][1][0:len(rots[1][1])-1]]
    else:
        rots[0]=[rots[0][0][-1]+rots[0][0][0:len(rots[0][0])-1],rots[0][1][-1]+rots[0][1][0:len(rots[0][1])-1]]
    if rots[1][1][-1]=="A":
        rots[2]=[rots[2][0][-1]+rots[2][0][0:len(rots[2][0])-1],rots[2][1][-1]+rots[2][1][0:len(rots[2][1])-1]]
        rots[1]=[rots[1][0][-1]+rots[1][0][0:len(rots[1][0])-1],rots[1][1][-1]+rots[1][1][0:len(rots[1][1])-1]]
#    if rot3[1][-1]=="A":
#        rot1=[rot1[0][-1]+rot1[0][0:len(rot1[0])-1],rot1[1][-1]+rot1[1][0:len(rot1[1])-1]]
#        rot2=[rot2[0][-1]+rot2[0][0:len(rot2[0])-1],rot2[1][-1]+rot2[1][0:len(rot2[1])-1]]
#pl=Plug(pl,plug)
def Key():
    global key,rots
    rots[0]=[rots[0][0][len(rots[0][0])-Alpha(key[0]):len(rots[0][0])]+rots[0][0][0:len(rots[0][0])-Alpha(key[0])],rots[0][1][len(rots[0][1])-Alpha(key[0]):len(rots[0][1])]+rots[0][1][0:len(rots[0][1])-Alpha(key[0])]]
    rots[1]=[rots[1][0][len(rots[1][0])-Alpha(key[1]):len(rots[1][0])]+rots[1][0][0:len(rots[1][0])-Alpha(key[1])],rots[1][1][len(rots[1][1])-Alpha(key[1]):len(rots[1][1])]+rots[1][1][0:len(rots[1][1])-Alpha(key[1])]]
    rots[2]=[rots[2][0][len(rots[2][0])-Alpha(key[2]):len(rots[2][0])]+rots[2][0][0:len(rots[2][0])-Alpha(key[2])],rots[2][1][len(rots[2][1])-Alpha(key[2]):len(rots[2][1])]+rots[2][1][0:len(rots[2][1])-Alpha(key[2])]]

Key()

#rots[0]=[rots[0][0][len(rots[0][0])-Alpha(key[0]):-2]+rots[0][0][0:len(rots[0][0])-Alpha(key[0])+1],rots[0][1][len(rots[0][1])-Alpha(key[0]):-2]+rots[0][1][0:len(rots[0][1])-Alpha(key[0])+1]]
#print(rot2)
#print(Ref(Rot(Rot(Rot(Alpha(pl[x]),rots[0]),rots[1]),rots[2]),reflec))
#print(Alpha(Ref(Rot(Rot(Rot(Alpha(pl[0]),rots[0]),rots[1]),rots[2]),reflec)))
pl=Plug(pl,plug)
for x in range(len(pl)):
    #print(Alpha(pl[x]))
    #print(Rot(Alpha(pl[x]),rot2))
    cipher+=Mod(RotI(RotI(RotI(Alpha(Ref(Rot(Rot(Rot(Alpha(pl[x]),rots[0]),rots[1]),rots[2]),reflec)),rots[2]),rots[1]),rots[0]))
    RotRot()
    #cipher+=Ref(Rot(Rot(Rot(Alpha(pl[x]),rots[0]),rots[1]),rots[2]),reflec)
cipher=Plug(cipher,plug)
print(cipher)

