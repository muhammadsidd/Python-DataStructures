class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    ##def __str__(self):
      ##  return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbors(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_neighbors(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, node):
        return self.adjacent[node]


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_Vertex = Vertex(node)
        self.vert_dict[node] = new_Vertex
        return new_Vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, fro, to, cost=0):
        if fro not in self.vert_dict:
            self.add_vertex(fro)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[fro].add_neighbors(self.vert_dict[to], cost)
        # self.vert_dict[to].add_neighbors(self.vert_dict[fro], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def pop_vert(self, node):
        return self.vert_dict.pop(node)

    def djkistra(self, frm, to):
        shortestdist = {}
        infinity = 99999
        predecessors = {}

        for node in self.vert_dict:
            shortestdist[node] = infinity
        
        shortestdist[frm] = 0
        print(shortestdist)
        
        while self.vert_dict:
            minNode = None

            for node in self.vert_dict:
                if minNode is None:
                    minNode = node
                elif shortestdist[node] < shortestdist[minNode]:
                    minNode = node

            for child in self.vert_dict[minNode].get_neighbors():
                print(minNode, child.id)
                if shortestdist[minNode] > self.vert_dict[minNode].get_weight(child):
                    shortestdist[minNode] = self.vert_dict[minNode].get_weight(child)
                

            self.pop_vert(minNode)
        print(shortestdist)


g = Graph()

g.add_vertex('a')
g.add_vertex('b')
g.add_vertex('c')
g.add_vertex('d')
g.add_vertex('e')
g.add_vertex('f')

g.add_edge('a', 'b', 7)
g.add_edge('a', 'c', 9)
g.add_edge('a', 'f', 14)
g.add_edge('b', 'c', 10)
g.add_edge('b', 'd', 9)
g.add_edge('c', 'd', 11)
g.add_edge('c', 'f', 2)
g.add_edge('d', 'e', 6)
g.add_edge('e', 'f', 9)
g.add_edge('f', 'a', 12)

for v in g:
    for w in v.get_neighbors():
        vid = v.get_id()
        wid = w.get_id()
        print(vid, wid, v.get_weight(w))

g.djkistra('c', 'f')
