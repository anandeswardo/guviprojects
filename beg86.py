str=input().split()
for i in str:
    s=set(i)
    if(len(s) == len(i)):
        print("Yes")
    else:
        print("No")
