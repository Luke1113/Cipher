seed="1011100110"
text="iloveanapple"
number=False
#1011100110
#iloveanapple
tmp=[[".","11011"],[",","01000"],["a","00011"],["b","11001"],["c","01110"],["d","01001"],
     ["e","00001"],["f","01101"],["g","11010"],["h","10100"],["i","00110"],["j","01011"],
     ["k","01111"],["l","10010"],["m","11100"],["n","01100"],["o","11000"],["p","10110"],
     ["q","10111"],["r","01010"],["s","00101"],["t","10000"],["u","00111"],["v","11110"],
     ["w","10011"],["x","11101"],["y","10101"],["z","10001"]]
count=0
ntext=""
nntext=""
nnntext=""

while True:
    if len(seed)==len(text)*5:
        break
    if (int(seed[count])+int(seed[count+3])+int(seed[count+4]))%2==0:
        seed+="0"
    else:
        seed+="1"
    count+=1
if number==False:
    for x in range(len(text)):
        for y in range(len(tmp)):
            if text[x]==tmp[y][0]:
                ntext+=tmp[y][1]
                break
else:
    for x in range(0,len(ntext)-10,10):
        for y in range(len(tmp)):
            if nntext[x:x+5]==tmp[y][1]:
                nnntext+=tmp[y][0]
                break
print(ntext)
for x in range(len(ntext)):
    if seed[x]==ntext[x]:
        nntext+="0"
    else:
        nntext+="1"

for x in range(0,len(ntext),5):
    for y in range(len(tmp)):
        if nntext[x:x+5]==tmp[y][1]:
            nnntext+=tmp[y][0]
            break

print("Key:"+seed)
print("Plain Text:"+text)
print("Plain Text:"+ntext)
print("Cipher Text:"+nnntext)
print("Cipher Text:"+nntext)
