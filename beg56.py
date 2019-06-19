str=input()
a=False
b=False
for i in str:
    if(i.isdigit()==True):
        b=True
    if(i.isalpha()==True):
        a=True
if(a and b):
    print("Yes")
else:
    print("No")
