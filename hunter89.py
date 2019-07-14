st1=input()
st2=''
for i in st1:
    if(i not in st2):
        st2+=i 
print(st2[::-1])
