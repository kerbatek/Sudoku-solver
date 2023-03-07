import cv2 as cv
import sys
import numpy as np
import pytesseract

img = cv.imread(cv.samples.findFile("board2.png"))
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
if img is None:
    sys.exit("Could not read the image.")
#cv.imshow("Display window", img)
r, c, channels = img.shape
row_part = r//9 
col_part = c//9 
cut = 23
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
def readBoard(good, bad):
    for row in range(9):
        for col in range(9):
            image = img[row_part*(row)+cut:row_part*(row+1)-cut, col_part*(col)+cut:col_part*(col+1)-cut]
            text = pytesseract.image_to_string(image, config='--psm 6 -c tessedit_char_whitelist=123456789')
        # cv.imshow(str(row) + " " + str(col) + " " +text, image)
            #cv.waitKey(0)
            if text == "":
                continue
            else:
                board[row][col//3][col%3] = text[0]
    print("Board after")
    for index, row in enumerate(board):
        if index % 3 == 0:
            print("")
        print(row)  
    if board == good_board:
        good += 1
        print("good")
    else:
        bad += 1
        print("Bad")
    print("GOOD:", good, "BAD:", bad, "ACC", good/(good+bad)*100, "%")
    readBoard(good, bad)
readBoard(0, 0)