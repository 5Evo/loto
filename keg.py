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



if __name__ == '__main__':

    bug_of_kegs = Kegs()

    # print(f'новый мешок: {len(bug_of_kegs)}, {bug_of_kegs.numbers}, ')
    # next_keg = bug_of_kegs.get_random_keg()
    # print(type(bug_of_kegs.numbers))
    # print(f'Выпало число: {next_keg}')
    # print(f'В мешке осталось: {len(bug_of_kegs)}, {bug_of_kegs.numbers}')

