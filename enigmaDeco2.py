rot1=["EKMFLGDQVZNTOWYHXUSPAIBRCJ","ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
rot2=["AJDKSIRUXBLHWTMCQGZNPYFVOE","ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
rot3=["BDFHJLCPRTXVZNYEIWGAKMUSQO","ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
reflec=[["A","Y"],["B","R"],["C","U"],["D","H"],["E","Q"],["F","S"],["G","L"],["H","D"],["I","P"],["J","X"],["K","N"],["L","G"],["M","O"],["N","K"],["O","M"],["P","I"],["Q","E"],["R","B"],["S","F"],["T","Z"],["U","C"],["V","W"],["W","V"],["X","J"],["Y","A"],["Z","T"]]
key="CTY"
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
        if rot[0][ind]==rot[1][x]:
            return x
def RotI(ind,rot):
    for x in range(len(rot[0])):
        if rot[0][x]==rot[1][ind]:
            return x
def Key():
    global key,rots
    rots[0]=[rots[0][0][len(rots[0][0])-Alpha(key[0]):len(rots[0][0])]+rots[0][0][0:len(rots[0][0])-Alpha(key[0])],rots[0][1][len(rots[0][1])-Alpha(key[0]):len(rots[0][1])]+rots[0][1][0:len(rots[0][1])-Alpha(key[0])]]
    rots[1]=[rots[1][0][len(rots[1][0])-Alpha(key[1]):len(rots[1][0])]+rots[1][0][0:len(rots[1][0])-Alpha(key[1])],rots[1][1][len(rots[1][1])-Alpha(key[1]):len(rots[1][1])]+rots[1][1][0:len(rots[1][1])-Alpha(key[1])]]
    rots[2]=[rots[2][0][len(rots[2][0])-Alpha(key[2]):len(rots[2][0])]+rots[2][0][0:len(rots[2][0])-Alpha(key[2])],rots[2][1][len(rots[2][1])-Alpha(key[2]):len(rots[2][1])]+rots[2][1][0:len(rots[2][1])-Alpha(key[2])]]
def Main():
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    output=[]
    for x in range(len(alpha)):
        output.append([])
        for y in range(len(output)):
            for z in range(len(output[y])):
                print(alpha[x],",",output[y][z])
                if alpha[x]==output[y][z]:
                    continue
                    print(1)
        output[-1].append(alpha[x])
        output[-1].append(Mod(RotI(RotI(RotI(Alpha(Ref(Rot(Rot(Rot(Alpha(alpha[x]),rots[0]),rots[1]),rots[2]),reflec)),rots[2]),rots[1]),rots[0])))
    print(output)
Key()
Main()

