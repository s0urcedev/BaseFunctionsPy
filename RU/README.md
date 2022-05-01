# BaseFunctionsJS_RU

## Вступление

В этом гайде вы сможете получить основные зания по Python. Причиной написания гайда была сложность и запутаность которую я заметил в другий гайдах и руководствах. Безусловно я не эксперт в Python, но при этом имею какой-то опыт и думаю, что могу помочь этими знаниями другим :)

## Полезные ссылки

Так как этот гайд достаточно субъективный я не уверен что захвачу все темы и не уверен что у нас не появяться вопросы после прочтения, по-этому в этом блоке прикреплю хорошие ссылки который можно использовать в таких случаях.

В первую очередь вы можете написать мне на почты и я попробую вам помочь:

boyarkin.gleb@gmail.com;

source.boar@gmail.com

Так же почты подублированы у меня в профиле.

Кроме меня вы можете воспользоваться: 

https://pythonworld.ru/samouchitel-python

https://metanit.com/python/tutorial/

Эти источники гарантирую что являються проверенными, сам по ним учился, но как по мне многие вещи там расписаны слишком сложными словами.

## Коротко про Python

Python — достаточно старый, но популярный в наше время язык. На нем очень легко писать мелкие программы, по-этому он в основном испольхуэться в маленьких проектах или для мелких автоматизаций.

## Синтаксис

Синстаксис в Python не являеться С-подобным и различаеться достаточно сильно, но от этого не становится сложнее.

**Если проходиться по основным правилам синтаксиса то:**

* символа для окончания строки нету

* `:` – переход на уровень ниже, открытие блока кода

* `snake_case` – стиль именованияпеременный и функций

* `PascalCase` – стиль именования классов

* `#` – символ для комментария одной строки

* `''' '''` – символы для комментирования блока кода

***Подробнее про правила написания кода написано в официыльном постановлении `PEP8`:*** https://peps.python.org/pep-0008/

## Работа с консолью

`input('''текст сообщения''')` – ввод с консоли

`print('''текст сообщения''')` – вывод в консоль

## Переменные

Как я думаю вам известно, или станет известо сейчас, по факту весь язык программирования держиться на переменных и операциях над ними.

В Python переменная — это указатель на область или ячейку памяти в которой хранится какое то зничени. Факт про память пока можно просто положить в голову, к нему мы прийдем потом.

Для объявления не нужны ключевые слова.

```py
a1 = 1
a2 = True
a3 = "hello"
```

При именовании переменных, как указано было выше, используеться стиль snake_case.

Что ж в него входит?

**snake_case:**

* все буквы нижнего регистра

* слова разделяються `_`

Так же если конкретно про Python то в нем название переменной может начинать с символа `_` или буквы любого регистра, последующие символы уже могут быть такие же плюс цифры(0-9). Так же стоит уточнить что Python чувствителен к регистру, то есть в нем `a` и `A` это разные имена.

Явно локальность или глобальность переменной в Python не указывается. По умолчанию они локальны для блока кода в котором они объявляються. Для использования глобальных или переменных внешнего блока кода используеться `global` и `nonlocal`

### global

Это ключевое слово используется для обозначения того, что переменная в этом блоке кода будет браться из глобального уровня, уровня программы.

***Пример:***

```py
a1 = 1

def func1():
    print(a1) # а1 не объявлена

def func2():
    global a1
    print(a1) # 1

def func3():
    def fucn4():
        global a1
        print(a1) # 1
```

### nonlocal

Это ключевое слово используется для обозначения того, что переменная в этом блоке кода будет браться из блока кода на уровень выше.

***Пример:***

```py
a1 = 1

def func1():
    a1 = 2
    def fucn2():
        global a1
        print(a1) # 1
    
    def func3():
        nonlocal a1
        print(a1) # 2
```

### Типы данных

**Тип данных** — типы того, какого типа значение может хранить переменная.

**Базовые типы данных в Python:**

* `bool` – логический тип данных, хранит 2 вида значений: `True` или `False`

* `int` – целочисленный тип данных, хранит целые числа, без ограничения по значению, оно зависит от мощности компьютера

* `float` – дробный тип данных, хранит дробные числа

* `complex` – комплексный тип данных, хранит комплексные числа

* `str` – строчный тип данных, хранит строку текста почти неограниченого размера