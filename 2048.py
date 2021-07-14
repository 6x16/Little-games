"""
This file is to practice how to make a 2048-playboard, exactly same question from FANOLab question set.
Created by Justin Lee, 15/4/2020
Progress: Completed, playable now. Finished at 11:14p.m.
"""


class Playboard2048:
    def __init__(self):
        self.row = 4
        self.col = 4
        self.field = [[0 for c in range(self.col)] for r in range(self.row)]

    def __generate_number(self):
        import random
        import math
        empty = []
        for r in range(self.row):
            for c in range(self.col):
                if self.field[r][c] == 0:
                    empty.append([r, c])
        [picked_r, picked_c] = random.choice(empty)
        max_ = 0
        for r in range(self.row):
            if max_ <= max(self.field[r]):
                max_ = max(self.field[r])
        self.field[picked_r][picked_c] = 2**(max(0, int(math.log(max_ + 0.00000001, 2)) - 1))

    def __check_stuck(self):
        stuck = True
        for r in range(self.row):
            for c in range(self.col):
                current = self.field[r][c]
                if 0 <= r < self.row - 1:
                    if current == self.field[r + 1][c]:
                        stuck = False
                if 0 < r <= self.row - 1:
                    if current == self.field[r - 1][c]:
                        stuck = False
                if 0 <= c < self.col - 1:
                    if current == self.field[r][c + 1]:
                        stuck = False
                if 0 < c <= self.col - 1:
                    if current == self.field[r][c - 1]:
                        stuck = False
        return stuck

    def get_maximum(self):
        max_ = 0
        for r in range(self.row):
            if max_ <= max(self.field[r]):
                max_ = max(self.field[r])
        return max_

    def show(self):
        for r in range(self.row):
            temp = self.field[r].copy()
            for i in range(len(temp)):
                if temp[i] == 0:
                    temp[i] = " "
            print(temp)

    def move_left(self):
        for r in range(self.row):
            diff = 0
            for c in range(self.col):
                if self.field[r][c] == 0:
                    diff += 1
                elif self.field[r][c] != 0 and diff > 0:
                    self.field[r][c - diff] = self.field[r][c]
                    self.field[r][c] = 0
        for r in range(self.row):
            for c in range(1, self.col):
                if self.field[r][c] == self.field[r][c - 1] and c != 0:
                    self.field[r][c - 1] += self.field[r][c]
                    self.field[r][c] = 0
                if self.field[r][c - 1] == 0:
                    self.field[r][c - 1] = self.field[r][c]
                    self.field[r][c] = 0

    def move_up(self):
        for c in range(self.col):
            diff = 0
            for r in range(self.row):
                if self.field[r][c] == 0:
                    diff += 1
                elif self.field[r][c] != 0 and diff > 0:
                    self.field[r - diff][c] = self.field[r][c]
                    self.field[r][c] = 0
        for c in range(self.col):
            for r in range(1, self.row):
                if self.field[r][c] == self.field[r - 1][c]:
                    self.field[r - 1][c] += self.field[r][c]
                    self.field[r][c] = 0
                if self.field[r - 1][c] == 0:
                    self.field[r - 1][c] = self.field[r][c]
                    self.field[r][c] = 0

    def move_right(self):
        for r in range(self.row):
            diff = 0
            for c in range(self.col - 1, -1, -1):
                if self.field[r][c] == 0:
                    diff += 1
                elif self.field[r][c] != 0 and diff > 0:
                    self.field[r][c + diff] = self.field[r][c]
                    self.field[r][c] = 0
        for r in range(self.row):
            for c in range(self.col - 2, -1, -1):
                if self.field[r][c] == self.field[r][c + 1]:
                    self.field[r][c + 1] += self.field[r][c]
                    self.field[r][c] = 0
                if self.field[r][c + 1] == 0:
                    self.field[r][c + 1] = self.field[r][c]
                    self.field[r][c] = 0

    def move_down(self):
        for c in range(self.col):
            diff = 0
            for r in range(self.row - 1, -1, -1):
                if self.field[r][c] == 0:
                    diff += 1
                elif self.field[r][c] != 0 and diff > 0:
                    self.field[r + diff][c] = self.field[r][c]
                    self.field[r][c] = 0
        for c in range(self.col):
            for r in range(self.row - 2, -1, -1):
                if self.field[r][c] == self.field[r + 1][c]:
                    self.field[r + 1][c] += self.field[r][c]
                    self.field[r][c] = 0
                if self.field[r + 1][c] == 0:
                    self.field[r + 1][c] = self.field[r][c]
                    self.field[r][c] = 0

    def play(self):
        exit_ = False
        stuck_ = False
        step = ""
        print("Generating a playboard...")
        while not exit_ and not stuck_:
            step = ""
            stuck_ = self.__check_stuck()
            if stuck_:
                self.show()
                print("Game over! You are stuck.")
                return
            self.__generate_number()
            self.show()
            while step == "":
                step = input("Your step (Up/Down/Left/Right/Exit): ")
                step = step.lower()
                if step == "exit":
                    print("Thanks for playing, now ending...")
                    return
                print(step)
                if step != "up" and step != "down" and step != "left" and step != "right":
                    step = ""
                    print("Only Up/Down/Left/Right/Exit is accepted... please re-input: ")
            if step == "left":
                self.move_left()
            elif step == "right":
                self.move_right()
            elif step == "up":
                self.move_up()
            elif step == "down":
                self.move_down()
            max_ = self.get_maximum()
            if max_ == 2048:
                self.show()
                print("You win!!!")
                return

game = Playboard2048()
game.play()



