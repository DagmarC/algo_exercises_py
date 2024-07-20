from typing import List
import heapq


class Solution:
    def network_becomes_idle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        adj_list = self.create_adjacency_list(edges, len(patience))
        distances = self.dijkstra(adj_list, 0) # calculate distances from vertex 0 to all other vertices
        
        max_time = 0
        for i in range(1, n):
            rtt = 2*distances[i]  # round trip time (the time it takes for a message to be sent back and forth)
            messages_sent = (rtt - 1) // patience[i]  # number of messages sent before the first message is received
            last_message_time = messages_sent * patience[i]
            max_time = max(max_time, rtt + last_message_time)
        return max_time + 1  # earliest second starting from which the network becomes idle
    
    # Dijkstra's algorithm to calculate the shortest path from the start vertex to all other vertices, considering the edges as unweighted and the graph is connected   
    def dijkstra(self, adj_list: List[List[int]], start_vertex: int) -> List[int]:
        n = len(adj_list)
        
        visited =[False for _ in range(n)]
        distances = [float('inf') for _ in range(n)]
        
         # Initialize the heap directly as a list of tuples (distance, vertex)
        heap = [(0, start_vertex)] 
        while heap:
            current_distance, vertex = heapq.heappop(heap) # get the vertex with the smallest distance
            if visited[vertex]:
                continue # skip the vertex if it was already visited
            
            visited[vertex] = True
            
            # visit all unvisited neighbors of the vertex and calculate the minimum distance to them
            for neighbor in adj_list[vertex]:
                neighbor_distance = current_distance + 1
                if not visited[neighbor] and neighbor_distance < distances[neighbor]:
                    distances[neighbor] = neighbor_distance
                    heapq.heappush(heap, (neighbor_distance, neighbor))
                    
        return distances
    
    
    def create_adjacency_list(self, edges: List[List[int]], n: int) -> List[List[int]]:
        adj_list = [[] for _ in range(n)]
        
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        return adj_list
    
    