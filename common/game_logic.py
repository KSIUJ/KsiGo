import string


class Board(object):
    def __init__(self, size=19):
        self.player_black_points = 0.0
        self.player_white_points = 7.5
        self.actual_turn = "black"
        self.size = size

        self.Matrix = [['*' for _ in range(self.size)] for _ in range(self.size)]
        self.groups = []
        self.passed_turn = 0

        self.ko_captive = (-1, -1)
        self.ko_beating = (-1, -1)

    def print_board(self):

        print("  ", end="")
        for k in range(self.size):
            print(string.ascii_uppercase[k], end=" ")

        print()
        for k in range(self.size):
            print(string.ascii_lowercase[k], end=" ")
            for l in range(self.size):
                print(self.Matrix[k][l], end=" ")
            print()
        print()

    def next_turn(self):
        if self.actual_turn == "black":
            self.actual_turn = "white"
        else:
            self.actual_turn = "black"

    def turn_is_passed(self, is_passed):
        if is_passed:
            self.next_turn()
            self.passed_turn += 1
        else:
            self.passed_turn = 0

    def update_board(self, x, y, color="*"):
        if color == "black":
            self.Matrix[x][y] = "b"
        elif color == "white":
            self.Matrix[x][y] = "w"
        else:
            self.Matrix[x][y] = "*"

    def search(self, point=None, points=[]):

        stones = []
        for group in self.groups:
            for stone in group.stones:
                if stone.point == point and not points:
                    return stone
                if stone.point in points:
                    stones.append(stone)
        return stones

    def update_liberties(self, added_stone=None, end_of_game_fix=False):

        for group in self.groups:
            if added_stone and group == added_stone.group:
                continue
            group.update_liberties(end_of_game_fix=end_of_game_fix)
        if added_stone:
            added_stone.group.update_liberties(end_of_game_fix=end_of_game_fix)

    def move_is_legal(self, row, col):
        if self.Matrix[row][col] != "*":
            return False

        if (row, col) == self.ko_captive:
            stone = self.search(point=self.ko_beating)
            lib = len(stone.group.liberties)
            abund = stone.group.abundance
            if abund == 1 and lib == 1:
                return False

        color = ""
        if self.actual_turn == "white":
            color = "w"
        elif self.actual_turn == "black":
            color = "b"

        if row > 0:
            if self.Matrix[row-1][col] == "*":
                return True
            elif self.Matrix[row-1][col] != color:
                stone = self.search(point=(row-1, col))
                lib = len(stone.group.liberties)
                if lib == 1:
                    if stone.group.abundance == 1:
                        if stone.blanc_neigh_fix():
                            self.ko_beating = (row, col)
                            self.ko_captive = (row-1, col)
                            return True
                    else:
                        return True
            elif self.Matrix[row-1][col] == color:
                stone = self.search(point=(row-1, col))
                lib = len(stone.group.liberties)
                if lib > 1:
                    return True
        if row < self.size - 1:
            if self.Matrix[row+1][col] == "*":
                return True
            elif self.Matrix[row+1][col] != color:
                stone = self.search(point=(row+1, col))
                lib = len(stone.group.liberties)
                if lib == 1:
                    if stone.group.abundance == 1:
                        if stone.blanc_neigh_fix():
                            self.ko_beating = (row, col)
                            self.ko_captive = (row + 1, col)
                            return True
                    else:
                        return True
            elif self.Matrix[row+1][col] == color:
                stone = self.search(point=(row+1, col))
                lib = len(stone.group.liberties)
                if lib > 1:
                    return True
        if col > 0:
            if self.Matrix[row][col-1] == "*":
                return True
            elif self.Matrix[row][col-1] != color:
                stone = self.search(point=(row, col-1))
                lib = len(stone.group.liberties)
                if lib == 1:
                    if stone.group.abundance == 1:
                        if stone.blanc_neigh_fix():
                            self.ko_beating = (row, col)
                            self.ko_captive = (row, col - 1)
                            return True
                    else:
                        return True
            elif self.Matrix[row][col-1] == color:
                stone = self.search(point=(row, col-1))
                lib = len(stone.group.liberties)
                if lib > 1:
                    return True
        if col < self.size - 1:
            if self.Matrix[row][col+1] == "*":
                return True
            elif self.Matrix[row][col + 1] != color:
                stone = self.search(point=(row, col + 1))
                lib = len(stone.group.liberties)
                if lib == 1:
                    if stone.group.abundance == 1:
                        if stone.blanc_neigh_fix():
                            self.ko_beating = (row, col)
                            self.ko_captive = (row, col + 1)
                            return True
                    else:
                        return True
            elif self.Matrix[row][col + 1] == color:
                stone = self.search(point=(row, col + 1))
                lib = len(stone.group.liberties)
                if lib > 1:
                    return True
        return False

    def count_points(self):
        for k in range(self.size):
            for l in range(self.size):
                if self.Matrix[k][l] == "*":

                    added_stone = Stone(board=self, point=(k, l), color="none")
                    self.update_liberties(added_stone=added_stone, end_of_game_fix=True)

        return self.player_black_points, self.player_white_points

    def lets_play(self):

        while self.passed_turn != 2:

            print("The current situation on the board")
            self.print_board()
            while True:
                print(f"Now is {self.actual_turn}'s turn")
                print(f"PASS or Col:", end=" ")
                col = input()
                if col == "PASS":
                    #self.turn_is_passed(True)
                    self.passed_turn += 1
                    self.ko_beating = (-1, -1)
                    self.ko_captive = (-1, -1)
                    break
                else:
                    col = ord(col) - 65
                    print(f"Row:", end=" ")
                    row = input()
                    row = ord(row) - 97
                    if self.move_is_legal(row=row, col=col):
                        #self.turn_is_passed(False)
                        self.passed_turn = 0
                        added_stone = Stone(board=self, point=(row, col), color=self.actual_turn)
                        self.update_liberties(added_stone=added_stone)
                        self.update_board(x=row, y=col, color=self.actual_turn)
                        if (row, col) != self.ko_beating:
                            self.ko_beating = (-1, -1)
                            self.ko_captive = (-1, -1)
                        break

                    else:
                        print("")
                        print("Wait, that's illegal")
                        print("Choose other Row and Col")

            self.next_turn()

        print(self.count_points())


class Stone(object):
    def __init__(self, board, point, color):

        self.board = board
        self.point = point
        self.color = color
        self.group = self.find_group()

        # self.board.update_board(x=self.point[0], y=self.point[1], color=self.color)

    def blanc_neigh_fix(self):
        blanc = 0
        if self.point[0] > 0:
            if self.board.Matrix[self.point[0] - 1][self.point[1]] == '*':
                blanc += 1
        if self.point[0] < self.board.size - 1:
            if self.board.Matrix[self.point[0] + 1][self.point[1]] == '*':
                blanc += 1
        if self.point[1] > 0:
            if self.board.Matrix[self.point[0]][self.point[1] - 1] == '*':
                blanc += 1
        if self.point[1] < self.board.size - 1:
            if self.board.Matrix[self.point[0]][self.point[1] + 1] == '*':
                blanc += 1
        if blanc <= 1:
            return True
        return False

    def remove(self):
        self.board.update_board(self.point[0], self.point[1])
        self.group.stones.remove(self)
        del self

    def return_point(self):
        return self.point

    @property
    def neighbors(self):

        neighboring = []

        if self.point[0] > 0:
            neighboring.append((self.point[0] - 1, self.point[1]))
        if self.point[0] < self.board.size - 1:
            neighboring.append((self.point[0] + 1, self.point[1]))
        if self.point[1] > 0:
            neighboring.append((self.point[0], self.point[1] - 1))
        if self.point[1] < self.board.size - 1:
            neighboring.append((self.point[0], self.point[1] + 1))

        return neighboring

    @property
    def liberties(self):
        liberties = self.neighbors
        stones = self.board.search(points=self.neighbors)
        for stone in stones:
            liberties.remove(stone.point)
        return liberties

    def find_group(self):
        groups = []
        stones = self.board.search(points=self.neighbors)
        for stone in stones:
            if stone.color == self.color and stone.group not in groups:
                groups.append(stone.group)

        if not groups:
            group = Group(self.board, self)
            return group
        else:
            if len(groups) > 1:
                for group in groups[1:]:
                    groups[0].merge(group)
            groups[0].stones.append(self)
            return groups[0]


class Group(object):
    def __init__(self, board, stone):

        self.board = board
        self.board.groups.append(self)
        self.stones = [stone]
        self.liberties = None
        self.abundance = 0

    def merge(self, group):

        for stone in group.stones:
            stone.group = self
            self.abundance += 1
            self.stones.append(stone)
        self.board.groups.remove(group)
        del group

    def remove(self):

        while self.stones:
            self.stones[0].remove()

        self.board.groups.remove(self)
        del self

    def update_liberties(self, end_of_game_fix=False):

        liberties = []
        col = ""
        count = 0.0
        for stone in self.stones:
            count += 1.0
            col = stone.color
            for liberty in stone.liberties:
                liberties.append(liberty)
        self.liberties = set(liberties)
        self.abundance = count
        if len(self.liberties) == 0 and col == "none":
            occupant_color = "*"
            only_one_occupant = True

            for stone in self.stones:
                if occupant_color == "*":
                    if stone.point[0] > 0:
                        occupant_color = self.board.Matrix[stone.point[0] - 1][stone.point[1]]
                    if stone.point[0] < self.board.size - 1:
                        tmp = self.board.Matrix[stone.point[0] + 1][stone.point[1]]
                        if occupant_color != "*" and tmp != "*" and occupant_color != tmp:
                            only_one_occupant = False
                            break
                        elif tmp != "*" and occupant_color == "*":
                            occupant_color = tmp
                    if stone.point[1] < self.board.size - 1:
                        tmp = self.board.Matrix[stone.point[0]][stone.point[1] + 1]
                        if occupant_color != "*" and tmp != "*" and occupant_color != tmp:
                            only_one_occupant = False
                            break
                        elif tmp != "*" and occupant_color == "*":
                            occupant_color = tmp
                    if stone.point[1] > 0:
                        tmp = self.board.Matrix[stone.point[0]][stone.point[1] - 1]
                        if occupant_color != "*" and tmp != "*" and occupant_color != tmp:
                            only_one_occupant = False
                            break
                        elif tmp != "*" and occupant_color == "*":
                            occupant_color = tmp
                else:

                    if stone.point[0] > 0:
                        neighbor_color = self.board.Matrix[stone.point[0] - 1][stone.point[1]]
                        if neighbor_color != "*" and neighbor_color != occupant_color:
                            only_one_occupant = False
                            break
                    if stone.point[0] < self.board.size - 1:
                        neighbor_color = self.board.Matrix[stone.point[0] + 1][stone.point[1]]
                        if neighbor_color != "*" and neighbor_color != occupant_color:
                            only_one_occupant = False
                            break
                    if stone.point[1] < self.board.size - 1:
                        neighbor_color = self.board.Matrix[stone.point[0]][stone.point[1] + 1]
                        if neighbor_color != "*" and neighbor_color != occupant_color:
                            only_one_occupant = False
                            break
                    if stone.point[1] > 0:
                        neighbor_color = self.board.Matrix[stone.point[0]][stone.point[1] - 1]
                        if neighbor_color != "*" and neighbor_color != occupant_color:
                            only_one_occupant = False
                            break
            if only_one_occupant:
                if occupant_color == "b":
                    self.board.player_black_points += count
                elif occupant_color == "w":
                    self.board.player_white_points += count
            self.remove()
        elif len(self.liberties) == 0 and not end_of_game_fix:
            if col == "black":
                self.board.player_white_points += count
            elif col == "white":
                self.board.player_black_points += count
                
            self.remove()
