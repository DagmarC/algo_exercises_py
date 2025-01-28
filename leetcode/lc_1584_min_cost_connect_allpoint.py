from typing import List
import heapq
# This implementation ensures that the minimum cost to connect all points is found using Prim's algorithm with a priority queue.

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        visited = [False for _ in range(len(points))]
        priority_queue = []
        
        heapq.heappush(priority_queue, (0, 0)) # choose 1st elenent as the starting point
        edge = 0
        
        minimum_cost = 0
        while edge < len(points):
            cost, vertex = heapq.heappop(priority_queue)
            if visited[vertex]:
                continue # vertex already visited
            
            visited[vertex] = True
            edge += 1
            minimum_cost += cost
            
            for neighbor in range(len(points)):
                if not visited[neighbor]:
                    distance = self.manhattan_distance(points[vertex], points[neighbor])
                    heapq.heappush(priority_queue, (distance, neighbor))

        return minimum_cost
    
    def manhattan_distance(self, x: List[int], y: List[int]) -> int:
        return abs(x[0] - y[0]) + abs(x[1] - y[1])
    

def main():
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    solution = Solution()
    result = solution.minCostConnectPoints(points)
    print(f"Minimum cost to connect all points: {result}")

if __name__ == "__main__":
    main()