n1,n2=map(int, input().split())
for mr in range(n1+1,n2):
   if mr > 1:
       for i in range(2,mr):
           if (mr % i) == 0:
               break
       else:
           print(mr,end=' ')
