import random


class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign

    def make_move(self, field):
        print(f'сделайте ход {self.name}: ', end='')
        while True:
            move = int(input())
            if field[move] == '-' and 0 <= move <= 8:
                field[move] = self.sign
                break
            else:
                print(f'сделайте другой ход {self.name}: ', end='')
        return move


class Machine:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign


    def set_complexity(self, complexity):
        if complexity == 'hard':
            self.make_move = self.hard_move
        elif complexity == 'medium':
            self.make_move = self.medium_move
        elif complexity == 'easy':
            self.make_move = self.easy_move


    def hard_move(self, field):
        # победные ходы
        func1 = lambda a, b, c: field[a] == field[b] == self.sign and field[c] == '-'
        func2 = lambda a, b, c: field[a] == field[b] and field[b] != '-' and field[c] == '-'

        # horizontal
        if func1(0, 1, 2):
            field[2] = self.sign
        elif func1(2, 0, 1):
            field[1] = self.sign
        elif func1(1, 2, 0):
            field[0] = self.sign

        elif func1(3, 4, 5):
            field[5] = self.sign
        elif func1(5, 3, 4):
            field[4] = self.sign
        elif func1(4, 5, 3):
            field[3] = self.sign

        elif func1(6, 7, 8):
            field[8] = self.sign
        elif func1(8, 6, 7):
            field[7] = self.sign
        elif func1(7, 8, 6):
            field[6] = self.sign

        # vertical

        elif func1(0, 3, 6):
            field[6] = self.sign
        elif func1(6, 0, 3):
            field[3] = self.sign
        elif func1(3, 6, 0):
            field[0] = self.sign

        elif func1(1, 4, 7):
            field[7] = self.sign
        elif func1(7, 1, 4):
            field[4] = self.sign
        elif func1(4, 7, 1):
            field[1] = self.sign

        elif func1(2, 5, 8):
            field[8] = self.sign
        elif func1(8, 2, 5):
            field[5] = self.sign
        elif func1(5, 8, 2):
            field[2] = self.sign

        #diagonal

        elif func1(0, 4, 8):
            field[8] = self.sign
        elif func1(8, 0, 4):
            field[4] = self.sign
        elif func1(4, 8, 0):
            field[0] = self.sign

        elif func1(2, 4, 6):
            field[6] = self.sign
        elif func1(6, 2, 4):
            field[4] = self.sign
        elif func1(4, 6, 2):
            field[2] = self.sign

        # ходы против противника

        # horizontal
        elif func2(0, 1, 2):
            field[2] = self.sign
        elif func2(2, 0, 1):
            field[1] = self.sign
        elif func2(1, 2, 0):
            field[0] = self.sign

        elif func2(3, 4, 5):
            field[5] = self.sign
        elif func2(5, 3, 4):
            field[4] = self.sign
        elif func2(4, 5, 3):
            field[3] = self.sign

        elif func2(6, 7, 8):
            field[8] = self.sign
        elif func2(8, 6, 7):
            field[7] = self.sign
        elif func2(7, 8, 6):
            field[6] = self.sign

        # vertical

        elif func2(0, 3, 6):
            field[6] = self.sign
        elif func2(6, 0, 3):
            field[3] = self.sign
        elif func2(3, 6, 0):
            field[0] = self.sign

        elif func2(1, 4, 7):
            field[7] = self.sign
        elif func2(7, 1, 4):
            field[4] = self.sign
        elif func2(4, 7, 1):
            field[1] = self.sign

        elif func2(2, 5, 8):
            field[8] = self.sign
        elif func2(8, 2, 5):
            field[5] = self.sign
        elif func2(5, 8, 2):
            field[2] = self.sign

        #diagonal

        elif func2(0, 4, 8):
            field[8] = self.sign
        elif func2(8, 0, 4):
            field[4] = self.sign
        elif func2(4, 8, 0):
            field[0] = self.sign

        elif func2(2, 4, 6):
            field[6] = self.sign
        elif func2(6, 2, 4):
            field[4] = self.sign
        elif func2(4, 6, 2):
            field[2] = self.sign

        # ходы по приоритету

        elif field[4] == '-':
            field[4] = self.sign

        elif field[0] == '-':
            field[0] = self.sign
        elif field[2] == '-':
            field[2] = self.sign
        elif field[6] == '-':
            field[6] = self.sign
        elif field[8] == '-':
            field[8] = self.sign

        elif field[1] == '-':
            field[1] = self.sign
        elif field[3] == '-':
            field[3] = self.sign
        elif field[5] == '-':
            field[5] = self.sign
        elif field[7] == '-':
            field[7] = self.sign
         
         
    def medium_move(self, field):
        func = random.choice([self.hard_move, self.easy_move])
        func(field)

    def easy_move(self, field):
        indexes = []
        for i, elem in enumerate(field):
            if elem == '-':
                indexes.append(i)
        move = random.choice(indexes)
        field[move] = self.sign


class Field:
    def __init__(self):
        self.field = ['-' for _ in range(9)]

    def __str__(self):
        row1 = f'{self.field[0]} {self.field[1]} {self.field[2]}'
        row2 = f'{self.field[3]} {self.field[4]} {self.field[5]}'
        row3 = f'{self.field[6]} {self.field[7]} {self.field[8]}'
        return f'{row1}\n{row2}\n{row3}\n'

    def is_win(self):
        func = lambda a, b, c: self.field[a] == self.field[b] == self.field[c] != '-'

        if (func(0, 1, 2) or func(3, 4, 5) or func(6, 7, 8) or
            func(0, 3, 6) or func(1, 4, 7) or func(2, 5, 8) or
            func(0, 4, 8) or func(2, 4, 6)):
            return True
        return False


class Game:
    def __init__(self, player1, player2):
        self.game_field = Field()
        self.player1 = player1
        self.player2 = player2

        if isinstance(self.player1, Machine):
            self.player1.set_complexity(input('выберите сложность игры (hard, medium, easy): '))
        elif isinstance(self.player2, Machine):
            self.player2.set_complexity(input('выберите сложность игры (hard, medium, easy): '))

            
    def start_game(self):
        print(self.game_field)
        for i in range(9):
            if i % 2 == 0:
                player = self.player1
            else:
                player = self.player2

            player.make_move(self.game_field.field)

            print(f'xoд {i} сделан')
            print(self.game_field)

            is_win = self.game_field.is_win()
            if is_win:
                print(f'победил {player.name}!')
                break
        
        if i == 8 and (not is_win):
            print('ничья')
        


def main():
    players = [Player('ildar', 'x'), Machine('machine', 'o')]
    random.shuffle(players)

    game = Game(*players)
    game.start_game()


if __name__ == '__main__':
    main()