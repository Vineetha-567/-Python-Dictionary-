sting=input("enter string:")
word=sting.split()
d={}
for str in word:
    ch=str[0]
    if ch not in d:
        d[ch]=[]
    d[ch].append(str)
print(d)
for k,v in d.items():
    print(k,";",v)
