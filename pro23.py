#anand
str=input()
list=["GLGLGL","GRRG","GLLG","GRGRGR"]
count=0
for i in range(0,len(list)):
    if list[i] in str:
        count+=1
if count==1:
    print("yes")
else:
    print("no")
