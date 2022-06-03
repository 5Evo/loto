from loto import Cards

class TestCards:

    def setup(self):
        self.card = Cards()                             # сформируем карточку для тестов

    def test_init(self):
        # TODO: проверить размерность карточки (3х9)
        # TODO: проверить количество цифр в каждом ряду (5)
        another_card = Cards()                          # создадим вторую карточку для сравнения
        assert isinstance(self.card, Cards)             # создается ли карточка
        assert self.card != another_card                # проверим, что генерируются разные карточки
        assert len(set(self.card.numbers)) == 15        # проверим что в карточке 15 уникальных чисел
        assert set(self.card.numbers).issubset(range(0, 91))        # все числа в диапазоне (0, 90)

    def test_contains(self):
        # сгенерирруем карточку и выберем второе число на карточке
        test_number = self.card.numbers[2]
        # проверим, что это число проходит проверку на вхождение в карточку:
        assert test_number in self.card.numbers

    def test_cross_out(self):
        '''
        #TODO:  проверить что вычеркнули из списка чисел
        #TODO:  проверить что стерли с карточки то же самое число
                Взять новую карточку, взять первое число из карточки и вычеркнуть его:
                проверить что :
                1. в списке чисел стало на одно меньше
                2. в списке символов - общее количество символов не изменилось, а '-' стало на 1 больше
        :return:
        '''
        del_number = str(self.card.numbers[7])
        #print(f'\nВычеркиваем {del_number}, {type(del_number)}')
        result = self.card.cross_out(del_number)
        #print(f'в списке чисел осталось {len(self.card.numbers)}')
        assert len(self.card.numbers) == 14     # в списке стало на 1 число меньше
        print('\n', self.card)                  # выводим карту, чтобы убедиться глазами: вставили 1 '-'
        dush_count = 0
        for line in self.card.symbols:
            dush_count += line.count('-')
        assert dush_count == 1

    def test_is_empty(self):
        assert not self.card.is_empty()         # новая карта не может быть пустой
        # зачеркнем на карточке все числа:
        for i in range(len(self.card.numbers)):         # пройдемся по всем числам на карте
            del_number = str(self.card.numbers[0])      # выбрали самое первое число из оставшихся чисел на карте
            self.card.cross_out(del_number)             # зачеркнули его
        assert self.card.is_empty()             # вычеркнули все числа по порядку, теперь карта должна быть пустой

    def test_eq(self):
        other = Cards()                 # Создаем новую карту
        #print('\nOther:\n', other)
        #print('\nSelf:\n', self.card)
        other.numbers = self.card.numbers   # Все числа из первой карты переносим в новую
        #print(other.numbers, '\n', self.card.numbers)      # можем убедиться, что числа действительно совпадают
        assert other == self.card           # все числа совпадают, значит карты должны быть равны

    def test_ne(self):
        other = Cards()  # Создаем новую карту
        # print('\nOther:\n', other)
        # print('\nSelf:\n', self.card)
        # print(other.numbers, '\n', self.card.numbers)      # можем убедиться, что числа на картах не совпадают
        assert other != self.card  # все числа совпадают, значит карты должны быть равны