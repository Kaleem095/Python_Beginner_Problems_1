"""Odd Or Even
input if types int equality comparison numbers mod

Again, the exercise comes first (with a few extras if you
want the extra challenge or want to spend more time), followed
by a discussion. Enjoy!

"""

"""
Exercise 2 (and Solution)
Ask the user for a number. Depending on whether the number is even or 
odd, print out an appropriate message to the user. Hint: how does an even / odd 
number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number 
to divide by (check). If check divides evenly into num, tell that to the user. 
If not, print a different appropriate message.
"""
# --------------Code Start from Here--------------------
number = int(input("Enter the number: "))
if number % 4 == 0 and number != 0:
    print(f"The number {number} is even and multiple of 4. ")
elif number % 2 == 0 and number != 0:
    print(f"The given number {number} is an Even. ")
elif number % 2 != 0:
    print(f"The given number {number} is Odd number. ")
else:
    print("Wrong input your entered zero")
num = int(input("Enter the to check: "))
check = int(input("Enter the number to divide by num "))
if num % check == 0:
    print(f"The number {num} is evenly divide by check {check} ")
else:
    print(f"The number {num} is not evenly divide by the {check} number")

