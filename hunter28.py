#anand
st=input()
li=[]
for i in st:
    if i not in li:
        li.append(i)
print(*li,end="")
