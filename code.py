input_string=str(input("input Your string ").strip())
lst=[]
for i in range(len(input_string)):
    if input_string[i] not in lst:
        lst.append(input_string[i])
    else:
         continue 
min=len(input_string)+1            
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
        if temp<min:
            min=temp
print(min+1)
