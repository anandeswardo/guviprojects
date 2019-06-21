st=input()
st=st.replace(" ","")
for i in st:
    if(st.count(i)==1):
        print(i,end=" ")
