d={1:2,3:4,4:3,2:1,0:0}
l=list(d.values())
l.sort()
r=l.copy()
r.reverse()

a={}
for i in l:
    for j in d:
        if i==d[j]:
            a[j]=i
print("assending:",a)
e={}
for i in r:
    for j in d:
        if i==d[j]:
            e[j]=i
print("desending",e)