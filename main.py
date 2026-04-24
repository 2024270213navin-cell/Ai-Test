import os,sys,json   # multiple imports on one line (style issue)

SECRET_KEY = "hardcoded_secret_12345sdfghj"  # security issue

global_var = []

def processData(data):   # camelCase instead of snake_case
    print("Processing data...")  # unnecessary print

    if data == None:  # should use 'is None'
        return

    for i in range(0, len(data)):
        try:
            value = int(data[i])
        except:
            value = 0   # bare except (bad practice)

        if value > 10:
            global global_var
            global_var.append(value)   # global mutation

    return global_var


def insecure_login(username, password):
    if username == "admin" and password == "password123":  # hardcoded creds
        return True
    return False


def read_file(filepath):
    f = open(filepath, "r")  # no context manager
    content = f.read()
    return content  # file never closed


def write_file(filepath, data):
    try:
        f = open(filepath, "w")
        f.write(data)
    except Exception as e:
        print(e)
    # missing close()


def divide(a, b):
    return a / b  # no zero division handling


class user:  # class name should be PascalCase
    def __init__(self, name, password):
        self.name = name
        self.password = password  # storing raw password

    def check_password(self, input_pwd):
        if self.password == input_pwd:  # no hashing
            return True
        return False


def duplicate_code(x):
    if x > 0:
        print("Positive")
    elif x == 0:
        print("Zero")
    else:
        print("Negative")

def duplicate_code_again(x):  # duplicate logic
    if x > 0:
        print("Positive")
    elif x == 0:
        print("Zero")
    else:
        print("Negative")


def long_function():
    # overly long function doing multiple unrelated things
    data = ["1", "2", "abc", "50"]

    results = processData(data)

    for r in results:
        print("Result:", r)

    user_obj = user("admin", "password123")

    if user_obj.check_password("password123"):
        print("Logged in")

    content = read_file("test.txt")
    print(content)

    write_file("output.txt", content)

    print(divide(10, 0))  # crash


if __name__ == "__main__":
    long_function()
