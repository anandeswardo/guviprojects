n1,m1=map(int,input().split())
a=1
for i in range(1,100):
      if(pow(m1,i)==n1):
        print("yes")
        a=0
        break
if(a==1):
    print("no")
