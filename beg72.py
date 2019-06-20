st=input()
vowel=["a","e","i","o","u"]
for i in range(0,len(st)):
    if(st[i] in vowel):
        print("yes")
        break
else:
    print("no")
    
