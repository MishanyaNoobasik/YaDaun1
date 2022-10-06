puzzle = [[0, 0, 0, 0, 1, 3, 8, 0, 4],
          [0, 5, 0, 0, 0, 6, 0, 9, 0],
          [0, 0, 0, 0, 9, 0, 0, 0, 5],
          [0, 0, 0, 0, 4, 2, 1, 0, 0],
          [0, 1, 5, 9, 0, 0, 0, 0, 0],
          [0, 4, 7, 0, 0, 5, 0, 6, 0],
          [0, 0, 8, 0, 5, 0, 0, 1, 2],
          [0, 0, 0, 0, 0, 0, 7, 0, 0],
          [0, 0, 0, 6, 0, 0, 0, 3, 8]]
from collections import Counter
import re


def sudoku(puz):
    for i in range(9):
        for j in range(9):
            if puz[i][j] == 0:
                puz[i][j] = ''
    quads = [[puz[0][0], puz[0][1], puz[0][2], puz[1][0], puz[1][1], puz[1][2], puz[2][0], puz[2][1], puz[2][2]],
             [puz[0][3], puz[0][4], puz[0][5], puz[1][3], puz[1][4], puz[1][5], puz[2][3], puz[2][4], puz[2][5]],
             [puz[0][6], puz[0][7], puz[0][8], puz[1][6], puz[1][7], puz[1][8], puz[2][6], puz[2][7], puz[2][8]],
             [puz[3][0], puz[3][1], puz[3][2], puz[4][0], puz[4][1], puz[4][2], puz[5][0], puz[5][1], puz[5][2]],
             [puz[3][3], puz[3][4], puz[3][5], puz[4][3], puz[4][4], puz[4][5], puz[5][3], puz[5][4], puz[5][5]],
             [puz[3][6], puz[3][7], puz[3][8], puz[4][6], puz[4][7], puz[4][8], puz[5][6], puz[5][7], puz[5][8]],
             [puz[6][0], puz[6][1], puz[6][2], puz[7][0], puz[7][1], puz[7][2], puz[8][0], puz[8][1], puz[8][2]],
             [puz[6][3], puz[6][4], puz[6][5], puz[7][3], puz[7][4], puz[7][5], puz[8][3], puz[8][4], puz[8][5]],
             [puz[6][6], puz[6][7], puz[6][8], puz[7][6], puz[7][7], puz[7][8], puz[8][6], puz[8][7], puz[8][8]]]
    stolbiki = []
    for j in range(9):
        stolb = []
        for i in range(9):
            stolb.append(puz[i][j])
        stolbiki.append(stolb)
    for i in range(9):
        for j in range(9):
            for k in range(1, 10):
                if puz[i][j] not in range(1, 10) and k not in puz[i] and k not in stolbiki[j] and k not in quads[j // 3 + i // 3 * 3]:
                    puz[i][j] = puz[i][j] + str(k)
    for i in range(9):
        for j in range(9):
            puz[i][j] = str(puz[i][j])
    a = 0
    for keks in range(10):
        quads = [[puz[0][0], puz[0][1], puz[0][2], puz[1][0], puz[1][1], puz[1][2], puz[2][0], puz[2][1], puz[2][2]],
                 [puz[0][3], puz[0][4], puz[0][5], puz[1][3], puz[1][4], puz[1][5], puz[2][3], puz[2][4], puz[2][5]],
                 [puz[0][6], puz[0][7], puz[0][8], puz[1][6], puz[1][7], puz[1][8], puz[2][6], puz[2][7], puz[2][8]],
                 [puz[3][0], puz[3][1], puz[3][2], puz[4][0], puz[4][1], puz[4][2], puz[5][0], puz[5][1], puz[5][2]],
                 [puz[3][3], puz[3][4], puz[3][5], puz[4][3], puz[4][4], puz[4][5], puz[5][3], puz[5][4], puz[5][5]],
                 [puz[3][6], puz[3][7], puz[3][8], puz[4][6], puz[4][7], puz[4][8], puz[5][6], puz[5][7], puz[5][8]],
                 [puz[6][0], puz[6][1], puz[6][2], puz[7][0], puz[7][1], puz[7][2], puz[8][0], puz[8][1], puz[8][2]],
                 [puz[6][3], puz[6][4], puz[6][5], puz[7][3], puz[7][4], puz[7][5], puz[8][3], puz[8][4], puz[8][5]],
                 [puz[6][6], puz[6][7], puz[6][8], puz[7][6], puz[7][7], puz[7][8], puz[8][6], puz[8][7], puz[8][8]]]
        stolbiki = []
        for j in range(9):
            stolb = []
            for i in range(9):
                stolb.append(puz[i][j])
            stolbiki.append(stolb)
        for i in range(9):
            for j in range(9):
                for k in range(1, 10):
                    if puz[i][j].count(str(k)) == 1 and ''.join(puz[i]).count(str(k)) == 1:
                        puz[i][j] = str(k)
                    if puz[i][j].count(str(k)) == 1 and ''.join(stolbiki[j]).count(str(k)) == 1:
                        puz[i][j] = str(k)
                    if puz[i][j].count(str(k)) == 1 and ''.join(quads[j // 3 + i // 3 * 3]).count(str(k)) == 1:
                        puz[i][j] = str(k)
        print(puz)
    for i in range(9):
        for j in range(9):
            puz[i][j] = int(puz[i][j])
    return puz


print(sudoku(puzzle))
