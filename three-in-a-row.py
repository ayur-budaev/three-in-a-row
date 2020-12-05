import os

EMPTY_CELL = '.'

class Turn:

    turn_dic = {"O": "red", "X":"blue"}

    def __init__(self, turn = "O"):
        self.__state = turn

    def next_turn(self):
        if self.__state == 'O':
            self.__state = 'X'
        else:
            self.__state = 'O'

    def cur_turn(self):
        return self.__state

class Cell:

    global EMPTY_CELL

    def __init__(self, state = EMPTY_CELL):
        self.__state = state

    def is_empty(self):
        return self.__state == EMPTY_CELL

    def set(self, state):
        if self.is_empty():
            self.__state = state
            return True
        else:
            return False

    def state(self):
        return self.__state

class Field:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__cells = []
        for i in range(0, x):
            arr = []
            for j in range(0, y):
                cell = Cell()
                arr.append(cell)
            self.__cells.append(arr)

    def show(self):
        os.system('cls')
        for x in range(0, self.__x):
            row = ""
            for y in range(0, self.__y):
                row += self.__cells[x][y].state()
            print(row)

    def get_cell(self, x, y):
        return self.__cells[x][y]

    def set_cell(self, x, y, turn):
        return self.__cells[x][y].set(turn)

class Game:
    global EMPTY_CELL

    def __init__(self):
        self.__t = Turn(self.game_invitation())
        self.field_width = self.input_data("Type field width: ")
        self.field_height = self.input_data("Type field height: ")
        self.winner = Cell()
        success = False
        while not success:
            self.__l = self.input_data("Type length of sequence to win (l <= min(x, y): ", MAX_SIZE=min(self.field_width, self.field_height))
            success = self.__l <= min(self.field_width, self.field_height)
        self.__f = Field(self.field_width, self.field_height)
        self.run()

    def input_data(self, invitation, MAX_SIZE = 100, MIN_SIZE = 1):
        value = 0            

        while value > MAX_SIZE or value < MIN_SIZE:
            print("Your value must be between {} and {}".format(MIN_SIZE, MAX_SIZE))
            try:
                value = int(input(invitation))
            except ValueError:
                print("Please, remember that it must be a natural number.")
                value = 0
        return value

    def someone_won(self):
        
        xneighbors = [1, 0, 1, 1]
        yneighbors = [0, 1, -1, 1]

        for x in range(self.field_width):
            for y in range(self.field_height):
                start = self.__f.get_cell(x, y).state()
                if start == EMPTY_CELL: continue

                for neighbor in range(4):
                    length, xline, yline = 1, x, y
                    while length < self.__l:
                        xline += xneighbors[neighbor]
                        yline += yneighbors[neighbor]
                        if xline < 0 or xline >= self.field_width \
                            or yline < 0 or yline >= self.field_height \
                            or self.__f.get_cell(xline, yline).state() != start:
                                break
                        length += 1
                    if length == self.__l:
                        self.winner.set(start)
                        return

    def is_over(self):
        if self.winner.state() != EMPTY_CELL:
            return True
        for x in range(self.field_width):
            for y in range(self.field_height):
                if self.__f.get_cell(x, y).state() == EMPTY_CELL:
                    return False
        return True
        

    def run(self):
        while not self.is_over():
            self.__f.show()
            print("{}'s turn ({})".format(self.__t.turn_dic[self.__t.cur_turn()], self.__t.cur_turn()))
            self.turn()
        self.print_result()
        
    def turn(self):
        success = False
        while not success:
            x = self.input_data("Type cell row: ", MAX_SIZE=self.field_width) - 1               
            y = self.input_data("Type cell column: ", MAX_SIZE=self.field_height) - 1
            success = self.__f.set_cell(x, y, self.__t.cur_turn())
            if not success:
                print("Cell is not empty.")
        self.__t.next_turn()
        self.someone_won()

    def game_invitation(self):
        print("I want to play a game...")
        first_turn = input("Who start the game (type O or X): ").upper()
        while first_turn != 'O' and first_turn != 'X':
            os.system("cls")
            print("Please, pay attention.")
            first_turn = input("Who start the game (type O or X): ").upper()
        return first_turn

    def print_result(self):
        self.__f.show()
        if self.winner.state() == EMPTY_CELL:
            print("No turns left. Draw!")
        else:
            print("The winner is {} ({})!".format(self.__t.turn_dic[self.winner.state()], self.winner.state()))
        os.system("pause")

g = Game()
