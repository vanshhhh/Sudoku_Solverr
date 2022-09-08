import numpy as np
sudoku = [] #emptylist
print("Please use 0 in place of blank spaces")
for i in range(9): #9rows
    row = list(input("Enter the elements of row {} without any spaces and commas: ".format(i+1))) 
    row = [int(i) for i in row] #bydef string so covert it to integer by using list comprehension
    sudoku.append(row) #append emptylist
print(np.matrix(sudoku)) #show result in matrix format

#create function to check value is true or false
def possible(y,x,n): #row,col,no. check
    global sudoku
    for i in range(0,9):
        if sudoku[y][i] == n: #row
            return False
    for i in range(0,9):
        if sudoku[i][x] == n: #column
            return False
            
            #check in 3x3 box
    box_y = (y//3)*3  
    box_x = (x//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if sudoku[box_y+i][box_x+j]==n:
                return False
    return True
    
    
def solve():
    for y in range(0,9):
        for x in range(0,9):
            if sudoku[y][x] == 0: #check for blank spaces
                for n in range(1,10): #exclude second so 10
                    if possible(y,x,n): 
                        sudoku[y][x] = n
                        solve() #recusrion
                        sudoku[y][x] = 0
                return
    print(np.matrix(sudoku))
    
solve()