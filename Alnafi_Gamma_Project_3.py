"""
Exercise 1 (and Solution)
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many
copies of the previous message. (Hint: order of operations exists in Python) Print out that many
copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the
ENTER button)fggf
"""
current_year = int(input("Enter The current Year: "))
name = input("Enter your name: ")
current_age = int(input("Enter your age: "))
Age_in_hundred = (current_year - current_age)+100
print(f"{name} You will be hundred years old in {Age_in_hundred} ")
# add previous programme
No_of_copies = int(input("Enter a number of copies you want to print: "))
print(f"{name} You will be hundred years old in {Age_in_hundred} \n " * No_of_copies)

