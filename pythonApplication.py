#First commit line#
import random
print("Welcome to this Python Application")
print("What do you want this application to do?")
print("1. Add two numbers")
print("2. Print a random number")
print("3. Print a random word")
print("4. Multiply two numbers")

input = input("Enter your choice: ")

match input:
    case "1":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"The sum of {num1} and {num2} is {num1 + num2}")
    case "2":
        print("Random number: " + random.randint(0, 100))
    case "3":
        print("Random word: " + random.choice(["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]))
    case "4":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"The product of {num1} and {num2} is {num1 * num2}")
    case _:
        print("Invalid choice")