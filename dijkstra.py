import sys
class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] 
                      for row in range(vertices)]

    def min_distance(self, distance_array, visited):
        min_val = sys.maxint
        for i in range(self.V):
            if distance_array[i] < min_val and visited[i] == False:
                min_val = distance_array[i]
                min_index = i
        return min_index
            

    def dijkstra(self, src):
        distance_array = self.V*[sys.maxint]
        distance_array[src] = 0
        visited = self.V*[False]

        for _ in xrange(self.V):
            u = self.min_distance(distance_array, visited)
            visited[u] = True
            for j in xrange(self.V):
                if self.graph[u][j] > 0 and visited[j] == False and distance_array[j] > distance_array[u] + self.graph[u][j]:
                    distance_array[j] = distance_array[u] + self.graph[u][j]

        for node in range(self.V):
            print node, "\t", distance_array[node]
                        

def main():
    g  = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]
    g.dijkstra(0);

if __name__ == "__main__":
    main()
