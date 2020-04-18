def cuont_list(listey):
    count = 0
    for i in listey:
        if type(i) == list:
            count += 1
    return count
listey = [1,2,3,4,[5,6,7,8],9,[10],[12,13],[14]]
print(f"listey have {cuont_list(listey)} lists")