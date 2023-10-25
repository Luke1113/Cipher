
def SetTable(tkey):
    ttable=[]
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    keyAlpha=tkey.upper()+alpha
    keyAlpha=keyAlpha.replace("J","I")
    count=-1
    tableAlpha=[]
    for x in range(5):
        ttable.append([])
        for y in range(5):
            ttable[x].append([])
            while True:
                count+=1
                if keyAlpha[count] not in tableAlpha:
                    ttable[x][y]=keyAlpha[count]
                    tableAlpha.append(keyAlpha[count])
                    break
    return ttable
def SetPlainText(tpl):
    uplt=[]
    tplt=tpl.upper()
    tplt=tplt.replace("J","I")
    ttplt=""
    count=0
    skip=0
    for x in range(len(tpl)):
        if tplt[x]!=" ":
            ttplt+=tplt[x]
    while True:
        if count>=len(ttplt)-2:
            if count!=len(ttplt)-2:
                uplt.append([ttplt[-1],"X"])
            break
        if ttplt[count]!=ttplt[count+1]:
            uplt.append([ttplt[count],ttplt[count+1]])
            count+=2
        else:
            uplt.append([ttplt[count],"X"])
            count+=1
    return uplt
def SetCipherText(tci):
    ucit=[]
    for x in range(0,len(tci),2):
        ucit.append([tci[x],tci[x+1]])
    return ucit
def EncryptText(ttable,tpl):
    cit=""
    for x in range(len(tpl)):
        if FindLocation(tpl[x][0],ttable)[0]==FindLocation(tpl[x][1],ttable)[0]:
            cit+=ttable[FindLocation(tpl[x][0],ttable)[0]][(FindLocation(tpl[x][0],ttable)[1]+1)%5]
            cit+=ttable[FindLocation(tpl[x][1],ttable)[0]][(FindLocation(tpl[x][1],ttable)[1]+1)%5]
        elif FindLocation(tpl[x][0],ttable)[1]==FindLocation(tpl[x][1],ttable)[1]:
            cit+=ttable[(FindLocation(tpl[x][0],ttable)[0]+1)%5][FindLocation(tpl[x][0],ttable)[1]]
            cit+=ttable[(FindLocation(tpl[x][1],ttable)[0]+1)%5][FindLocation(tpl[x][1],ttable)[1]]
        else:
            cit+=ttable[FindLocation(tpl[x][0],ttable)[0]][FindLocation(tpl[x][1],ttable)[1]]
            cit+=ttable[FindLocation(tpl[x][1],ttable)[0]][FindLocation(tpl[x][0],ttable)[1]]
    return cit
def DecryptText(ttable,tpl):
    cit=""
    for x in range(len(tpl)):
        if FindLocation(tpl[x][0],ttable)[0]==FindLocation(tpl[x][1],ttable)[0]:
            cit+=ttable[FindLocation(tpl[x][0],ttable)[0]][(FindLocation(tpl[x][0],ttable)[1]-1)%5]
            cit+=ttable[FindLocation(tpl[x][1],ttable)[0]][(FindLocation(tpl[x][1],ttable)[1]-1)%5]
        elif FindLocation(tpl[x][0],ttable)[1]==FindLocation(tpl[x][1],ttable)[1]:
            cit+=ttable[(FindLocation(tpl[x][0],ttable)[0]-1)%5][FindLocation(tpl[x][0],ttable)[1]]
            cit+=ttable[(FindLocation(tpl[x][1],ttable)[0]-1)%5][FindLocation(tpl[x][1],ttable)[1]]
        else:
            cit+=ttable[FindLocation(tpl[x][0],ttable)[0]][FindLocation(tpl[x][1],ttable)[1]]
            cit+=ttable[FindLocation(tpl[x][1],ttable)[0]][FindLocation(tpl[x][0],ttable)[1]]
    return cit
def FindLocation(char,ttable):
    for x in range(5):
        for y in range(5):
            if ttable[x][y]==char:
                return [x,y]
def Encrypt(pl,key):
    table=SetTable(key)
    upl=SetPlainText(pl)
    return EncryptText(table,upl)
def Decrypt(ci,key):
    table=SetTable(key)
    uci=SetCipherText(ci)
    return DecryptText(table,uci)
print(Decrypt(Encrypt("I like an apple","apple"),"apple"))

