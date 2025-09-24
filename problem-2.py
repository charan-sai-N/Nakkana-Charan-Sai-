a=int(input("enter 'a' value: "))
for i in range(1, 2*a, 2):
    print(i,end=",")

           #or
a=int(input("enter 'a' value: "))
for i in range(1, 2*a):
    if i % 2 != 0:
        print(i,end=",")

#Output= 1,3,5,7