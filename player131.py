num=input()
su=0
for i in num:
    if(int(i)%2!=0):
        su+=int(i)
if(su%2==0):
    print("E")
else:
    print("O")
