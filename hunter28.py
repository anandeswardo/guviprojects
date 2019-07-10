#anand
st=input()
ch=""
for i in st:
    if i not in ch:
        ch+=i
print(ch,end="")
