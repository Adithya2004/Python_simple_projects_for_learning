import random
import re
class Board:
    def __init__(self,dim_size,num_bombs):
        self.dim_size=dim_size
        self.num_bombs=num_bombs
        self.board = self.makeNewBoard()
        self.values = self.assign_values()
        self.dug = set()
    def makeNewBoard(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        bombs_planted = 0
        while bombs_planted<self.num_bombs:
            loc = random.randint(0,self.dim_size**2-1)
            row = loc // self.dim_size
            col = loc % self.dim_size
            if board[row][col] == "*":
                continue
            board[row][col] = "*"
            bombs_planted+=1
            #print(bombs_planted)
        return board
    def assign_values(self):
        for i in range(self.dim_size):
            for j in range(self.dim_size):
                if self.board[i][j] == "*":
                    continue
                else:
                    self.board[i][j] = self.get_neighbour(i,j)
    def get_neighbour(self,i,j):
        num = 0
        for row in range(max(0,i-1),min(self.dim_size-1,i+1)+1):
            for col in range(max(0,j-1),min(self.dim_size-1,j+1)+1):
                if col == j and row == i:
                    continue
                if self.board[row][col] == "*":
                    num+=1
        #print(num)
        return num
    def dig(self,i,j):
        self.dug.add((i,j))
        if self.board[i][j]=="*":
            return False
        elif self.board[i][j]>0:
            return True
        for row in range(max(0,i-1),min(self.dim_size-1,i+2)):
            for col in range(max(0,j-1),min(self.dim_size-1,j+2)):
                if (row,col) in self.dug:
                    continue
                self.dig(row,col)
        return True
    def __str__(self):
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for i in range(self.dim_size):
            for j in range(self.dim_size):
                if (i,j) in self.dug:
                    visible_board[i][j] = str(self.board[i][j])
                else:
                    visible_board[i][j] = " "
        string_rep = ""
        width = []
        for idx in range(self.dim_size):
            columns = map(lambda x:x[idx],visible_board)
            width.append((len(max(columns,key=len))))
        indices = [i for i in range(self.dim_size)]
        indices_row = "    "
        cells = []
        for idx,col in enumerate(indices):
            format = '%-'+str(width[idx])+"s"
            cells.append(format%(col))
        indices_row += " ".join(cells)
        indices_row += "\n"
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f"{i} |"
            cells = []
            for idx,col in enumerate(row):
                format = '%-'+str(width[idx])+"s"
                cells.append(format%(col))
            string_rep += " ".join(cells)
            string_rep += "\n"
        str_len = int(len(string_rep)/self.dim_size)
        string_rep = indices_row+'-'*str_len +'\n'+string_rep+"-"*str_len
        return string_rep
        
        
        
def play(dim_size =10,num_bombs=10):
    board = Board(dim_size,num_bombs)
    safe =True
    while len(board.dug)<(board.dim_size**2-num_bombs):
        print(board)
        user_input = re.split(',(\\s)*',input("Where would you like to dig:Ip as row,col :"))
        row,col = int(user_input[0]),int(user_input[-1])
        if row<0 or col<0 or row>board.dim_size or col>board.dim_size:
            print("Invalid Input !!!Try Again !!!")
            continue
        safe = board.dig(row,col)
        if not safe:
            break
    if safe:
        print("Congrats !!! You WIn!!")
    else:
        print("You lose")
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)
#if __name__ = '__main__':
play()
    