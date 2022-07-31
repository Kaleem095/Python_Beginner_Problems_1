birth_days = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4', 'Sana': 'Sep 12'}
while True:
    print("Enter a name: (Keep blank to quit and press enter) ")
    name = input()
    if name == '':
        break

    if name in birth_days:
        print(birth_days[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information ' + name)
        print("What is their birthday? ")
        bday = input()
        birth_days[name] = bday
        print("Birthday database is updated. ")