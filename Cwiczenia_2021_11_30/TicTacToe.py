from os import system

class Game:
    def __init__(self, who_start):
        self.outcomes = ['Tie', 'Circle win', 'X win']
        self.result = ''
        self.board = [[' ', ' ', ' '],
                     [' ', ' ', ' '],
                     [' ', ' ', ' ']]
        self.turn = who_start
        self.is_game_over = False
        self.moves = 0
        self.remaining_positions = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.board_coords = { '1' : [0,0],
                              '2' : [0,1],
                              '3' : [0,2],
                              '4' : [1,0],
                              '5' : [1,1],
                              '6' : [1,2],
                              '7' : [2,0],
                              '8' : [2,1],
                              '9' : [2,2]}
    

    def print_board(self):
        line = '-+-+-'
        for i, row in enumerate(self.board):
            print(row[0] + '|' + row[1] + '|' + row[2])
            
            if i != 2:
                print(line)
    

    def place_symbol(self):
        pos = '0'
        while pos not in self.remaining_positions:
            pos = input("Where: (1 - 9)")
            if pos not in self.remaining_positions:
                print("Wrong input.")
        
        self.remaining_positions.remove(pos)
        self.change_turn()
        self.moves +=1
        return pos
        
    def change_turn(self):
        if self.turn == 'x':
            self.turn = 'o'
        else:
            self.turn = 'x'

    def move(self):
        symbol = self.turn
        pos = self.place_symbol()
        pos_on_board = self.board[self.board_coords[pos][0]][self.board_coords[pos][1]]
        if pos_on_board == ' ':
            self.board[self.board_coords[pos][0]][self.board_coords[pos][1]] = symbol
    
    def check(self):
        win_list = [['x', 'x', 'x'], ['o', 'o', 'o']]
        columns = [[],[],[]]
        diagonals = [[], []]
        for j, row in enumerate(self.board):
            if row in win_list:
                self.result = self.outcomes[1 if self.turn == 'x' else 2]
                self.is_game_over = True
            for i, elem in enumerate(row):
                columns[i].append(elem)
                if i == j:
                    diagonals[0].append(elem)
                if j + i == 2:
                    diagonals[1].append(elem)

        if not self.is_game_over:
            for column in columns:
                if column in win_list:
                    self.is_game_over = True
                    self.result = self.outcomes[1 if self.turn == 'x' else 2]
            
            if diagonals[0] in win_list or diagonals[1] in win_list:
                self.is_game_over = True
                self.result = self.outcomes[1 if self.turn == 'x' else 2]


        if self.moves == 9 and not self.is_game_over:
            self.is_game_over = True
            self.result = self.outcomes[0]
        



def main():
    game = Game('x')
    
    while not game.is_game_over:
        game.print_board()
        game.move()
        system('cls')
        game.check()

    print(game.print_board())
    print(game.result)
main()