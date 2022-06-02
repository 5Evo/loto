from loto import Cards
from player import create_player
from keg import Kegs

def game_over(players):
    for player in players:
        #print(player.name, player.is_winner)
        if not (player.is_winner is None):
            #print(player.name, player.is_winner)
            return True

    return False


print('Приветствуем Вас в Игре в ЛОТО')
number_of_players = int(input('Введите количество игроков: '))


# Создадим игроков:
players = []
for i in range(number_of_players):
    name = input(f'Введите имя {i+1} игрока: ')
    type_of_player = input('Введите тип игрока: "0" - компьютер, "1" - человек: ')
    card = Cards()
    player = create_player(name, type_of_player, card)
    #print(player)
    players.append(player)

# Создадим Мешок с бочонками:
bug_of_kegs = Kegs()
# print(f'Новый мешок: {bug_of_kegs}')
# z = input(f'game_over: {game_over(players)}')

while not game_over(players):                       # проверяем признак завершения игры у каждого
    next_number = bug_of_kegs.get_random_keg()      # вытянули число из мешка
    print(f'Выпало число {next_number}')

    for player in players:                # каждый игорк делает ход
        print(f'Ход делает:  {player}')
        player.move(next_number)

# проверим проигравшего:
for player in players:
    if player.is_winner == True:
        print(f'{player.name} - Победитель')
        #print(player)
    elif player.is_winner == False:
        print(f'{player.name} - Проиграл!')
        #print(player)
