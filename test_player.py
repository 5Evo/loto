from player import CPUPlayer, create_player
from loto import Cards


def setup():
    card_CPU = Cards()
    card_Human = Cards()
    playerCPU = create_player('Комп', '0', card_CPU)
    playerHuman = create_player ('Чел', '1', card_Human)

class TestPlayer:


    def test_init(selfself):
        pass


    def test_move_CPU(self):
        # Провеверка на вычеркивание
        pass

    def test_move_Human(self):
        # TODO: Зачеркиваем число:
            # TODO: число есть на карте
            # TODO: числа нет на карте
        # TODO: Не зачеркиваем число:
            # TODO: число есть на карте
            # TODO: числа нет на карте
        pass
