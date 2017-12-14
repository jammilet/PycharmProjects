import random  # imports should be at the top
print(random.randint(0, 6))

print('Hello World')


# jamilet

print(3 + 5)
print(5 - 3)
print(5 * 3)
print(6 / 2)
print(3 ** 2)

print()  # creates a blank line
print('see if you can figure this out')
print(5 % 3)


# taking input
name = input('What is your name?')
print('Hello %s' % name)
# print(name)

age = input('What is your age?')
print('%s you are old' % age)


def print_hw():
    print('Hello World')


print_hw()


def say_hi(name1):
    print('Hello %s.' % name1)
    print('I hope you have a fantastic day')


say_hi('jamilet')


def birthday(age1):
    age1 += 1  # age = age + 1


say_hi('John')
print('John is 15. Next year:')
birthday(16)


# variables
car_name = 'jamilet mobile'
car_type = 'toyota'
car_cylinders = 8
car_mpg = 900.1

# inline printing
print('my car is the %s.' % car_name)
print('my car is the %s. it is a %s' % (car_name, car_type))


def birthday(age1):
    age1 += 1   # age = age + 1


def f(x):
    return x**5 + 4 * x ** 4 - 17*x**2 + 4


print(f(3))
print(f(3) + f(5))

# if statements


def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:  # else if
        return "B"
    if percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    elif percentage >= 50:
        return "E"
    elif percentage >= 40:
        return "F"

# loops

# for num in range(5):
# print(num + 1)

# for letter in "Hello World":
#    print(letter)

    a = 1
    while a < 10:
        print(a)
        a += 1

# response = ""
# while response != "Hello":
#  response = input("Say \"Hello\"")


print("Hello \nWorld")  # \n means newline


#  comparisons
print(1 == 1)  # two equal signs to compare
print(1 != 2)  # one is not equal to two
print(not False)
print(1 == 1 and 4 <= 5)


# recasting
c = '1'
print(c == 1)  # false - c is a string, 1 is an integer
print(int(c) == 1)
print(c == str(1))


num = input("give me a number")
# inputs are ALWAYS (!!!!!!!) of type string!!!
