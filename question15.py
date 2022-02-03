#marge 2dictionarys
x={"a":1,"b":2,"c":3,"d":5}
y={"b":4,"c":6,"d":8}
for i in x:
    z=x.update(y)
print(x)