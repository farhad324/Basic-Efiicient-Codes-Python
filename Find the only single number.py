numlist=[2,2,1]
single = numlist[0]
for i in range(1, len(numlist)):
    single = single ^ numlist[i]
print(single)