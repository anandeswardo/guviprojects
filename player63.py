n1=int(input())
li1=[int(i) for i in input().split()]
li2=[int(i) for i in input().split()]
for i in range(0,len(li1)):
    for j in range(0,len(li2)):
        if(li1[i]==li2[j]):
            print(li1[i],end=" ")
            break
