import math

print("Hellow World from func_def __name__:", __name__)


def learn_loops(isLearning):
    if not isLearning:
        return
    for i in range(10):  # for(int i=0;i<=10;i++){.....}
        if i == 5:
            print("breaking loop at five")
            break
        if i == 3:
            print("skipping three")
            continue
        print(i)

    print("\nLearning while loop")
    i = 0
    while i < 6:
        i += 1
        if i == 4:  # There's no switch in Python
            print("in i==4")
        elif i > 2:
            print("in i > 2")  # jump back to while
        # i += 1 # infinite loop at 2 if increment is here
        else:
            print(i)
    else:
        print("i is no longer less than 6")


def learn_if_elif_else(isLearning):
    if not isLearning:
        return

    while True:
        user_input = input("Enter a number (or 'q' to quit): ")
        if user_input == "q":
            print("Exiting infinite loop...q")
            break
        else:
            num = float(user_input)
            if num >= 0:
                if num == 0:
                    print("Zero")
                elif num > 0 and num <= 10:
                    print("In the range 1 to 10")
                else:
                    print("Positive number")
            else:
                print("Negative number")


def learn_dictionary_func(isLearning):
    if not isLearning:
        return

    student = {
        1: "one",
        "name": "Andy",
        "age": 12,
        "courses": ["Bangla", "English", "Math", "Physics"],
    }
    print(student)
    print(
        f"{student['name']} is {student['age']} years old. He's studying {student['courses']}"
    )
    # print(student["phone"])
    print(
        f"{student.get('name')} is {student.get('age')} years old. He's studying {student.get('courses')}. His mobile no is {student.get('phone')} or {student.get('phone', 'UNKNOWN')}"
    )

    student["phone"] = "0404040404"  # add key-value
    print(student)

    student["name"] = "Bridget"  # update value
    print(student)

    new_info = {"name": "Charlie", "enrolled": True}
    student.update(new_info)
    print(student)

    # del student[1]
    # print(student)
    popped_info = student.pop(1)  # key 1
    print(popped_info, ": ", student)

    print(len(student))

    print(student.keys())

    print(student.values())

    print(student.items())

    for key in student:
        print(key)

    for key, value in student.items():
        print(key, ": ", value)


def learn_list_tuple_set_func(learn):
    """ learning List, Tuple, and Set"""
    if not learn:
        print("skipping learn_list_tuple_set_func funcion")
        return
    fruits = ["apple", "banana", "cherry", "dates"]
    print(fruits)
    print(len(fruits))
    print("{0}, {1}".format(fruits[0], fruits[3]))  # 0 = apple, 3 = dates
    print("{0[0]}, {0[3]}".format(fruits))  # 0 = apple, 3 = dates
    print(f"{fruits[0]}, {fruits[3]}")  # 0 = apple, 3 = dates
    print(
        f"I like {fruits[-1]} and {fruits[-3]}"
    )  # - means opposite direction and 0 = apple; -1 is always the end of the list
    print(fruits[0:2])  # 0, 1
    print(fruits[:2])  # empty before : => start of the list
    print(fruits[2:3])  # 2
    print(fruits[2:])  # 2,..., end; empty after : => end of the list

    fruits.append("fig")  # append 'fig' at the end - "in-place"
    print(fruits)

    fruits.insert(0, "fig")  # insert 'fig' at location=0 - "in-place"
    print(fruits)

    fruits.insert(3, "fig")
    print(fruits)

    new_fruits = ["fig", "grapes"]
    print(new_fruits)
    print(*new_fruits)  # easy way to convert to string

    fruits.append(new_fruits)
    print(fruits)

    fruits.insert(3, new_fruits)
    print(fruits)

    fruits.extend(new_fruits)  # a
    print(fruits)

    fruits.remove("apple")  # removes apple in-place
    print(fruits)

    popped_fruit = fruits.pop()  # returns last item in-place
    print(popped_fruit)
    print(fruits)

    fruits = ["apple", "banana", "cherry", "dates"]
    fruits.reverse()  # in-place modification
    print(fruits)
    fruits.sort()  # in-place
    print(fruits)
    fruits.sort(reverse=True)  # in-place
    print(fruits)
    print(sorted(fruits), " - ", fruits)  # sorted() is not in-place

    print(fruits.index("cherry"))
    print("cherry" in fruits)  # membership test

    # print(fruits.index("grapes"))  # generates error
    print("grapes" in fruits)  # safe

    for fruit in fruits:
        print(fruit)

    for index, fruit in enumerate(fruits):
        print(index, ": ", fruit)

    for index, fruit in enumerate(fruits, start=123):
        print(index, ": ", fruit)

    fruits_str = ", ".join(fruits)
    print(fruits_str)
    fruits_str = "{}, fig".format(fruits_str)
    print(fruits_str)
    fruits_2 = fruits_str.split(", ")
    print(fruits_2)

    numbers = [1, 5, 18, 1999, 2020, 7, 23, 66]
    #          0  1  2     3     4   5   6   7
    #         -8 -7  -6    -5   -4   -3  -2  -1
    #         first                         last
    # for forward (+step): start=0, end=end
    # for reverse (-step): start=last, end=0
    # step1: identify direction, step2: identify start and end,
    # step3: identify step
    print(numbers[:])  # list[start:end:step=default 1]
    print(numbers[::-1])  # reverse_start=66:end=1:step=1
    print(numbers[1:6:2])  # forward_start=1:end=5:step=2 i.e. [5, 1999, 7]
    print(numbers[:-2:2])  # [1, 18, 2020]
    print(numbers[1:6:-1])  # reverse_start=1:end=5:step=1 i.e.not continuous=>[]
    print(numbers[1::-1])  # reverse_start=1:end=first:reverse step=1 i.e. [5, 1]
    print(numbers[-1:-5:-1])  # start=last:end=-4:step=1
    print(numbers[-1:-5:1])  # start=last:end=-4:step=1 but not continuous, so []
    print(numbers[-3::-1])  # start=-3:end=first:step=1 i.e. [7, 2020, 1999, 18, 5, 1]
    print(numbers[-3::1])  # start=-3:end=last:step=1 i.e. [7, 23, 66]

    str = "abcdefghijklmnopqrstuvwxyz"
    # all items in the array, reversed
    print(str[::-1])  # start=last:end=first:step1 i.e. zyxwvutsrqponmlkjihgfedcba
    # the first two items, reversed
    print(str[1::-1])  # start=1: end=first: step=1 i.e. ba
    # the last two items, reversed
    print(str[:-3:-1])  # reverse_start=last:end:-2:step=1 i.e. zy
    # everything except the last two items, reversed
    print(str[-3::-1])  # reverse_start=-3:end:first:step1 i.e. xwvutsrqponmlkjihgfedcba

    print(min(numbers))
    print(max(numbers))
    print(sum(numbers))

    fruits_copy = fruits  # List is MUTABLE
    print(id(fruits), ": ", fruits)
    print(id(fruits_copy), ": ", fruits_copy)
    print(fruits == fruits_copy)  # == checks value
    print(fruits is fruits_copy)  # is checks memory location
    fruits_copy[3] = "figs"
    print(id(fruits), ": ", fruits)
    print(id(fruits_copy), ": ", fruits_copy)

    fruits = ["apple", "banana", "cherry", "dates"]
    fruits_copy = ["apple", "banana", "cherry", "dates"]
    print(id(fruits), ": ", fruits)
    print(id(fruits_copy), ": ", fruits_copy)
    print(fruits == fruits_copy)
    print(fruits is fruits_copy)
    fruits_copy[3] = "figs"
    print(id(fruits), ": ", fruits)
    print(id(fruits_copy), ": ", fruits_copy)

    # list + access + modify => use list
    # list + access => use tuple (no modification, so not much methods)
    tup_fruits = ("apple", "banana", "cherry", "dates")  # Tuple is IMMUTABLE
    print(tup_fruits)

    # tup_fruits[2] = "fig" # Tuple modification is not allowed
    print(tup_fruits)

    # Main use: i) keep unique values (but un-ordered)
    # ii) check it contains a value or not (better than list)
    sFruits = {"apple", "banana", "cherry", "dates", "apple"}
    print(sFruits)
    print("cherry" in sFruits)
    sFruits2 = {"apple", "banana", "fig", "grapes"}
    print(sFruits2)
    print(sFruits.intersection(sFruits2))  # common
    print(sFruits.difference(sFruits2))  # sFruits - sFruits2
    print(sFruits.union(sFruits2))  # all

    print(f"empty list: {[]} or {list()}")  # [] or list()
    print(f"empty tuple: {()} or {tuple()}")  # () or tuple()
    print("empty set: ", type({}), type(set()))  # only set(). {} or dict() is empty dictionary
    # print("empty dictionary: ", {})


def learn_number_func(learn):
    if not learn:
        return
    num = 3
    print(type(num))
    num = 3.14
    print(type(num))
    num1 = 7
    num2 = 3
    print("Addition: ", (num1 + num2))
    print("Subtraction: ", (num1 - num2))
    print("Multiplication: ", (num1 * num2))
    print("Division: ", (num1 / num2))
    print("Floor Division: ", (num1 // num2))
    print("Exponent: ", (num1 ** num2))
    print("Modulus: ", (num1 % num2))
    print("Absolute: ", abs(-num1))
    print("Round: ", round(num1 / num2))
    print("Round: ", round(math.pi, 5))
    # print("++: ", num1++) # not available
    num1 = num1 + 1
    print("increment by 1: ", num1)
    num1 += 9  # num1 = num1 + 1
    print("increment by 9: ", num1)
    num1 *= 2
    print("multiplied by 2: ", num1)

    print("Equal: ", (num1 == num2))
    print("Not Equal: ", (num1 != num2))
    print("Greater than: ", (num1 > num2))
    print("Less than: ", (num1 < num2))
    print("Greater OR equal: ", (num1 >= num2))
    print("Less OR equal: ", (num1 <= num2))

    # The characters in both strings are compared one by one
    print("apple" == "aPple")
    print("apple" > "aPple")
    print("Unicode of p: ", ord("p"), "\n", "Unicode of P: ", ord("P"))

    num1 = "7"
    num2 = "3"
    print(num1 + num2)  # for string, + concatenates
    print(int(num1) + int(num2))  # for numbers, + adds


def learn_str_func(learn):
    if learn:  # if learn == True
        msg = "Hello World Hello hello hello World"
        print(msg)
        print(type(msg))
        print(len(msg))

        print(msg[1])
        print(msg[0:5])  # 0=included but 5=not included i.e. 0,1,2,3,4
        print(msg[:5])  # before : => empty means start from beginning

        print(msg[6:])  # 6,7,...end

        print(msg.lower())
        print(msg.upper())
        print(msg.count("Hello"), "\n")
        print(msg.count("World"))
        print(msg.lower().count("hello"))
        print(msg.find("world"))  # case sensitive - not found = -1
        print(msg.find("World"))
        print("World" in msg)
        print(msg.find("World", 7))

        print(msg.replace("hello", "Hello"))
        first_str = "Hello"
        second_str = "World"
        msg = first_str + " " + second_str  # \t
        msg = "{} {}. We're learning python...story....first, second".format(
            first_str, second_str
        )
        msg = "{1} {0}. We're learning python...story....first, second".format(
            first_str, second_str
        )
        msg = f"{first_str} {second_str}. We're learning python."
        print(msg)
