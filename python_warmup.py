# # taking input
# name = input("Enter your name:- ")
# print(name)

# Taking list elements one by one
'''
marks = []

while True:
    print("Enter Marks:-")
    a = int(input())
    marks.append(a)
    dec = input('finished? (y/n)')
    if dec == 'y':
        break
print(marks)

'''

# # Using map() and list()

# lst = list(map(int, input("Enter elements sep by space ").split()))
# print(lst)


# # Print with custom separator and end
# print("Hello! ", end="")
# print("my name is john")


# Import the whole module

import math as mt

square_rt = mt.sqrt(7)
print(square_rt)
fact = mt.factorial(5)
print(fact)