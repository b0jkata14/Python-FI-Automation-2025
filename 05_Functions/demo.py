def greet(first_name, last_name):
    print(f"Hello {first_name} {last_name}!")


greet("Peter", "Vasilev")


def change_num(num):
    num[0] = 643524


numbers = [1, 3, 6]
print(numbers)

change_num(numbers[:])
print(numbers)


def inc_num(num):
    return num + 1


x = 5
print(x)

x = inc_num(x)
print(x)


def bmi(weight=70, height=1.7):
    print(weight / (height * height))


bmi()
bmi(65)
bmi(60, 1.6)
bmi(height=1.9)
bmi(weight=34)
bmi(80, 1.8)
bmi(height=190, weight=90)


def power(base, exp=2):
    return base ** exp


print(power(2))
print(power(2, 3))


def sum_numbers(*args):
    return sum(args)


a = sum_numbers(1, 2, 3, 4)
print(a)


def params(a, b, *args, **kwargs):
    print("a, b: ", a, " ", b)
    print("args: ", args)
    print("kwargs: ", kwargs)


params(1, 2, 45, 45, 67, 42, x=2, y=5, d=124)

msg = "Hello from global!"


def outer():
    msg = "Hello from outer!"

    def inner():
        print(msg)

    print(msg)
    inner()
    print(msg)


outer()


def make_multiplier(n):
    def multiply(x):
        return x * n

    return multiply


times3 = make_multiplier(3)

times7 = make_multiplier(7)

result_of_times_7 = times7(7)

print(times3(5))
print(result_of_times_7 // 49)


x = "global"


def outer():
    global x
    x = "abvg"


print(x)
outer()
print(x)


def countdown(n):
    if n == 0:
        print("Done!")
        return

    print(n)
    countdown(n - 1)


countdown(5)


def fact_recursive(n):
    if n <= 0:
        return 1

    return n * fact_recursive(n - 1)


print(fact_recursive(5))

scores = {
    "Stanimir": [6, 6, 6, 6],
    "Diqn": [6, 6, 6, 6],
    "Krasimir": [6],
    "Ivaylo": [5, 5]
}


print(sorted(scores.items(), key=lambda x: (-len(x[1]), x[0])))


def my_generator():
    yield 1
    yield 2
    yield 3


for value in my_generator():
    print(value)

for value in my_generator():
    print(value)
