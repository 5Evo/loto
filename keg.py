"""
Модуль класса Бочонок для игры в Лото
"""
import random

class Kegs:

    def __init__(self):
        self.numbers = list(range(1, 91))

    def __str__(self):
        return str(self.numbers)

    def get_random_keg(self):
        result = random.sample(self.numbers, 1)[0]
        self.numbers.remove(int(result))
        return result

    def __len__(self):
        return len(self.numbers)

    def __eq__(self, other):
        '''
        Мешки равны, если количество бочонков (чисел) в них совпадают
        сами числа могут не совпадать, тк мы смотрим на мешок снаружи и никогда не знаем, какие в них числа
        :param other:
        :return:
        '''
        return len(self.numbers) == len(other.numbers)

    def __ne__(self, other):
        '''
        мешки не совпадают, если в них разное количество чисел
        :param other:
        :return:
        '''
        return len(self.numbers) != len(other.numbers)


if __name__ == '__main__':

    bug_of_kegs = Kegs()

