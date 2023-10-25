mks=[]
while True:
    a=input()
    if a=="":
        break
    if len(a)==6:
        mks.append(a)
mks=["AAJCBS","GBOACM","TCEGDS","CDWDES","DEDTFA","BFSJGS","JGSHHD","HHKRIS","RIAPAS","PJDBKE","EKCILS","ILEQMS","QMAONR","ONCZOR","ZOREJI","FPEKQL","KQPMRE","MROLPL","LSONTW","NTOFUE","SUTVVP","VVKUWA","UWOSXQ","WXAXYO","XYJYZO","YZMWSO"]
sgm1=[[]]
sgm2=[[]]
sgm3=[[]]
sgms=[]
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def Sgm(sgm,ind):
    global alpha
    count=0
    stl="A"
    change=False
    while True:
        if count==26:
            break
        if change==True:
            for x in range(len(alpha)):
                change=False
                check=False
                for y in range(len(sgm)):
                    if alpha[x] in sgm[y]:
                        check=True
                        break
                if check==False:
                    stl=alpha[x]
                    break
        sgm[-1].append(stl)
        count+=1
        for x in range(len(mks)):
            if mks[x][ind]==stl:
                enl=mks[x][ind+3]
        if sgm[-1][0]==enl:
            sgm.append([])
            change=True
        else:
            stl=enl
    tmp1=[]
    for x in range(len(sgm)):
        tmp1.append(len(sgm[x]))
    tmp1.sort()
    tmp1.reverse()
    sgmp=""
    for x in range(len(tmp1)):
        sgmp+=str(tmp1[x])+"-"
    sgmp=sgmp[0:len(sgmp)-3]
    return sgmp
print(Sgm(sgm1,1))

"""
count=0
stl="A"
change=False
while True:
    if count==26:
        break
    if change==True:
        for x in range(len(alpha)):
            change=False
            check=False
            for y in range(len(sgm1)):
                if alpha[x] in sgm1[y]:
                    check=True
                    break
            if check==False:
                stl=alpha[x]
                break
    sgm1[-1].append(stl)
    count+=1
    for x in range(len(mks)):
        if mks[x][0]==stl:
            enl=mks[x][3]
    if sgm1[-1][0]==enl:
        sgm1.append([])
        change=True
    else:
        stl=enl
tmp1=[]
for x in range(len(sgm1)):
    tmp1.append(len(sgm1[x]))
tmp1.sort()
tmp1.reverse()
sgmp1=""
for x in range(len(tmp1)):
    sgmp1+=str(tmp1[x])+"-"
sgmp1=sgmp1[0:len(sgmp1)-3]
print(sgmp1)
"""
