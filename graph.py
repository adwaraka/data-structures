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
        print src,

        queue.extend(self.graph[src])
        visited.append(src)
        while len(queue) > 0:
            temp = queue.pop(0)
            if temp not in visited and temp is not None:
                print temp,
                visited.append(temp)
                if temp in self.graph:
                    queue.extend(self.graph[temp])


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
    g.add_edge(4,7)
    g.add_edge(7,0)
    g.bfs(3)

if __name__ == "__main__":
    main()