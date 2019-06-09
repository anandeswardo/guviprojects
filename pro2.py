from itertools import combinations
str1,num1=map(int,input().split())
num2=len(str(str1))
x=list(combinations(str(str1),num2-num1))
x=(sorted(x))
y="".join(x[0])
print(y)
