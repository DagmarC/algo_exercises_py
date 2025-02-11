from typing import List

def verify_sudoku_board(board: List[List[int]]) -> bool:
    row_set: List[Set[int]] = [set() for _ in range(9)]
    column_set: List[Set[int]] = [set() for _ in range(9)]
    subgrid: List[List[Set[int]]] = [[set() for _ in range(3)] for _ in range(3)] # 3x3 subgrid that contains sets of 9 elements
    
    for i, row in enumerate(board):
        for j, el in enumerate(row):
            if el == 0:
                continue  # 0 represents empty value
            if el in row_set[i]:
                return False
            if el in column_set[j]:
                return False
            if el in subgrid[i//3][j//3]:
                return False
            # Add element to all corresponding hash-sets: row, column and subgrid
            row_set[i].add(el)
            column_set[j].add(el)
            subgrid[i//3][j//3].add(el)
            
    return True
