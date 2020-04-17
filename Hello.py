def common(l1,l2):
    dummy = []
    for i in l1:
        if i in l2:
           dummy.append(i)
    return dummy 
list_1 = [1,2,3,4,5,6,7,8,9]
list_2 = [2,4,6,8]
print(f"The common in the list is {common(list_1,list_2)}")