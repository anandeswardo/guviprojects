n1=int(input())
n2=bin(n1)[2:]
n2=n2[::-1]
for i in range(len(n2)):
    if(n2[i]=='1'):
        print(i+1)
        break
