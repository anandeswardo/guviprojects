a,b=[int(i) for i in input().split()]
c,d=[int(i) for i in input().split()]
e,f=[int(i) for i in input().split()]
if a==c==e:
    print("yes")
elif b==d==f:
    print("yes")
elif a==b and c==d and e==f:
    print("yes")
else:
    print("no")
