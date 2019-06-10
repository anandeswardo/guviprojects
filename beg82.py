import decimal
n1,n2=map(float,input().split())
c=n1*n2
d=(decimal.Decimal(c))
print(round(d,5))
