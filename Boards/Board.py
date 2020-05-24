
class Board:
    level = 0
    board_list = []
    saved_boards_list = []
    new_board = []

    def __init__(self):
        with open("Boards/board.txt") as file_in:
            for line in file_in:
                self.board_list.append(line.split())

    def save_board(self):
        # global board
        # global saved_boards
        self.saved_boards_list.append("Boards/board" + str(self.level) + "_1.txt")
        with open("Boards/board" + str(self.level) + "_1.txt", "w") as fp:
            fp.writelines('%s\n' % '\t'.join(items) for items in self.board_list)

    def get_new_board(self):
        self.new_board = []
        if "Boards/board" + str(self.level) + "_1.txt" in self.saved_boards_list:
            with open("Boards/board" + str(self.level) + "_1.txt") as file_in:
                for line in file_in:
                    self.new_board.append(line.split())
        else:
            with open("Boards/board" + str(self.level) + ".txt") as file_in:
                for line in file_in:
                    self.new_board.append(line.split())

    def get_prev_board(self):
        self.new_board = []
        with open("Boards/board" + str(self.level) + "_1.txt") as file_in:
            for line in file_in:
                self.new_board.append(line.split())
