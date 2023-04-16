a = int(input("Enter number: "))
b = int(input("enter number: "))
result = 0
try:
    result = a / b

except ZeroDivisionError:
    print("Could not divide by zero")
except BaseException as e:
    print("Something went wrong")
    print(e.args)
print(result)
print("shmulik")
