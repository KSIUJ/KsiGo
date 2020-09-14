import string


class Player(object):
    def __init__(self, color, komi=0.0):
        self.color = color
        self.points = komi

    def add_points(self, new_points):
        self.points += new_points

    def return_points(self):
        return self.points


class Board(object):
    def __init__(self, player_black, player_white):
        self.player_black = player_black
        self.player_white = player_white
        self.actual_turn = "black"
        self.size = 19
        self.Matrix = [['*' for x in range(self.size)] for y in range(self.size)]
        self.groups = []
        self.passed_turn = 0

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
            if added_stone:
                if group == added_stone.group:
                    continue
            group.update_liberties(end_of_game_fix=end_of_game_fix)
        if added_stone:
            added_stone.group.update_liberties(end_of_game_fix=end_of_game_fix)

    def count_points(self):
        for k in range(self.size):
            for l in range(self.size):
                if self.Matrix[k][l] == "*":

                    added_stone = Stone(board=self, point=(k, l), color="none")
                    self.update_liberties(added_stone=added_stone, end_of_game_fix=True)

        if self.player_white.points > self.player_black.points:
            print(f"white won by {self.player_white.points - self.player_black.points}")
        elif self.player_white.points < self.player_black.points:
            print(f"black won by {self.player_black.points - self.player_white.points}")
        else:
            print("its draw")

        # print(f"w {self.player_white.points},b {self.player_black.points}")

    def lets_play(self):

        while self.passed_turn != 2:

            print("The current situation on the board")
            self.print_board()
            print(f"Now is {self.actual_turn}'s turn")
            print(f"PASS or Col:", end=" ")
            col = input()
            if col == "PASS":
                self.passed_turn += 1
            else:
                self.passed_turn = 0
                col = ord(col) - 65
                print(f"Row:", end=" ")
                row = input()
                row = ord(row) - 97

                added_stone = Stone(board=self, point=(row, col), color=self.actual_turn)
                self.update_liberties(added_stone=added_stone)
                self.update_board(x=row, y=col, color=self.actual_turn)

            self.next_turn()

        self.count_points()


class Stone(object):
    def __init__(self, board, point, color):

        self.board = board
        self.point = point
        self.color = color
        self.group = self.find_group()

        # self.board.update_board(x=self.point[0], y=self.point[1], color=self.color)

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
        if self.point[0] < 18:
            neighboring.append((self.point[0] + 1, self.point[1]))
        if self.point[1] > 0:
            neighboring.append((self.point[0], self.point[1] - 1))
        if self.point[1] < 18:
            neighboring.append((self.point[0], self.point[1] + 1))

        # neighboring = [(self.point[0] - 1, self.point[1]),
        #                (self.point[0] + 1, self.point[1]),
        #                (self.point[0], self.point[1] - 1),
        #                (self.point[0], self.point[1] + 1)]
        # for point in neighboring:
        #     if not 0 <= point[0] < 19 or not 0 <= point[1] < 19:
        #         neighboring.remove(point)
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

    def merge(self, group):

        for stone in group.stones:
            stone.group = self
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
        if len(self.liberties) == 0 and col == "none":
            occupant_color = "*"
            only_one_occupant = True

            for stone in self.stones:
                if occupant_color == "*":
                    if stone.point[0] > 0:
                        occupant_color = self.board.Matrix[stone.point[0] - 1][stone.point[1]]
                    if stone.point[0] < 18:
                        tmp = self.board.Matrix[stone.point[0] + 1][stone.point[1]]
                        if occupant_color != "*" and tmp != "*" and occupant_color != tmp:
                            only_one_occupant = False
                            break
                        elif tmp != "*" and occupant_color == "*":
                            occupant_color = tmp
                    if stone.point[1] < 18:
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
                    if stone.point[0] < 18:
                        neighbor_color = self.board.Matrix[stone.point[0] + 1][stone.point[1]]
                        if neighbor_color != "*" and neighbor_color != occupant_color:
                            only_one_occupant = False
                            break
                    if stone.point[1] < 18:
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
                    self.board.player_black.add_points(new_points=count)
                elif occupant_color == "w":
                    self.board.player_white.add_points(new_points=count)
            self.remove()
        elif len(self.liberties) == 0 and not end_of_game_fix:
            if col == "black":
                self.board.player_white.add_points(new_points=count)
            elif col == "white":
                self.board.player_black.add_points(new_points=count)
            self.remove()


if __name__ == '__main__':
    czarny = Player(color="black")
    bialy = Player(color="white", komi=5.5)
    theBoard = Board(player_black=czarny, player_white=bialy)
    theBoard.lets_play()
