# import sys
# print(sys.path)
print("In calculator.py")


def add(x, y):
    return x + y


def subtract(x, y):
    pass


def multiplication(x, y):
    pass


def divide(x, y):
    pass


sum = add(5, 9)


def greet(greeting, msg="How are you?", name="World"):
    msg = f"{greeting} {name}. {msg}"
    print(msg)
    return msg


# not discussed yet
def student_info(arg1, *args, **kwargs):
    print(arg1)
    print(args)
    print(kwargs)
    # for arg in args:
    #     print(arg)
    # for key, value in kwargs.items():
    #     print(key, value)


greetings = greet("Hi", "Universe")  # Hi World. Universe
print("greetings: ", greetings)
greetings = greet("Hi", name="Universe")  # Hi Universe. How are you?
print("greetings: ", greetings)


# student_info('English', 'Bangla', 'Physics', 'Math', name='Andy', age=25)

# Example of unpacking
# courses = ["Bangla", "Physics", "Math"]
# info = {"name": "Andy", "age": 25}
# print(info)
# student_info("First Argument", courses, info)
# print()
# student_info("First Argument", *courses, **info)

print(__name__)
