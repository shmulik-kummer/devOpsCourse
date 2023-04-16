# A
# 1 - Create two variables name X and Y.
x = 6
y = 8

# 2 - Print “BIG” if X is bigger than Y
if x > y:
    print("BIG")
# 3 - Print “small” if X is smaller than Y.
elif x < y:
    print("small")
else:
    print("x and y are equals")

# B
# 1 - Run a “for” loop 5 times.
for i in range(5):
    # 2 - print iteration number every time
    print(i)

# C
# 1 - Create a variable and initialize it with a number 1-4.
season_number = 2
# 2 - Create 4 conditions (if-elif) which will check the variable.
# 3 - print the season name accordingly
if season_number == 1:
    print("summer")
elif season_number == 2:
    print("winter")
elif season_number == 3:
    print("fall")
elif season_number == 4:
    print("spring")
else:
    print("unknown")

# D
# 1 - how many times will the following loop run?
# 10 times
# 2 - what will be printed last
# number 10
count = 1
while count < 11:
    print(count)
    count = count + 1

# E
# Write a program with variables holding the following:
# 1. Your age.
age = 39
# 2. First letter of your last name.
lname_first_letter = "k"
# 3. Current shekels-dollar currency.
shekel_dollar_curr = 3.62
# 4. Did you flew abroad (true/false)
is_flew_abroad = True
# 5. Your apartment number.
appt_number = 14

# Print all variables.
print(age)
print(lname_first_letter)
print(shekel_dollar_curr)
print(is_flew_abroad)
print(appt_number)

# Add the currency to your age, and check the result.
print(age + shekel_dollar_curr)

# F
# Create a program which uses input with the following:
# 1. Ask user for his phone number
# 2. Print the words “phone number” and the phone number the user entered.

phone_number = input("Please type your phone number: ")
print(f"Phone number is: {phone_number}")


# G
# Write a program with the following:

# 1. Method named printHello() that prints the word “hello”.
def printHello():
    print("hello")


# 2. Method named calculate() which adds 5+3.2 and prints the
# result.
def calculate():
    x = 5 + 3.2
    print(x)


# H.
# Write a program with the following:
# 1. Method that receive your name and prints it.
def print_name(name):
    print(name)


# 2. Method that receive a number, divide it by 2, and prints the
# result.
def divide_num_by_2(num):
    print(num / 2)


# I.
# Write a program with the following:
# 1. Method that receive two numbers, add them, and return the
# sum.
def add_numbers(num1: int, num2: int):
    return num1 + num2


# 2. Method that receive two Strings, add space between them,
# and return one spaced string.
def add_space_to_Strings(str1: str, str2: str):
    return str1 + " " + str2


print(add_space_to_Strings("hello", "world"))

# K
# Create a nested for loop (loop inside another loop) to create
# a pyramid shape:

for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end="")
    print()

#
# Create a nested for loop to create X shape (width is 7,
# length is 7):
for i in range(7):
    for j in range(7):
        if i == j or i == 6 - j:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# M.
# Write a program with the following:
# 1. Method that gets a number from the user (using input).
def get_num_from_user():
    number = int(input("Please enter a number: "))
    return number


# 2. Method that receive the number from the first method, and
# computes the sum of the digits the integer (e.g. 25 = 7, 2+5=7)

def compute_sum_of_digits(num):
    digits = [int(digit) for digit in str(num)]
    return sum(digits)