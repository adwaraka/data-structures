#All Graph related stuff
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, src, dest):
        src = str(src)
        dest = str(dest)
        try:
            self.graph[src].append(dest)
        except:
            self.graph[src] = list(dest)

    def bfs(self, src):
        visited, queue = [], []
        src = str(src)

        queue.extend(self.graph[src])
        visited.append(src)
        print src, queue
        while len(queue) > 0:
            temp = queue.pop(0)
            if temp not in visited and temp is not None:
                print temp, queue
                visited.append(temp)
                if temp in self.graph:
                    queue.extend(self.graph[temp])

    def dfs(self, src, dest):
        visited, stack = [], []
        src = str(src)
        dest = str(dest)

        stack.extend(self.graph[src])
        visited.append(src)
        print src, stack
        while len(stack) > 0:
            temp = stack.pop()
            if temp not in visited and temp is not None:
                print temp, stack
                if temp == dest:
                    break
                visited.append(temp)
                if temp in self.graph:
                    stack.extend(self.graph[temp])

def main():
    g = Graph()
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,2)
    g.add_edge(2,0)
    g.add_edge(2,3)
    g.add_edge(3,4)
    g.add_edge(3,5)
    g.add_edge(3,6)
    g.add_edge(4,7)
    g.add_edge(7,0)
    print "BFS"
    g.bfs(3)
    print
    print "DFS"
    g.dfs(2, 7)

if __name__ == "__main__":
    main()