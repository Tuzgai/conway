import random

def TODO():
    print("whoops, not done yet")

class GameBoard:
    
    def __init__(self, size, seed):
        self.size = size
        self.seed = seed
        random.seed(seed)
        self.board = [[random.choice([0,1]) for i in range(size+5)] for j in range(size+5)]

    def update(self):
        new_board = [[0 for i in range(self.size+5)] for j in range(self.size+5)]

        for i in range(1, len(self.board)-1):
            for j in range(1, len(self.board)-1):
                neighbors = (self.board[i-1][j-1]
                + self.board[i-1][j]
                + self.board[i-1][j+1]
                + self.board[i][j-1]
                + self.board[i][j+1]
                + self.board[i+1][j-1]
                + self.board[i+1][j]
                + self.board[i+1][j+1])

                new_state = 0
                if(self.board[i][j] == 1 and neighbors == 2):
                    new_state = 1
                elif(neighbors == 3):
                    new_state = 1
                else:
                    new_state = 0

                new_board[i][j] = new_state         

        self.board = new_board

    def display(self):
        for i in range(len(self.board)):
            row = ""
            for j in range(len(self.board)):
                row += "." if self.board[i][j] == 0 else "X"
            print(row)
        print("\n")

    def get_twitter_content(self):
        output = ""
        for i in range(len(self.board)):
            row = ""
            for j in range(len(self.board)):
                row += "⬛️" if self.board[i][j] == 0 else "🟩"
            output += f"{row}\n"
        return output
        