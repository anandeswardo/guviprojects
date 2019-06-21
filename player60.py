s1,s2=list(map(str,input().split()))
for i in range(len(s1)):
    if(s1[i] in s2):
        print("yes")
        break
else:
    print("no")
