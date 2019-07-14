st1="WELCOMETOGUVICORPORATIONS"
st=input()
li=[]
for i in range(5):
    li.append(list(st1[i*5:(i*5)+5]))
st2="".join(["".join(x) for x in [[arr[i][j] for i in range(5)] for j in range(5)]])
for i in range(len(st1)):
    if(st1[i:i+len(st)]==st):
        print(i//5,i%5)
        print((i+len(st)-1)//5,(i+len(st)-1)%5)
        break
    if(st2[i:i+len(st)]==st):
        print(i%5, i//5)
        print((i+len(st)-1)%5, (i+len(st)-1)//5)
        break
else: 
    print(0)
