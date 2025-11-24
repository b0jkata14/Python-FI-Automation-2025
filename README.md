# Strypes Python FI Automation 2025

---

### Knowledge Checks

-  [Lists & Tuples](https://docs.google.com/forms/d/e/1FAIpQLSeFP4HFzCzh6NVxOQIHqVcqrwn2yD6iuTmNDHCRf6De4dqXJQ/viewform?usp=dialog)
-  [Functions](https://docs.google.com/forms/d/e/1FAIpQLSfPUvxxX7r0aEecrbSTY-5oz8NWBNvge9bmc3qryMvk30Ko8A/viewform?usp=header)
- [Object-Oriented Programming (OOP)](https://docs.google.com/forms/d/e/1FAIpQLSec-IleEHAoL73XVvfioZjwQbLsida70a2SwWBQD5F4rQZ5Fg/viewform?usp=dialog)
- [Exception Handling](https://docs.google.com/forms/d/e/1FAIpQLSch16Rfzuy7_0Ew6xYn5QT-xpFHzChBCeI5ti_KQWe51DFMPQ/viewform?usp=dialog)
- [WEB Basics — Interacting with REST APIs (1)](https://docs.google.com/forms/d/e/1FAIpQLSfmScyxjbLGD6bj7TGQQu2ir2mx9n5OC2zSJKLjbxKFiGAnhw/viewform?usp=dialog)
- [WEB Basics — Interacting with REST APIs (2)](https://docs.google.com/forms/d/e/1FAIpQLSfZnC3nR0EIeUgWzxt5RM3CKMgmUg9lPrMgRnuSGubvUSPaBA/viewform?usp=dialog)
- [Testing](https://docs.google.com/forms/d/e/1FAIpQLSfa-ysg8Wcb1wbU2hDxcZAPTPPG_-AU-rO8eW7-yCX-Eouivg/viewform?usp=publish-editor)
  
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
      mixed_values[-1]  # Връща първия елемент отдясно (последния) → None
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
    - `**kwargs` - събира именуваните аргументи в речник.
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

### 10. WEB Basics — Interacting with REST APIs (1)
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

3. Query параметри
      ```py
      r = requests.get("https://httpbin.org/get", params={"q": "mnknowledge", "page": 2})
      print(r.url)  # автоматично добавя ?q=mnknowledge&page=2

      r = requests.get("https://httpbin.org/headers",
                    headers={"X-Course": "API101"})
      print(r.json())
      ```
    - `params` вместо ръчно добавяне на `?`.
    - `headers` за изпращане на токени, тип съдържание и др.

4. Статус кодове
    - `200` - успешна заявка
    - `201` - успешно създаден ресурс
    - `401` - неоторизиран достъп
    - `404` - не е намерено
    - `500` - грешка в сървъра

5. Проверка и обработка на грешки
      ```py
      r = requests.get("https://httpbin.org/status/404", timeout=5)
      print(r.status_code, r.ok)  # 404 False

      try:
          r.raise_for_status()
      except requests.HTTPError as e:
          print("HTTP error:", e)
      ```
    - `timeout` - за да не "виси" програмата.
    - `raise_for_status()` — за автоматично откриване на 4xx/5xx грешки.

---

### 11. WEB Basics — Interacting with REST APIs (2)
1. POST – създаване на ресурс
    - Използва се за добавяне на нов обект.
    - Изпраща данни в body на заявката.
    - Най-често връща `201 Created`.
        ```py
        import requests

        url = "https://jsonplaceholder.typicode.com/posts"
        data = {
            "title": "Hello API",
            "body": "This is my first POST request",
            "userId": 1
        }

        r = requests.post(url, json=data)
        print(r.status_code)  # 201
        print(r.json())  # Върнатият нов ресурс
        ```

2. PUT и PATCH – промяна на ресурс
    - `PUT` - заменя целия обект.
    - `PATCH` - променя само конкретни полета.
    - И двата метода често връщат `200 OK`.
        ```py
        # PUT – пълна замяна
        r = requests.put("https://jsonplaceholder.typicode.com/posts/1",
                        json={"id": 1, "title": "Updated", "body": "Full replace", "userId": 1})

        # PATCH – частична промяна
        r = requests.patch("https://jsonplaceholder.typicode.com/posts/1",
                        json={"title": "Partial update"})
        ```
3. DELETE – изтриване на ресурс
    - Използва се за изтриване на съществуващ ресурс.
    - Връща `200 OK` или `204 No Content`.
        ```py
        r = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
        print(r.status_code)  # 200 или 204        
        ```

4. Сесии (requests.Session)
    - `Session()` - пази състояние между заявките.
    - Позволява споделени headers, cookies и връзки между заявки.
    - По-бързо и по-ефективно при множество заявки.
    - Използвай `with` за автоматично затваряне.
        ```py
        with requests.Session() as s:
            s.headers.update({"X-App": "Demo"})
            s.get("https://httpbin.org/cookies/set?theme=dark")
            res = s.get("https://httpbin.org/cookies")
            print(res.json())  # {'cookies': {'theme': 'dark'}}
        ```

5. Автентикация (Authentication)
    - `Authorization header` се използва за всички типове токени.
    - Никога не записвай токени в кода — използвай `.env` или променливи на средата.
    - Винаги използвай HTTPS при реална автентикация.
    - Basic Authentication (пример):
        ```py
        from requests.auth import HTTPBasicAuth

        r = requests.get("https://httpbin.org/basic-auth/user/pass",
                        auth=HTTPBasicAuth("user", "pass"))
        print(r.status_code)  # 200
        ```
    - Bearer Token Authentication (пример):
        ```py
        headers = {"Authorization": "Bearer testtoken123"}
        r = requests.get("https://httpbin.org/bearer", headers=headers)
        print(r.json())
        ```  

---

### 12. Testing (Тестване)
1. Автоматизирани тестове
    - Програми, които автоматично проверяват дали друг код работи правилно.
    - Спестяват време, предотвратяват повторни грешки, осигуряват стабилност.
    - Основни библиотеки в Python: unittest (вградена) или pytest.
    - Пример с `unittest`:
        ```py
        import unittest

        def add(a, b):
            return a + b

        class TestMath(unittest.TestCase):
            def test_add(self):  # Ако тестът се провали, Python спира с „FAILED“.
                self.assertEqual(add(2, 3), 5)  # assertEqual - проверява очаквания резултат
                self.assertNotEqual(add(2, 2), 5)

        if __name__ == "__main__":
            unittest.main()
        ```

2. Test philosophy & Test types
    - Тестването не доказва, че няма грешки — доказва, че кодът работи както очакваме.
    - Test Types:
      - Unit test - проверява отделна функция/метод - `assertEqual(add(2,3), 5)`
      - Integration test - проверява дали модулите работят заедно - (напр. API + база данни)
      - System test - проверява цялата система - (напр. Web UI + backend)
      - Acceptance test - проверява дали отговаря на изискванията на клиента - (напр. тест на бизнес сценарий)

3. TDD (Test-Driven Development)
    - (Стъпка 1) Напиши тест, който първоначално се проваля.
    - (Стъпка 2) Напиши минимален код, за да мине тестът.
    - (Стъпка 3) Подобри кода, запазвайки успешните тестове.
        ```py
        # 1. Първо пишем тест
        class TestEven(unittest.TestCase):
            def test_is_even(self):
                self.assertTrue(is_even(4))
                self.assertFalse(is_even(5))

        # 2. Тогава пишем функцията
        def is_even(x):
            return x % 2 == 0
        ```

4. Coverage (Покритие на кода)
    - Процент от кода, който е бил изпълнен от тестовете.
    - Измерва се с инструменти като coverage.py или pytest --cov.
    - Ако тестовете покриват 80% от кода → добър резултат, под 50% - вероятно има не тествани случаи.
        ```bash
        pip install coverage
        coverage run -m unittest
        coverage report
        ```

5. Breakpoints & Debugger
    - Целта е да спреш изпълнението на програмата и да видиш какво се случва „вътре“.

---
