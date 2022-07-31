"""
Create a program that asks the user for a number and then
prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that
divides evenly into another number. For example, 13 is a divisor
 of 26 because 26 / 13 has no remainder.)
"""
# first method
number = int(input("Enter a number "))
My_list = range(1, 20)
new_list = []
for num in My_list:
    if number % num == 0:
        new_list.append(num)
print(new_list)


# @second Method

# num1 = int(input("Please Enter a number to Divide "))
# My_new_list = list(range(1, num1+1))
# divisor_list = []
# for num2 in My_new_list:
#     if num1 % num2 == 0:
#         divisor_list.append(num2)
# print(divisor_list)


