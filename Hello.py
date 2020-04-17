def neg_list (l):
    nagative = []
    for i in l:
        nagative.append(-i)
    return nagative
pos_list = list(range(1,11))
print(f"The list is {neg_list(pos_list)}")