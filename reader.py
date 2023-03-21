import cv2 as cv
import sys
import numpy as np
import pytesseract

good_board = [
[[None, None, '7'], [None, '8', '4'], [None, None, None]],
[['9', '6', None], ['7', None, None], ['1', None, None]],
[[None, None, None], [None, '1', None], [None, '3', '2']],
[['1', None, '8'], [None, '4', None], ['3', '6', None]],
[['7', None, None], [None, None, '1'], ['8', None, None]],
[[None, '9', None], [None, None, '6'], [None, '7', None]],
[[None, '7', None], ['4', None, None], [None, '1', None]],
[[None, None, '9'], ['1', None, '5'], ['4', None, '3']],
[['8', '4', None], ['9', None, None], [None, None, None]],
]
def readBoard(path, cut = 23):
    # Get image from file and apply filters to it
    img = cv.imread(cv.samples.findFile(path+".png"))
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    if img is None:
        sys.exit("Could not read the image.")
    # Divide the image into 9x9 grid
    row, col, channels = img.shape
    row_size = row//9 
    col_size = col//9 
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
    # Go through every cell and recognise the number in the cell
    for row in range(9):
        for col in range(9):
            
            #row_size x row + cut : row_size x row+1 - cut
            #row_size - size of one row
            #x row - used to iterate each row
            #cut - adjustment
            image = img[row_size*(row)+cut:row_size*(row+1)-cut, col_size*(col)+cut:col_size*(col+1)-cut]
            #recognise the digit
            text = pytesseract.image_to_string(image, config='--psm 6 -c tessedit_char_whitelist=123456789')
            if text == "":
                continue
            else:
                board[row][col//3][col%3] = int(text[0])
    return board

if(__name__ == "__main__"):  
    print(readBoard("board2"))