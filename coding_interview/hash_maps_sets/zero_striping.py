from typing import List, Set

def zero_striping(matrix: List[List[int]]) -> None:
    if len(matrix) == 0:
        return
    
    hs_rows, hs_cols = find_zeros(matrix)
    # set all columns at specific rows to 0
    while len(hs_rows) != 0:
        row = hs_rows.pop()
        for j in range(len(matrix[row])):
            matrix[row][j] = 0
            
    # set all rows at specific columns to 0
    while len(hs_cols) != 0:
        col = hs_cols.pop()
        for i in range(len(matrix)):
            matrix[i][col] = 0
    
    
def find_zeros(matrix: List[List[int]]):
    n, m = len(matrix), len(matrix[0])

    hs_rows: Set[int] = set()
    hs_cols: Set[int] = set()
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                hs_rows.add(i)
                hs_cols.add(j)
    
    return hs_rows, hs_cols


if __name__ == "__main__":
    tc = [[1,2,3,4,5],[6,0,6,9,10],[11,12,13,14,15],[16,17,18,19,0]]
    print("before: ", tc)
    zero_striping(tc)
    print("after", tc)