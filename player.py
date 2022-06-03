from loto import Cards
from keg import Kegs

class CPUPlayer:

    def __init__(self, name, card):
        self.card = card
        self.name = name
        # True - победитель, False - проигравший, None - еще играет
        self.is_winner = None

    def __str__(self):
        type_of_player = 'Человек' if type(self).__name__ == 'HumanPlayer' else 'Компьютер'
        result = f'{self.name} - {type_of_player}\n{self.card}'
        return result

    def __eq__(self, other):
        '''
        Игроки равны, если они одинакового типа (комп/человек) и имя у них одинаковое
        При этом карточки мы не проверяем, т.к. одному игорку могут выпадать разные карточки
        :param other:
        :return:
        '''
        return (self.name == other.name) and (type(self).__name__ == type(other).__name__)



    def move(self, number):
        #print(f'move - Комп: {number} {number in self.card}')
        if number in self.card.numbers:             # компьютер зачеркивает число
            # print(f'Зачеркиваем число {number}')
            self.card.cross_out(str(number))
            # print(self.card)
            if self.card.is_empty():        # Проверим на выигрыш
                self.is_winner = True



class HumanPlayer(CPUPlayer):

    def move(self, number):
        #print(f'move - Человек {number}')
        answer = input('Зачеркиваем? y/n: ')
        if answer == 'y':
            if number in self.card.numbers:          # Проверим есть ли такое число на карточке
                self.card.cross_out(str(number))     # зачеркнем число
                if self.card.is_empty():        # проверим не выиграл ли игрок
                    self.is_winner = True
            else:                               # если числа не оказалось на карточке, то сразу проиграл
                self.is_winner = False
        else:
            # если число все-таки есть на карте, то проигрыш:
            if number in self.card.numbers:
                self.is_winner = False



def create_player(name, player_type, card):
    players = {
        '0': CPUPlayer,
        '1': HumanPlayer
    }
    player = players[player_type](name, card)
    return player



if __name__ == '__main__':
    bug_of_kegs = Kegs()
    card_CPU = Cards()
    player1 = create_player('Alex', '0', card_CPU)
    print(f'вот и новый игрок: {player1}, {type(player1)}')
    # print(player1.name, '\n', player1.card)
    print(player1)
    for next_number in range (1, 91):
    # next_number = bug_of_kegs.get_random_keg()
        print(f'------------->Выпало число {next_number}<-------------')
        player1.move(next_number)

    print(player1)