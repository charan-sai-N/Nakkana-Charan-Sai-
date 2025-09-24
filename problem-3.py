a=int(input("enter 'a' value: "))
if a % 2 == 0:
    a = a-1
else:
    pass
for i in range(1 ,2*a ,2 ):
    print(i,end=" ")
# if a=6 then Output = 1 3 5 7 9 