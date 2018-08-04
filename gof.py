import os
import time

from utils import (
    constrain,
    print_board,
)


INITIAL_BOARD = {
    (2, 20),
    (3, 18), (3, 20),
    (4, 8), (4, 9), (4, 16), (4, 17),
    (5, 7), (5, 11), (5, 16), (5, 17),
    (7, 2), (7, 3), (7, 6), (7, 10), (7, 12), (7, 13), (7, 18), (7, 20),
    (8, 6), (8, 12), (8, 20),
    (9, 7), (9, 11),
    (10, 8), (10, 9)
}


def get_neighbors_of(cell):
    """
    Return the neighbors of cell.
    """
    x = cell[0]
    y = cell[1]
    neighbors = set()
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if ( i, j) != cell:
                neighbors.add((i,j))

    return neighbors


def advance(board):
    """
    Advance the board one step and return it.
    """
    new_board = set()
    for cell in board:
        # your code below
        pass

    return new_board


def start(board, steps=100, size=20):
    for i in range(1, steps + 1):
        os.system('clear')
        print('step:', i, '/', steps)
        print_board(board, size)
        time.sleep(0.1)
        board = constrain(advance(board), size)


if __name__ == '__main__':
    start(INITIAL_BOARD)
