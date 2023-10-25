def Encrypt(pl,key):
    ci=""
    for x in range(len(pl)):
        for y in range(len(key)):
            if pl[x]==key[y][0]:
                ci+=key[y][1]
                break
    return ci
def Decrypt(ci,key):
    pl=""
    for x in range(len(ci)):
        for y in range(len(key)):
            if ci[x]==key[y][1]:
                pl+=key[y][0]
    return pl
key=[["A","B"],["B","C"],["C","D"],["D","E"],["E","F"],["F","G"],["G","H"],["H","I"],["I","J"],["J","K"],["K","L"],["L","M"],["M","N"],["N","O"],["O","P"],["P","Q"],["Q","R"],["R","S"],["S","T"],["T","U"],["U","V"],["V","W"],["W","X"],["X","Y"],["Y","Z"],["Z","A"]]
print(Encrypt("ABCD",key))
print(Decrypt("BCDE",key))
