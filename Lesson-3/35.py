# my_file = open("my_file.txt")
# for line in my_file.readlines():
#     print(line, end='')


def save_name_to_file():
    name = input("what is your name?: ").capitalize()

    with open("names.txt", "a") as names_file:
        names_file.write(name + "\n")
        names_file.close()


save_name_to_file()


def greet_person():
    with open("names.txt") as names_file:
        for line in names_file.readlines():
            print("Hello " + line, end='')
        names_file.close()


greet_person()
