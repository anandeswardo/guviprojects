#anand
num=int(input())
list1=[int(i) for i in input().split()]
for i in list1:
  if(list1.count(i)==1):
      print(i)
