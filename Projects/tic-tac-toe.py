class tictactoe():
    def __init__(self) -> None:
        self.board = [["1","2","3"],["4","5","6"],["7","8","9"]]
        self.current = False
        self.round = 0
        print("Welcome to Tic Tac Toe")
        
        while True:
            if self.current == True:
                break
            elif self.round == 9:
                print("\nGAME TIE\n")
                break
            else:
                self.p1Choice()
            
            if self.current == True:
                break
            elif self.round == 9:
                print("\nGAME TIE\n")
                break
            else:
                self.p2Choice()

    def p1Choice(self): 
        self.round += 1
        self.Board()
        x = int(input("Player 1 (X) - Please choose one of these boxes: "))
        box = self.Choose(x)
        if self.isSelected(box) == True:
            print("\nYou can't choose the chosen one!\n")
            self.p1Choice()
        else:
            self.board[box[0]][box[1]] = "X"
            if self.gameControl(1) == True:
                print("GAME OVER")
                self.current = True
            else:
                pass

    def p2Choice(self):
        self.round += 1
        self.Board()
        y = int(input("Player 2 (O) - Please choose one of these boxes: "))
        box2 = self.Choose(y)
        if self.isSelected(box2) == True:
            print("\nYou can't choose the chosen one!\n")
            self.p2Choice()
        else:
            self.board[box2[0]][box2[1]] = "O"
            if self.gameControl(2) == True:
                print("GAME OVER")
                self.current = True
            else:
                pass

    def gameControl(self, a):
        # horizontal control
        if (self.board[0][0] == "X" and self.board[0][1] == "X" and self.board[0][2] == "X") or (self.board[0][0] == "O" and self.board[0][1] == "O" and self.board[0][2] == "O"):
            self.Board()
            print(f"Player {a} WIN!")
            return True
        elif (self.board[1][0] == "X" and self.board[1][1] == "X" and self.board[1][2] == "X") or (self.board[1][0] == "O" and self.board[1][1] == "O" and self.board[1][2] == "O"):
            self.Board()
            print(f"Player {a} WIN!")
            return True
        elif (self.board[2][0] == "X" and self.board[2][1] == "X" and self.board[2][2] == "X") or (self.board[2][0] == "O" and self.board[2][1] == "O" and self.board[2][2] == "O"):
            self.Board()
            print(f"Player {a} WIN!")
            return True
        # vertical control
        elif (self.board[0][0] == "X" and self.board[1][0] == "X" and self.board[2][0] == "X") or (self.board[0][0] == "O" and self.board[1][0] == "O" and self.board[2][0] == "O"):
            self.Board()
            print(f"Player {a} WIN!")
            return True
        elif (self.board[0][1] == "X" and self.board[1][1] == "X" and self.board[2][1] == "X") or (self.board[0][1] == "O" and self.board[1][1] == "O" and self.board[2][1] == "O"):
            self.Board()
            print(f"Player {a} WIN!")
            return True
        elif (self.board[0][2] == "X" and self.board[1][2] == "X" and self.board[2][2] == "X") or (self.board[0][2] == "O" and self.board[1][2] == "O" and self.board[2][2] == "O"):
            self.Board()
            print(f"Player {a} WIN!")
            return True
        # cross control
        elif (self.board[0][0] == "X" and self.board[1][1] == "X" and self.board[2][2] == "X") or (self.board[0][0] == "O" and self.board[1][1] == "O" and self.board[2][2] == "O"):
            self.Board()
            print(f"Player {a} WIN!")
            return True
        elif (self.board[0][2] == "X" and self.board[1][1] == "X" and self.board[2][0] == "X") or (self.board[0][2] == "O" and self.board[1][1] == "O" and self.board[2][0] == "O"):
            self.Board()
            print(f"Player {a} WIN!")
            return True
        else:
            pass

    def Board(self):
        print(f"{self.board[0][0]} {self.board[0][1]} {self.board[0][2]}\n{self.board[1][0]} {self.board[1][1]} {self.board[1][2]}\n{self.board[2][0]} {self.board[2][1]} {self.board[2][2]}")

    def isSelected(self, a):
        if self.board[a[0]][a[1]] == "X" or self.board[a[0]][a[1]] == "O":
            return True
        else:
            return False

    def Choose(self, b):
        if b == 1:
            return [0,0]
        elif b == 2:
            return [0,1]
        elif b == 3:
            return [0,2]
        elif b == 4:
            return [1,0]
        elif b == 5:
            return [1,1]
        elif b == 6:
            return [1,2]
        elif b == 7:
            return [2,0]
        elif b == 8:
            return [2,1]
        elif b == 9:
            return [2,2]


tic = tictactoe()