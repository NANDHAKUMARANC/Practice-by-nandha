n=int(input("Enter the number: "))
fact=1
if n<1:
    print("Negative integer")
elif n==0:
    print("the factorial number of 0 is 1")
else:
    for i in range(1,n+1):
        fact=fact*i
    print(fact) 