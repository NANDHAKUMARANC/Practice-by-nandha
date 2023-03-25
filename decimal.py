n=int(input("Enter the decimal value: "))
binary=[]
while(n>0):
    if n%2==0:
        binary.append(0)
    else:
        binary.append(1)
    n=n//2
binary=binary[::-1]
print(binary)