num=input()
count=0
for i in range (len(num)):
    if(num[i].isdigit()!=True):
        count+=1
    else:
        continue
if(count==0):
    print("yes")
else:
    print("no")
