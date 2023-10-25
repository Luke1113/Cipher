def Encrypt(pl,key):
    ci=""
    key=SetKey(pl,key)
    for x in range(len(pl)):
        ci+=GetChar((GetLocation(pl[x])+GetLocation(key[x]))%26)
    return ci
def SetKey(txt,key):
    nkey=""
    while True:
        nkey+=key
        if len(nkey)>=len(txt):
            break
    return nkey
def Decrypt(ci,key):
    pl=""
    key=SetKey(ci,key)
    for x in range(len(ci)):
        pl+=GetChar((GetLocation(ci[x])-GetLocation(key[x]))%26)
    return pl
def GetLocation(char):
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for x in range(len(alpha)):
        if char.upper()==alpha[x]:
            return x
def GetChar(loc):
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return alpha[loc]
#print(Encrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZ","CBA"))
#print(Decrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZ","ABC"))
#print(Decrypt(Encrypt("ILOVEANAPPLE","APPLE"),"APPLE"))
