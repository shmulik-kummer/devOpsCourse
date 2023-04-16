def get_age():
    age = int(input("enter your age: "))
    if age < 0:
        raise BaseException("age can't be negative", age)


try:
    get_age()
except BaseException as e:
    print(e.args)
