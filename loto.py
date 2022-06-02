"""
Модуль класса для игры в Лото
"""
from random import randint

class Cards:

    def __init__(self):
        """
        Метод формирует случайную карточку, цифры на карточке также располагаются в случайном месте
        Свойства Карточки:
        self.symbols = список всех чисел на карточке, включая пробелы (в типе str)
        self.numbers = список всех чисел на карточке
        self.amount = количество цифр на карточке
        self.lines = количество строк в карточке
        self.length = количество позиций в строке (числа + пробелы)
        """
        card_lines = 3
        card_lenght = 9
        amount_in_line = 5
        card_numbers = set()    # создаем пустое МНОЖЕСТВО для уникальных чисел на карточке

        # выберем нужное количество случайных и уникальных чисел для заполнения карточки:
        while len(card_numbers) < amount_in_line * card_lines:
            card_numbers.add(randint(1, 90))
        card_numbers = list(card_numbers)           # было уникальное множество => сделали сортируемый список

        # заполним ими карточку (3 линии по 5 чисел в каждой:
        card = [[card_numbers[j * amount_in_line + i] for i in range(amount_in_line)] for j in range(card_lines)]

        # отсортируем карточку по строкам:
        for i in range(card_lines):
            card[i].sort()

        # переведем числа в строки и расставим пустые места в карточке
        new_card = []
        for every_line in range(card_lines):
            # выберем случайные места для чисел на карточке:
            index_of_num = set()
            while len(index_of_num) < amount_in_line - 1:
                index_of_num.add(randint(0, card_lenght - 1))
            index_of_num = list(index_of_num)
            index_of_num.sort()

            #print('Принт ',every_line,  index_of_num, card[0])

            # ---
            next_number = 0
            line = []
            for i in range(card_lenght):
                if i in index_of_num:
                    line.append(' ' * 3)
                else:
                    line.append(str(card[every_line][next_number]))
                    next_number += 1
            # ---
            new_card.append(line)
        #print('расставим пробелы тут:', index_of_num)
        #print(line)
        #print(f'Карточка: {new_card}')
        self.symbols = new_card
        self.numbers = card_numbers
        self.amount = len(new_card)
        self.lines = card_lines
        self.length = card_lenght

    def __str__(self):
        """
        магический метод для вывода карточки на печать
        :return:
        """
        num_decorator = 31 # количество подчеркиваний в выделении карточки

        # Формируем карточку для печати:
        card_str = str('-' * num_decorator)             # верхний сепаратор карточки
        for i in range(self.lines):                     # сформируем 3 строки карточки
            line = ''
            for j in range(self.length):                # формируем каждую строку
                line = f'{line} {self.symbols[i][j]}'
            card_str += '\n' + line                     # добавим сформированную выше строку
        card_str += '\n' + str('-' * num_decorator)     # нижний сепаратор карточки
        #print(f'Вывод карточки: {self.symbols}')
        return card_str

    def __contains__(self, item):
        #print(f'проверка на вхождение: {item}, type{item} -- а тип self.numbers {self.numbers}')
        if isinstance(item, int):
            pass
            item = int(item)
        return item in self.numbers

    def cross_out(self, number):
        """
        если такого числа в карточке нет - "Проиграл"
        если число есть - вычериваем его из карточки и удаляем из списка чисел
        потом проверяем: если в карточке больше нет чисел - возвращаем "Выиграл"

        :return:
        """
        # TODO: если числа нет в карточке - возвращаем "Вы Проиграли"
        # TODO: если "число" в карточке - зачеркиваем его в карточке и удаляем их списка чисел
        # TODO: проверяем, остались ли еще еще числа, если нет - возвращаем "Вы Выиграли"
        #print(int(number) in self.numbers)
        #print(f'проверка на вхождение: {number}, type {type(number)} -- а тип self.numbers {type(self.numbers)}')

        if int(number) in self.numbers:
            self.numbers.remove(int(number))        # удалили число из списка чисел
            # Сформируем новую карточку:
            new_symbols = []
            for line in self.symbols:               # Для каждой строки в карточке
                # Сформируем новую строку:
                new_line = []
                for symbol in line:
                    new_line.append(symbol if symbol != number else '-')
                new_symbols.append(new_line)
            self.symbols = list(new_symbols)
            # print(f'Для теста: зачеркиваем число {number}: \n{self.symbols}')
        else:
            print('НЕТ ТАКОГО ЧИСЛА!')
            # result = False

    def is_empty(self):
        return True if len(self.numbers) == 0 else False


# проверка модуля
if __name__ == '__main__':

    # Создание карточки
    my_card = Cards()
    print(my_card)
    print(f'Карточка пустая? {my_card.is_empty()}')
    # is_winner = None
    while not my_card.is_empty():
        number = input("какое число зачеркнем: ")
        #print(f'Старые числа: {my_card.numbers}')
        # print(type(number))
        my_card.cross_out(number)
        # print(is_winner)
        # print(f'Карточка пустая? {my_card.is_empty()}')
        #print(f'Новые числа:  {my_card.numbers}')
        print(my_card)
