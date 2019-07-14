n=int(input())
li1=list(map(int,input().split()))
li2=[]
a=(li1.index(min(li1))+1)
b=(li1.index(max(li1))+1)  
li2.append(a)  
li2.append(b)
print(*li2)
