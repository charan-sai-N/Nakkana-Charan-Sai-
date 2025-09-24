list1=[1,2,3,4,5,6,7,8,9]
list2=[1,2,8,9,12,46,76,82,15,20,30]
dict1={}
for i in list1:
    count = 0
    for j in list2:
        if j % i == 0:
            count = count + 1
    dict1[i] = count
print(dict1)
#Output = {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}       
                

