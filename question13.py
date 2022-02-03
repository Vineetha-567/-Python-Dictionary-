dict={"a":50,"b":58,"c":56,"d":40,"e":100}
max1=0
max2=0
max3=0
for i in dict:
    for j in dict:
        if dict[i]>max1:
            max1=dict[i]
            temp1=i
        elif max1>dict[j] and max2<dict[j]:
            max2=dict[j]
            temp2=j
        elif max2>dict[j] and max3<dict[j]:
            max3=dict[j]
            temp3=j
print("maxi1:",temp1,max1)
print("max2",temp2,max2)
print("max3",temp3,max3)