input_string=str(input("input Your string").strip())
lst=[]
for i in range(len(input_string)):
    if input_string[i] not in lst:
        lst.append(input_string[i])
    else:
         continue 
minima=9999
for i in range(len(input_string)):
    lst2=[]+lst[:]
    k=-1
    for j in range(i,len(input_string)):
        if input_string[j] in lst2:
            lst2.remove(input_string[j])
        if lst2==[]:
            k=j
            break
    if k!=-1:
        temp=k-i
        if temp<minima:
            minima=temp
print(minima+1)

