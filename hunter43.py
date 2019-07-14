st=input()
a=''
for i in range(0,len(st)-1,2):
  if(int(st[i+1])%2==0):
    a+=st[i]*int(st[i+1])
  else:
    a+=st[i]+st[i+1]
print(a)
