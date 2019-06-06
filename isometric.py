#anand
str1,str2=list(map(str,input().split()))
set1=len(set(str1)) 
set2=len(set(str2))
if(set1==set2):
    print ("yes") 
else:
    print ("no")
