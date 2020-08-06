"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.

Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
При этом скрипт завершается, сформированный список выводится на экран.

Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и
вносить его в список, только если введено число. Класс-исключение должен не позволить пользователю
ввести текст (не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
"""


class MyOwnError(Exception):
    def __init__(self, txt="Value error! List should contain only numbers!"):
        self.txt = txt
        super().__init__(self.txt)


def check_number(string):
    try:
        float(string)
    except ValueError:
        return False
    return True

lst = []
while True:
    list_num = input("Enter the line of numbers (Enter 'n' to finish): ").split()
    for e in list_num:
        try:
            if not check_number(e):
                raise MyOwnError()
            lst.append(float(e))
        except MyOwnError as err:
            print(err)
    print(lst)
    if "n" in list_num:
        break
print(lst)
