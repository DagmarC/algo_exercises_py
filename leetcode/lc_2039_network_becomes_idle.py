from typing import List
import deque


class Solution:
    def network_becomes_idle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        adj_list = self.create_adjacency_list(edges, len(patience))
        distances = self.bfs(adj_list, 0) # calculate distances from vertex 0 to all other vertices

        max_time = 0
        for i in range(1, n):
            rtt = 2*distances[i]  # round trip time (the time it takes for a message to be sent back and forth)
            messages_sent = (rtt - 1) // patience[i]  # number of messages sent before the first message is received
            last_message_time = messages_sent * patience[i]
            max_time = max(max_time, rtt + last_message_time)
        return max_time + 1  # earliest second starting from which the network becomes idle
    
    # bfs to calculate the minimum distance from the start_vertex to all other vertices
    def bfs(self, adj_list: List[List[int]], start_vertex: int) -> List[int]:
        n = len(adj_list)
        
        visited =[False for _ in range(n)]
        distances = [float('inf') for _ in range(n)]
        
        distances[0] = 0
        q = deque([0])
        while q:
            vertex = q.popleft()
            if visited[vertex]:
                continue # skip the vertex if it was already visited
            
            visited[vertex] = True
            
            # visit all unvisited neighbors of the vertex and calculate the minimum distance to them
            for neighbor in adj_list[vertex]:
                neighbor_distance = distances[vertex] + 1
                if not visited[neighbor] and neighbor_distance < distances[neighbor]:
                    distances[neighbor] = neighbor_distance
                    q.append(neighbor)
                    
        return distances
    
    
    def create_adjacency_list(self, edges: List[List[int]], n: int) -> List[List[int]]:
        adj_list = [[] for _ in range(n)]
        
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        return adj_list
    
    