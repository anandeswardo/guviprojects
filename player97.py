n1,n2=map(int,input().split())
a=1
b=0
for i in range(n1,n2+1):
    if(a%2!=0): 
        b=b+i
        a=a+1
print(b)
