class Graph:
    def __init__(self):
        self.adjacency_matrix = {}
        self.inverted_adjacency_matrix = {}
        self.visited = []
        self.out = []
        self.component = []

    def add_vertex(self, vertex_name):
        self.adjacency_matrix[vertex_name] = []

    def add_inv_vertex(self, vertex_name):
        self.inverted_adjacency_matrix[vertex_name] = []

    def add_edge(self, departure, destination):
        if departure not in self.adjacency_matrix:
            self.add_vertex(departure)
        if destination not in self.adjacency_matrix:
            self.add_vertex(destination)
        self.adjacency_matrix[departure].append(destination)

        if departure not in self.inverted_adjacency_matrix:
            self.add_inv_vertex(departure)
        if destination not in self.inverted_adjacency_matrix:
            self.add_inv_vertex(destination)
        self.inverted_adjacency_matrix[destination].append(departure)

    def direct_dfs(self, current):
        self.visited.append(current)
        for vertex in self.adjacency_matrix[current]:
            if vertex not in self.visited:
                self.direct_dfs(vertex)
        self.out.append(current)

    def reverse_dfs(self, current):
        self.visited.append(current)
        self.component.append(current)
        for vertex in self.inverted_adjacency_matrix[current]:
            if vertex not in self.visited:
                self.reverse_dfs(vertex)

    def find_num_of_components(self):
        for vertex in list(self.adjacency_matrix.keys()):
            self.visited = []
            graph.direct_dfs(vertex)
            print('visited during this iteration:', self.visited)
            if len(self.visited) == len(list(self.adjacency_matrix.keys())):
                print(vertex, ': start')
                break
            else:
                print(vertex, ': no luck')

        num = 0
        self.visited = []
        for vertex in self.out[::-1]:
            if vertex not in self.visited:
                graph.reverse_dfs(vertex)
                num += 1
                print(num, ':', graph.component)
                graph.component.clear()
        return num


if __name__ == '__main__':
    graph = Graph()

    graph.add_edge('1', '2')
    graph.add_edge('2', '3')
    graph.add_edge('3', '1')
    graph.add_edge('3', '4')
    graph.add_edge('4', '1')
    graph.add_edge('4', '2')
    graph.add_edge('4', '8')
    graph.add_edge('5', '4')
    graph.add_edge('5', '6')
    graph.add_edge('5', '8')
    graph.add_edge('6', '3')
    graph.add_edge('7', '3')
    graph.add_edge('7', '6')
    graph.add_edge('8', '7')

    print('adjacency_matrix:', graph.adjacency_matrix)

    print('number of components:', graph.find_num_of_components())
