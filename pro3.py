st1,st2=input().split()
char=abs(len(st2)-len(st1))
for i in range(len(st1)):
  if(len(st2)==1 and st2[i] in st1):
    break
  if(st1[i]!=st2[i]):
    char=char+1
print(char)
