# If first number is divisible by the second the number print true else false

"""step 1 : get the values a and b from the user
step 2 : using if condition a modulo of b and it statisfy means true
step 3 : else false and print the output"""

a=float(input("Enter the first number : "))
b=float(input("Enter the first number : "))
if a%b==0:
    print(True)
else:
    print(False)