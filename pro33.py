str=input()
j=0
for i in range(len(str)):
    if(str[j]<str[i]):
        print(str[i:])
        break
