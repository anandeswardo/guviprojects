#anand
n=int(input())
str=input()
for i in range (-1,-n-1,-1):
    if not(str[i]=="a" or str[i]=="e" or str[i]=="i" or str[i]=="o" or str[i]=="u" or str[i]=="A" or str[i]=="E" or str[i]=="I" or str[i]=="O" or str[i]=="U"):
        print(str[i],end="")
