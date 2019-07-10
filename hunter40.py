#anand
n=int(input())
sum=0
for i in n:
    sum+=i
if(str(sum)==str(sum)[::-1]):
    print("YES")
else:
    print("NO")
