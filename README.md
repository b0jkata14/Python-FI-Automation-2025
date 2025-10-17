# Strypes Python FI Automation 2025

---

## Проверки на знанията
-  [Lists & Tuples](https://docs.google.com/forms/d/e/1FAIpQLSeFP4HFzCzh6NVxOQIHqVcqrwn2yD6iuTmNDHCRf6De4dqXJQ/viewform?usp=dialog)
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
