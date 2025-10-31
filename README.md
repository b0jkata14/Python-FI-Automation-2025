# Strypes Python FI Automation 2025

---

### Knowledge Checks

-  [Lists & Tuples](https://docs.google.com/forms/d/e/1FAIpQLSeFP4HFzCzh6NVxOQIHqVcqrwn2yD6iuTmNDHCRf6De4dqXJQ/viewform?usp=dialog)
-  [Functions](https://docs.google.com/forms/d/e/1FAIpQLSfPUvxxX7r0aEecrbSTY-5oz8NWBNvge9bmc3qryMvk30Ko8A/viewform?usp=header)
- [Object-Oriented Programming (OOP)](https://docs.google.com/forms/d/e/1FAIpQLSec-IleEHAoL73XVvfioZjwQbLsida70a2SwWBQD5F4rQZ5Fg/viewform?usp=dialog)
- [Exception Handling](https://docs.google.com/forms/d/e/1FAIpQLSch16Rfzuy7_0Ew6xYn5QT-xpFHzChBCeI5ti_KQWe51DFMPQ/viewform?usp=dialog)
---

### 02. Lists & Tuples (Списъци и кортежи)
1. Списък (list)
    - Наредена и променяема (mutable) колекция от елементи.
    - Може да съдържа различни типове данни.
    - Създаване:
      ```py
      mixed_values = [42, "hello", 3.14, True, None]
      empty = []
      a = list()
      ```
    - Индексиране и отрязъци (slicing):
      ```py
      mixed_values[0]  # Връща първия елемент отляво в списъка → 42
      mixed_values[-1]  # Връща първия елемент отдясно (последния) → True
      mixed_values[1:4]  # Връща елементите от индекс 1 до 3 вкл. (от "hello" до True) → ['hello', 3.14, True]
      mixed_values[::-1]  # Връща списъка в обратен ред → [None, True, 3.14, 'hello', 42]
      ```
    - Основни операции:
      ```py
      numbers = [3, 7, 2, 9]

      len(numbers)  # Връща броя на елементите в списъка → 4
      5 in numbers  # Проверява дали 5 е в списъка → False
      more_numbers = numbers + [10, 20]  # Съединява два списъка → [3, 7, 2, 9, 10, 20]
      repeated = numbers * 2  # Повтаря елементите 2 пъти → [3, 7, 2, 9, 3, 7, 2, 9]
      min(numbers)  # Най-малкият елемент → 2
      max(numbers)  # Най-големият елемент → 9
      sum(numbers)  # Сборът на всички числа → 21
      ```
    - Основни методи:
      ```py
      fruits = ["apple", "banana", "cherry"]

      fruits.append("orange")  # Добавя елемент в края
      fruits.extend(["kiwi", "melon"])  # Добавя няколко елемента наведнъж
      fruits.insert(1, "pear")  # Вмъква "pear" на позиция 1

      fruits.pop()  # Премахва последния елемент и го връща
      fruits.remove("banana")  # Премахва първото срещане на 'banana'

      fruits.reverse()  # Обръща реда на елементите
      fruits.sort()  # Подрежда елементите по азбучен ред 
      ```
    - List comprehension:
      ```py
      [x**2 for x in range(10) if x % 2 == 0]
      # Само квадратите на четните числа от 0 до 9 вкл. → [0, 4, 16, 36, 64]
      ```

2. Кортеж (tuple)
    - Наредена, непроменяема (immutable) колекция.
    - Може да съдържа различни типове данни.
    - Създаване:
      ```py
      t = (1, 2, 3)
      single = (1,)
      b = tuple()
      ```
    - Полезни за:
      - фиксирани данни - например координати (x, y);
      - безопасно предаване на стойности;
      - използване като ключове в речници.
    - Поддържат индексиране и отрязъци (slicing), както и базовите операции като списъците.
    - Имат само методите count() и index()
      ```py
      t = (1, 2, 2, 3, 2)

      t.count(2)  # Брои колко пъти се среща 2 → 3
      t.index(2)  # Връща индекса на първото срещане на 2 → 1
      ```
    - НЕподдържат методи за промяна на съдържанието (append(), remove(), sort() и т.н.).

3. Обхождане с enumerate
    - Дава достъп до индекс + стойност:
      ```py
      for i, val in enumerate(['a', 'b', 'c']):
          print(i, val)

      # 0 a
      # 1 b
      # 2 c
      ```

---

### 05. Functions (Функции)
1. Какво представлява функцията?
    - Отделен блок код, който изпълнява конкретна задача.
    - Предимства: по-ясна структура и по-лесна поддръжка.
    - Създаване:
      ```py
      def hello(name):
          return f"Hello, {name}!"
      ```
2. Параметри
    - Входът на функцията – позволяват ѝ да работи с различни данни.
    - Видове параметри - позиционни, именувани, със стойности по подразбиране.
    - `*args` - събира всички позиционни аргументи в кортеж.
    - `*kwargs` - събира именуваните аргументи в речник.
      ```py
      def register_user(role, *skills, **details):
          # role = "Dev"
          # skills = ("Python", "SQL")
          # kwargs = {"name"="Ivan", "age"=21}

          print(role, skills, details)


      register_user("Dev", "Python", "SQL", name="Ivan", age=21)
      ```
3. Вложени функции
    - Достъпват променливи от обхвата над тях.
      ```py
      def outer():
          b = 6
          def inner():
              print(b)
          inner()
      

      outer() # 6
      ```
4. Рекурсия
    - Функция, която извиква сама себе си.
    - Задължителен базов случай (край на рекурсията).
    - Всеки рекурсивен проблем, може да бъде решен итеративно.
    - Пример:
      ```py
      def factorial(n):
          if n == 1:
              return 1  # Базов случай (дъно)

          return n * factorial(n - 1)
      ```
5. Генератори
    - Функции, които връщат итератор чрез `yield`.
    - „Помнят“ състоянието си между извикванията.
    - Спестяват памет и време.
    - Пример:
      ```py
      def count_up_to(n):
          i = 1
          while i <= n:
              yield i   # връща стойност и „запомня“ къде е стигнала функцията
              i += 1


      for num in count_up_to(5):
          print(num)
      ```

6. Анонимни функции (Lambda)
    - Синтаксис: `lambda аргумент(и): израз`
    - Ползва се в `map(), filter(), sorted()`
    - Пример:
      ```py
      numbers = [1, 2, 3, 4, 5]
      doubled = list(map(lambda n: n * 2, numbers))  # [2, 4, 6, 8, 10]
      ```
---

### 06. Object-Oriented Programming (Обектно-ориентирано програмиране)
1. Какво е ООП?
    - Начин на програмиране, при който кодът се организира около обекти, а не около функции.
    - Всичко в Python е обект.
    - Обектът комбинира данни (атрибути) и поведение (методи).
    - Основните принципи са: 
      - Капсулиране - скриване на вътрешната реализация и достъп само през методи.
      - Наследяване - позволява един клас да „наследи“ атрибутите и методите на друг.
      - Полиморфизъм - една и съща операция работи различно за различни типове обекти.
      - Абстракция - показваш само важното поведение, скриваш ненужните детайли.

2. Класове и обекти
    - Класът е „шаблон“ за създаване на обекти.
    - Обектът е конкретен екземпляр на класа.
    - Създаване:
      ```py
      class Car:
          def __init__(self, brand, color):  # атрибути
              self.brand = brand
              self.color = color

          def drive(self):  # метод
              print(f"The {self.color} {self.brand} is driving!")


      car1 = Car("Tesla", "red")  # Създаване на инстанция
      car1.drive()  # The red Tesla is driving!
      ```

3. Променливи на класа и обекта
    - Променливи на класа – споделени от всички обекти.
    - Променливи на обекта – индивидуални за всяка инстанция.
      ```py
      class Zombie:
          members = 0  # променлива на класа

          def __init__(self, name):
              self.name = name  # променлива на обекта

          def summon(self):
              Zombie.members += 1
      ```

4. Стойности по подразбиране (*често срещана грешка)
    - Никога не използвай списък или речник като стойност по подразбиране.
    - Защото Python ги създава само веднъж при дефиницията, не при всяко извикване!
    - Правилен вариант (всяка инстанция има собствен списък):
      ```py
      class SomeClass:
          def __init__(self, lst=None):
              self.lst = lst if lst is not None else []
      ```

5. Методи в класовете
    - Инстанционни методи – най-често срещани, работят със `self`.
    - Класови методи – работят с целия клас, използват `@classmethod` и `cls`.
    - Статични методи – не зависят от нито един обект, използват `@staticmethod`.
      ```py
      class MathDemo:
          def square(self, x):  # инстанционен метод
              return x ** 2

          @classmethod
          def show_class(cls):  # класов метод
              print("This is a class method.")

          @staticmethod
          def add(a, b):  # статичен метод
              return a + b
      ```

---

### 08. Exception Handling (Обработка на изключения)
1. Какво е изключение?
    - Обект, който Python създава автоматично при грешка по време на изпълнение.
    - Спира програмата, освен ако не бъде прихванато.
      ```py
      x = int("abc")  # ValueError
      print(5 / 0)  # ZeroDivisionError
      ```
    - Изключения ≠ syntax errors.
      - SyntaxError → грешка при компилация.
      - Exception → грешка при изпълнение (runtime).

2. try / except / else и finally - прихващане на изключения
    - Можеш да имаш няколко `except` блока.
    - `else` → за „нормалната“ логика след успешен `try`.
    - `finally` → за освобождаване на ресурси (файлове, връзки, мрежа и др.).
      ```py
      try:
          result = 10 / 2
      except ZeroDivisionError:
          print("Division by zero.")
      else:
          print("Everything worked!")  # само ако няма грешка
      finally:
          print("This runs no matter what.")  # винаги
      ```

3. Предизвикване на изключения
    - `raise` - ръчно „хвърляне“ на изключение.
      ```py
      age = -5
      if age < 0:
          raise ValueError("Age cannot be negative.")
      ```

4. Собствени изключения 
    - По-ясен контрол върху конкретен тип грешка.
      ```py
      class InvalidScore(Exception):
          """Custom exception for invalid exam scores."""
          pass

      def set_score(score):
          if not 0 <= score <= 100:
              raise InvalidScore("Score must be between 0 and 100.")
          print("Score accepted!")

      try:
          set_score(120)
      except InvalidScore as e:
          print("Custom exception:", e)  # Custom exception: Score must be between 0 and 100.
      ```

---

### 10. WEB Basics — Interacting with REST APIs
1. Какво е REST API?
    - REST (Representational State Transfer) — архитектурен стил, използващ HTTP методи.
    - API (Application Programming Interface) — начин различни системи да обменят данни.
    - Всеки ресурс (напр. потребител, пост, файл) има уникален URL.
    - Методи:
      - `GET` - извличане на данни - `/users`
      - `POST` - създаване на нов ресурс - `/users`
      - `PUT` - пълна промяна - `/users/1`
      - `PATCH` - частична промяна - `/users/1`
      - `DELETE` - изтриване - `/users/1`

2. Първи стъпки с requests
    - Инсталация:
      ```bash
      pip install requests
      ```
    - Пример:
      ```py
      import requests

      r = requests.get("https://jsonplaceholder.typicode.com/todos/1")
      print(r.status_code)  # 200
      print(r.json())  # Отговор в JSON формат
      ```
