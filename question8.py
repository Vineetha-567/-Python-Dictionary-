a="w3resource"
k={}
count={}
for key in a:
    if key in count:
        count[key]+=1
    else:
        count[key]=1
for key in count:
    if count[key]>=1:
        k[key]=count[key]
print(k)