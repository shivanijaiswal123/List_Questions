Money = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
count=0
count2=0
count3=0
while(i<len(Money)):
    if(Money[i]>10000000):
        count=count+1
    elif(Money[i]>100000):
        count2=count2+1
    else:
        count3=count3+1
    i=i+1
print(count,"crorepati hai")
print(count2,"lakhpati hai")
print(count3,"dilwale hai")