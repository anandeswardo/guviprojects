#anand
str=list(input())
for i in range(0,len(str),2):
    str[i],str[i+1]=str[i+1],str[i]
print("".join(str))
