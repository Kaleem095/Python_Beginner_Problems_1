"""
List Less Than Ten
Take a list, say for example this one:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.
Extras:
1.Instead of printing the elements one by one, make a new list that has all the
elements less than 5 from this list in it and print out this new list.
2.Write this in one line of Python using loop.
3.Ask the user for a number and return a list that contains only elements from the
original list a that are smaller than that number given by the user.

"""
# my_list = [1, 4, 9, 2, 3, 5, 8, 13, 21,7, 34, 55, 6, 89, 10]
# for number in my_list:
#     if number < 5:
#         my_list.sort()
#         print(number)

# Instead of printing the elements one by one, make a new list that has all the
# elements less than 5 from this list in it and print out this new list.
mylist = range(1, 20)
New_list = []
newList = []
for number in mylist:
    if number < 5:
        New_list.append(number)
        New_list.sort()
print(New_list)
print()
#
get_number = int(input("Enter any number to check list! "))
for number in mylist:
    if number < get_number:
        newList.append(number)
        newList.sort()
print(newList)
# in one line using loop
# print([x for x in mylist if x < 5])
