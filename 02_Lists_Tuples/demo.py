# Обхождане на списък
cities = ["Sofia", "Plovdiv", "Varna", "Blagoevgrad", "Sandanski"]

for city in cities:  # минава през всеки един елемент
    print(city)

for i in range(len(cities)):  # по подразбиране ще обходи в диапазона от 0 до 4 вкл.
    print(f"{i}. {cities[i]}")  # печата индекса и града, който се намира на това място

print(list(enumerate(cities)))  # [(0, 'Sofia'), (1, 'Plovdiv'), (2, 'Varna'), (3, 'Blagoevgrad'), (4, 'Sandanski')]

for i, city in enumerate(cities):  # най-добрият вариант ако ти трябва индекс и стойност
    print(i, city)  # на функ. enumerate може да се подаде втори аргумент, число за започване (дефоулт = 0)


# List comprehension - предпочитан и по-бърз вариант от обхождане и .append() напр.

numbers = [num for num in range(10)]

even_numbers = [num for num in range(10) if num % 2 == 0]

labels = ["even" if n % 2 == 0 else "odd" for n in numbers]  # ['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']


# Test belonging

cities = ["Sofia", "Plovdiv", "Varna", "Blagoevgrad", "Sofia", "Sandanski", "Sofia"]

if "Sofia" in cities:
    cities.remove("Sofia")  # Премахва първото срещане на София в списъка (т.е. с индекс 0)

if "Kavarna" not in cities:
    cities.append("Kavarna")

# Методите count и index
print(cities.count("Sofia"))  # Брои колко пъти се среща София в списъка в нашия случай - 2 пъти
print(cities.index("Sofia"))  # Връща индекса на първо срещнатата София тоест 3
