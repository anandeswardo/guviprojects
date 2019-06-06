#anand
n1,n2=map(int,input().split())
q=n1*n2
m=[]
for i in range(1,q+1):
    if i%n1==0 and i%n2==0:
        m.append(i)
print(min(m))
