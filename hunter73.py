st1=input("")
st2=input("")
a=""
for i in range(len(st1)):
    for j in range(len(st1),-1,-1):
        if(st1[i:j] in st2):
            if(len(st1[i:j])>=len(a)):
                a=st1[i:j]
print(a)
