verb1 = ""
verb2 = ""
noun = ""
number = 0
celebrity_guest = ""

verb1 = input("Enter your first verb: ")
verb2 = input("Enter your second verb: ")
noun = input("Enter your first noun: ")
celebrity_guest = input("Enter the name of a celebrity: ")

while True:
    number = input("Enter a positive integer: ")
    if number.isdigit() and int(number) > 0:
        number = int(number)
        break
    print("That's not a positive integer!")

madlib = (f"Once upon a time, there was a person named {celebrity_guest}. "
          f"This person decided to {verb1} on a {noun}. "
          f"Because of this, they also decided to {verb2} until it turned dark. "
          f"The summary of the person's actions resulted in the gaining of {number} coins. ")


print(madlib)