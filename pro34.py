n1,n2=map(int,input().split())
c=0
li=[]
for i in range(n1):
      li.append(input())
for i in range(n1):
      for j in range(n2-1):
            if(li[i][j]!='R' and li[i][j+1]!='R'):
                  c+=3
            elif(li[i][j]!='G' and li[i][j+1]!='G'):
                  c+=5
print(c)
