# pseudocode for question 3:

"""
steps:

1. first declare a list with some elements .
2. create a empty list.
3. I used "for" loop for getting a elements from a list.
4. And I used if statement to control the flow of the program execution. Here I check if the elements in list is greater than 10 or equal to 10
5. If elements in list is greater than or equal to 10 it should go back to the condition repeatedly and it should not show any error in if statement so we used pass keyword.
6. if the condition not satisfy it should append the element in that empty list and print that result using print keyword.

"""

list =[1,12,4,5,8,9,10,21,33,7]
g = []
for i in list:
    if i == 10 or i > 10:
        pass
    else:
        g.append(i)
print(g)