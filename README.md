# Лабораторная работа №3

#### Задание №1

1.1 Создать ветку task/complete-first-task-фамилия(на англ)
1.2 Каждый из разработчиков создает класс ElementФамилия,
имеющий атрибуты объекта name, symbol и number. Создать объект этого
класса со значениями из таблицы Менделеева в соответствии с вашим
вариантом по списку. В корневой README.md включить описания
создаваемого объекта. Результат работы зафиксировать в репозиториии в
каталоге «ElementФамилия».
1.3 Для класса ElementФамилия определить метод в именем dump(),
который выводит на экран значения атрибутов объекта (name, symbol и
number). Создать объект соответствующий элементу по варианту и
использовать метод dump(), чтобы вывести на экран атрибуты элемента.
Результат работы зафиксировать в репозиториии в каталоге
«ElementФамилия».
1.4 Модифицировать класс ElementФамилия, сделав атрибуты name,
symbol и number приватными. Определить свойство получателя для
каждого атрибута, возвращающее его значение. Результат работы
зафиксировать в репозиториии в каталоге «ElementФамилия».
1.5 Сделать мердж реквест в master ветку

##### Описание создаваемых объектов

- Водород(H): 1 элемент
- ...
- ...

##### Примечание

- Комитов должно быть не меньше 5

#### Задание №2

- Реализовать программу на Python в соответствии с вариантом из
  таблицы 1. Разработка должна идти итеративно, периодически создавая
  отдельные ветки в Gitea и сливая их (через зарос на слияние - PR) после
  ревью другими участниками команды. Реализация программы должна
  быть выполнена по зонам ответственности, указанным в таблицах 2 и 3.
  Результат работы зафиксировать в репозитории в каталоге «app».

##### Задание по варианту

- Программа расчета объема правильной пирамиды

##### Таблица 1

| Зона ответственности разработчика №1   | Зона ответственности разработчика №2 | Зона ответственности разработчика №3 |
| -------------------------------------- | ------------------------------------ | ------------------------------------ |
| Начальное определение родительского    | Определение методов класса.          | Наследование от родительского        |
| класса и атрибутов. Определение        | Инициализация. Определение приватных | класса. Переопределение методов      |
| статического метода about() для вывода | (закрытых) атрибутов объектов.       | Реализация вычисляемого значения     |
| информации по команде разработки.      |                                      |
