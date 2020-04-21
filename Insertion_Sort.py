li = [1,8,5,3,2]

for i in range(1,len(li)):
    for j in range(i):
        if li[i] < li[j]:
            li.insert(j,li.pop(i))
            print(li)
        else:
            print("X",li)
