def getAdjacentFields(table, row, column):
    adjacent = []
    col = column//3
    #Now we get rest the fields in its subset
    if row % 3 == 0: #top part
        nearbySubsets = [table[row][col], table[row+1][col], table[row+2][col]]
    elif row % 3 == 1: #middle part
        nearbySubsets = [table[row-1][col], table[row][col], table[row+1][col]]
    else: #bottom part
        nearbySubsets = [table[row-2][col], table[row-1][col], table[row][col]]
    #Now we add the numbers from the subsets to the adjacent, excluding duplicates
    for numSet in nearbySubsets:
        for num in numSet:
            if num not in adjacent:
                adjacent.append(num)
    #Now we just need to add numbers on the same row and same column
    #same row
    for group in table[row]:
        for num in group:
            if num not in adjacent:
                adjacent.append(num)
    #same column
    for row in table:
        num = row[col][column%3]
        if num not in adjacent:
                adjacent.append(num)
        
    return adjacent

#check if elem (num) is valid
def isValid(tab, row, col, num):
    
    return num not in getAdjacentFields(tab, row, col)

    

def solve(tab, index = 0):
    #if we are at the end of the table it means we solved it or its not possible to solve
    if index == 9*9:
        return True
    #translate index into row,col number
    row = index // 9
    col = index % 9 
    #we can go check next field if there is already a number here, as there is no need to check if it is valid, 
    #because there is no way that an invalid number gets written into array
    if tab[row][col//3][col%3] is not None:
        return solve(tab, index+1)
    
    for num in range(1,10):
        if isValid(tab, row, col, num):
            tab[row][col//3][col%3] = num
            if (solve(tab, index+1)):
                #if this number leads to solving the table we keep it
                return True
            #if it doesnt then we clear it and try another one    
            tab[row][col//3][col%3] = None
    return False
    




if __name__ == "__main__":
    from reader import readBoard

    board = [
    [[None, None, None], [None, None, None], [None, None, None]], 
    [[None, None, None], [None, None, None], [None, None, None]], 
    [[None, None, None], [None, None, None], [None, None, None]], 

    [[None, None, None], [None, None, None], [None, None, None]], 
    [[None, None, None], [None, None, None], [None, None, None]], 
    [[None, None, None], [None, None, None], [None, None, None]], 

    [[None, None, None], [None, None, None], [None, None, None]], 
    [[None, None, None], [None, None, None], [None, None, None]], 
    [[None, None, None], [None, None, None], [None, None, None]]]

    board = [
    [[4, None, None], [None, 5, None], [None, None, 8]], 
    [[None, None, None], [None, None, 2], [1, None, None]], 
    [[1, 5, None], [None, None, 6], [7, None, None]], 

    [[7, None, None], [None, None, None], [None, 5, None]], 
    [[None, None, 8], [3, None, None], [None, None, 1]], 
    [[None, None, None], [4, None, None], [None, 2, None]], 

    [[9, 6, 3], [None, None, 4], [None, None, None]], 
    [[None, None, None], [9, None, None], [2, None, None]], 
    [[None, None, None], [None, 1, None], [None, None, 3]]]
                    
    board = readBoard("board2");
    print("Board before")
    for index, row in enumerate(board):
        if index % 3 == 0:
            print("")
        print(row)

    print("\n")
    solve(board)

    print("Board after")
    for index, row in enumerate(board):
        if index % 3 == 0:
            print("")
        print(row)   

