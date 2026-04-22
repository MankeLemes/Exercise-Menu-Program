def exercise1():
    number_1 = int(input("Type the number 1: "))
    number_2 = int(input("Type the number 2: "))

    if number_1 > number_2:
        print(f"The higher number between {number_1} and {number_2} is: {number_1}")
    elif number_2 > number_1:
        print(f"The higher number between {number_1} and {number_2} is: {number_2}")
    else:
        print("Both numbers are equal.")


def exercise2():
    number = int(input("Type any number: "))

    if number > 0:
        print(f"The number {number} is positive!")
    elif number < 0:
        print(f"The number {number} is negative!")
    else:
        print(f"The number {number} is zero!")


def exercise3():
    user_gender = input("What's your gender? (M/F): ").upper()

    if user_gender == 'M':
        print("You are male!")
    elif user_gender == 'F':
        print("You are female!")
    else:
        print("Gender not identified!")


def exercise4():
    letter = input("Type a letter: ").upper()

    if letter in "AEIOU":
        print("It's a vowel!")
    elif letter.isalpha():
        print("It's a consonant!")
    else:
        print("That's not a letter!")


def exercise5():
    student_name = input("What's your name? ")

    note_1 = float(input("First grade: "))
    note_2 = float(input("Second grade: "))
    note_3 = float(input("Third grade: "))

    average = (note_1 + note_2 + note_3) / 3

    if average >= 7:
        print(f"{student_name}, congratulations! Your average is high: {average:.2f}")
    elif 5 <= average < 7:
        print(f"{student_name}, your average is okay: {average:.2f}")
    else:
        print(f"{student_name}, your average is low. It's an opportunity to improve!")


# 🔥 MENU LOOP
while True:
    print("\n===== MENU =====")
    print("1 - Exercise 1")
    print("2 - Exercise 2")
    print("3 - Exercise 3")
    print("4 - Exercise 4")
    print("5 - Exercise 5")
    print("0 - Exit")

    option = input("Choose an option: ")

    if option == "1":
        exercise1()
    elif option == "2":
        exercise2()
    elif option == "3":
        exercise3()
    elif option == "4":
        exercise4()
    elif option == "5":
        exercise5()
    elif option == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid option! Try again.")