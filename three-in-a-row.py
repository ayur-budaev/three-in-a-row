import os

class Turn:

    turn_dic = {"O": "red", "X":"blue"}

    def __init__(self, turn = "O"):
        self.__state = self.turn_dic[turn]

    def next_turn(self):
        if self.__state == self.turn_dic["O"]:
            print("Next turn is: blue")
            self.__state = self.turn_dic["X"]
        else:
            print("Next turn is: red")
            self.__state = self.turn_dic["O"]

    def cur_turn(self):
        return self.__state

class Cell:

    __empty_cell = "_"

    def __init__(self, state = __empty_cell):
        self.__state = state

    def is_empty(self):
        return self.__state == self.__empty_cell

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
        return self.__cells[x, y]

    def set_cell(self, x, y, turn):
        return self.__cells[x][y].set(turn)

class Game:

    def __init__(self, first_turn):
        self.__t = Turn(first_turn)
        x = self.input_data("Type field width:")
        y = self.input_data("Type field height:")
        success = False
        while not success:
            self.__l = self.input_data("Type length of sequence to win (l <= min(x, y):")
            success = self.__l <= min(x, y)
        self.__f = Field(x, y)
        self.run()

    def input_data(self, invitation):
        print(invitation)
        return int(input())
    
    def someone_won(self):
        #Checking three in a row
        print("Write algorithm")
        return False

    def run(self):
        while not self.someone_won():
            self.__f.show()
            self.turn()
        print("The winner is ", self.__t.cur_turn())
        
    def turn(self):
        success = False
        while not success:
            x = self.input_data("Type cell row:") - 1
            y = self.input_data("Type cell column:") - 1
            success = self.__f.set_cell(x, y, self.__t.cur_turn())
            print("Cell is not empty.")
        self.__t.next_turn()

print("Who start the game (type O or X):")
try:
    first_turn = input()
    g = Game(first_turn)
except:
    print("rerun game and then print what you asked")
