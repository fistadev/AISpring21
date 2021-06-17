import cv2
import numpy as np
import matplotlib.pyplot as plt

# print(f'OpenCV: {cv2.__version__}')


def imshow(img, enlarge = True, color = True):
    if enlarge:
        plt.figure(figsize=(15,10));
    if not color:
        plt.imshow(img, cmap='gray');
    else:
        plt.imshow(img[:,:,::-1]);
    plt.show()

sudoku = cv2.imread('img/sudoku.png')
sudoku_1 = cv2.imread('img/sudoku_1.png',0)
sudoku_ph = cv2.imread('img/sudoku-photo-2.jpg')
sudoku_ph_1 = cv2.imread('img/sudoku_1.jpg',0)


imshow(sudoku, False)

imshow(sudoku_ph, False)


# Create a rotation matrix to rotate the image by 45 degrees (using the center as the pivot point)
h, w = sudoku_ph.shape[:2]

x_center = w//2
y_center = h//2
rotation_matrix = cv2.getRotationMatrix2D((x_center,y_center), -15, 1,)

img_rot = cv2.warpAffine(sudoku_ph,rotation_matrix,(w,h))
imshow(img_rot)


# cropping image

cropped_sudoku = img_rot[110:620,180:810]
imshow(cropped_sudoku, False, False)

# threshold
cropped_sudoku_gray = cv2.cvtColor(cropped_sudoku,cv2.COLOR_BGR2GRAY)
ret, thr =cv2.threshold(cropped_sudoku_gray,127,255,cv2.THRESH_BINARY_INV)
# imshow(thr)

# canny
canny = cv2.Canny(cropped_sudoku_gray,100,200)
# imshow(canny)

# houghlines
lines = cv2.HoughLines(canny,1,np.pi/180,200)
# print(lines)


sudoku_copy = cropped_sudoku.copy()
for line in lines:
    for rho,theta in line:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(sudoku_copy,(x1,y1),(x2,y2),(0,255,0),2)

imshow(sudoku_copy)


# solving Sudoku

def findNextCellToFill(grid, i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if grid[x][y] == 0:
                return x, y
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                return x, y
    return -1, -1


def isValid(grid, i, j, e):
    rowOk = all([e != grid[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != grid[x][j] for x in range(9)])
        if columnOk:
            # finding the top left x,y co-ordinates of the section containing the i,j cell
            secTopX, secTopY = (
                3 * (i // 3),
                3 * (j // 3),
            )  # floored quotient should be used here.
            for x in range(secTopX, secTopX + 3):
                for y in range(secTopY, secTopY + 3):
                    if grid[x][y] == e:
                        return False
            return True
    return False


def solveSudoku(grid, i=0, j=0):
    i, j = findNextCellToFill(grid, i, j)
    if i == -1:
        return True
    for e in range(1, 10):
        if isValid(grid, i, j, e):
            grid[i][j] = e
            if solveSudoku(grid, i, j):
                return True
            # Undo the current cell for backtracking
            grid[i][j] = 0
    return False

