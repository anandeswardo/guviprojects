st1,st2=map(str,input().split())
a=0
if len(st1)>len(st2):
   st1,st2=st2,st1
b=0
while s<len(st1):
   a+=(ord(st2[b])-ord(st1[b]))
   b+=1
for b in range(b,len(st2)):
   a+=ord(st2[b])-ord('a')+1
print(a)
