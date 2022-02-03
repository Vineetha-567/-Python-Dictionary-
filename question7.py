d1={"a":100,"b":200,"c":400}
d2={"a":300,"b":200,"c":400}
#print(sum(d1.values()))
#print(sum(d2.values()))
for key in d2:
    if  key in d1:
        d2[key]=d2[key]+d1[key]
    else:
        print("none")
print(d2)