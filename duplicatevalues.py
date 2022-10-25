list=[4,45,6,3,1,4,5,6,7,8]
duplicate=[]
for i in list:
    if i not in duplicate:
        duplicate.append(i)
print(duplicate)
