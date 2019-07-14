n1=int(input())
li1=[int(i) for i in input().split()]
a=0
for i in range(1,n1-1):
    if(li1[i]<li1[i-1] and li1[i]<li1[i+1]):
        a+=1
    elif(li1[i]>li1[i-1] and li1[i]>li1[i+1]):
        a+=1
print(a)
