#anand
string=input()
count=0
for i in string:
    if(string.count(i)>count):
        count=string.count(i)
        s=i
print(s)
