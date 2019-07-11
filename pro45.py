n=input()
if(n==n[::-1]):
    print("yes")
else:
    n2=n.strip("0")
    if n2==n2[::-1]:
        print("yes")
    else:
        print("no")
