s1,s2=list(map(str,input().split()))
for i in range(0,len(s1)+1):
    for j in range(len(s2)):
        continue
    if(s2[j]==s1[i]):
        print(i+1)
        break
    
