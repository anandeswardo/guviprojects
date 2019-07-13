n1,n2=map(int,input().split())
li=list(map(int,input().split()))
a=int(input())
b=(sum(li)-li[n2])//2
if(a==b):
  print("Bon Appetit")
else:
  print(a-b)
