from loto import Cards
from keg import Kegs
from player import create_player



# создаем мешок:
bug = Kegs()
# print(bug)

player_count = input('Введите количество игроков: ')

#создадим игроков и их карточки
players = []
for i in range(player_count):
    type_of_player = int(input(f'Введите тип игрока №{i+1} (0 - Компьютер, 1 - Человек: '))
    player_name = input(f'Введите имя: ') if type_of_player == 1
    card = Cards()
    player = create_player(player_name, type_of_player, card)