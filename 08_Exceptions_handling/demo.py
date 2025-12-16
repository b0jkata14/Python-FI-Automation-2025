users = {"alice": 25}

# print(users["bob"])  # KeyError: ключът "bob" не съществува

numbers = [1, 2, 3]

# print(numbers[10])  # IndexError: индексът не съществува

age = 5

if age < 0:
    raise ValueError("Age cannot be negative")  # вдигаме грешка, защото възрастта не може да е отрицателна


try:
    x = int(input())
    y = int(input())
    print(x / y)  # може да хвърли ZeroDivisionError
except ZeroDivisionError:
    print("Ne moje delenie na 0")
except ValueError:
    print("Nevaliden vhod")
except Exception:
    print("Drug tip greshka")

print("Programata produljava!")

while True:
    try:
        x = int(input())
        y = int(input())
        print(x / y)
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error {e}")
    except Exception as e:
        print("Unexpected error:", e)
    else:
        print("Operation completed successfully!")
        break
    finally:
        print("Finally block is always executed, even after break or error")
        # finally се изпълнява винаги – дори когато има break,
        # защото Python първо приключва try-блока, после излиза от цикъла


# Custom грешки
class IncorrectAge(Exception):
    ...


class CustomError(Exception):
    ...


# try:
#     int("abc")
# except ValueError as e:
#     raise RuntimeError("Conversion failed") from e
    # вдигаме нова, по-смислена грешка,
    # като запазваме оригиналната причина (exception chaining)
