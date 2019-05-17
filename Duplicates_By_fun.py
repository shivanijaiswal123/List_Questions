def duplicate(list):
    n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
    i=0
    new_list=[]
    while i<len(n):
        j=i+1
        count=0
        while j<len(n):
           
            if n[i]==n[j]:
                if n[i] not in new_list:
                    new_list.append(n[i])
        
            j=j+1
        i=i+1
    return new_list

Duplicates=duplicate([19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11])
print(Duplicates)