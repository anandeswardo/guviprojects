#anand
num=int(input())
list1=[int(i) for i in input().split()]
list2=[]
for i in list1:
  if(list1.count(i)>1):
    list2.append(i)
c=set(list2)
if(len(c)==0):
  print('unique')
else:
  print(*c)
