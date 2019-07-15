li1=list(map(int,input().split()))
li2=list(map(int,input().split()))
li3=li2[0:li1[0]]
li4=li2[li1[0]:li1[0]+li1[1]]
for i in li4:
  if(li3.count(i)>=1):
    print(i,end=' ')
