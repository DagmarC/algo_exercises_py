from typing import List
from collections import deque

# You are given an n x n integer matrix grid.
# 3x3 matrices -> k in sliding window is 3


class Solution:
    def largest_local(self, grid: List[List[int]]) -> List[List[int]]:
        k = 3
        # for each row in grid get the sliding window maximum in-place
        for row in grid:
            row[:] = self.sliding_window(row, k)
            
        # transpose grid matrix in-place (replace columns for rows and rows for columns)
        self.transposeMatrix(grid)
        
        # calculate column maximums in-place
        for row in grid:
            row[:] = self.sliding_window(row, k)
            
        # transpose grid back to original orientation 
        self.transposeMatrix(grid) 
        return grid

    def sliding_window(self, arr: List[int], k: int) -> List[int]:
        maximums = []
        q = deque()  # queue has indices of arr elements for current window of size k, index of the greatest element for current window of size k is at the top of the queue

        if k > len(arr):
            k = len(arr)
    
        for i in range(len(arr)):
            # remove an old index of an element from the queue, make sure all old indices are removed, but here in sliding window only one is being removoved
            while q and i-k >= q[0]:
                q.popleft()
            # top of the queue has to have the greatest element, so remove all queue elements smaller than the current one, go from the end of the queue (last inserted)
            while q and arr[q[-1]] < arr[i]:
                q.pop()
            # now we can freely enque current element
            q.append(i)
            
            # add element from the top of the queue, at least 1 element is in the queue, from the previous line
            if i-k+1 >= 0:
                maximums.append(arr[q[0]])
        
        return maximums
 
    def transposeMatrix(self, m: List[List[int]]) -> None:
        m[:] = [[row[i] for row in m] for i in range(len(m[0]))]
            

if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()

    # Define your grid
    # grid = [
    #     [1, 2, 3, 4],
    #     [5, 6, 7, 8],
    #     [9, 10, 11, 12],
    #     [13, 14, 15, 16]
    # ]
    
    grid = [
        [9, 9, 8, 1],
        [5, 6, 2, 4],
        [8, 2, 6, 4],
        [6, 2, 2, 2]
    ]
    
    print(solution.largest_local(grid))