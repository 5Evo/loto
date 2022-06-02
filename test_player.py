from player import CPUPlayer, create_player
from loto import Cards

class TestPlayer:

    def setup(self):
        card_CPU = Cards()

        self.player = create_player('test_name', '0', card_CPU)


    def test_init(self):
        assert self.player.name == 'test_name'
        assert self.player.is_winner == None
        assert len(self.player.card.numbers) == 15


    def test_move_CPU(self):
        # Проверка на вычеркивание: количество цифр на карте уменьшилось 1 после вычеркивания:
        init_len = len(self.player.card.numbers)
        del_number = self.player.card.numbers[0]
        self.player.move(del_number)
        new_len = len(self.player.card.numbers)
        assert init_len - new_len == 1
        # проверка на количество символов '-' на карточке после вычеркивания
        # init_len = len(self.player.card.numbers)

