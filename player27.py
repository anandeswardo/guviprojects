#anand
str=input()
for i in range(0,len(str)):
    if(str[i].islower()==True):
        print(str[i].upper(),end="")
    elif(str[i].isupper()==True):
        print(str[i].lower(),end="")
