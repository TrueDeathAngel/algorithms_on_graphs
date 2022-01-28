class Graph:
    def __init__(self):
        self.incidence_matrix = {}

    def add_vertex(self, name):
        self.incidence_matrix[name] = {}

    def add_edge(self, departure, destination, name):
        if departure not in self.incidence_matrix:
            self.add_vertex(departure)
        self.incidence_matrix[departure][name] = 1
        if destination not in self.incidence_matrix:
            self.add_vertex(destination)
        self.incidence_matrix[destination][name] = -1
        if departure == destination:
            self.incidence_matrix[destination][name] = 0

    def get_colors_dict(self):
        colors_dict = {}
        color = 0
        weight_dict = dict(sorted(
            map(lambda x: (x[0], len(x[1].keys())), self.incidence_matrix.items()),
            key=lambda item: item[1])[::-1])

        while list(filter(lambda k: k not in colors_dict, self.incidence_matrix.keys())):
            edge_black_list = []
            for v, e_d in self.incidence_matrix.items():
                if v in colors_dict and colors_dict[v] == color:
                    edge_black_list += e_d.keys()
            edge_black_list = list(set(edge_black_list))

            vertices = list(dict(filter(
                lambda x: x[0] not in colors_dict and not list(filter(
                    lambda edge: edge in edge_black_list, self.incidence_matrix[x[0]].keys())), weight_dict.items()))
                            .keys())

            if vertices:
                colors_dict[vertices[0]] = color
            else:
                color += 1

        return colors_dict

    def visualize(self):
        edge_list = []
        for v, e_d in self.incidence_matrix.items():
            edge_list += e_d.keys()
        edge_list = list(set(edge_list))

        import networkx as nx
        import matplotlib.pyplot as plt

        g = nx.DiGraph()

        for e in edge_list:
            departure = ''
            destination = ''
            for v, e_d in self.incidence_matrix.items():
                if e in e_d:
                    if e_d[e] == 1:
                        departure = v
                    elif e_d[e] == -1:
                        destination = v
                if departure and destination:
                    break
            g.add_edge(departure, destination)
        colors = []
        colors_dict = self.get_colors_dict()
        for node in g:
            colors.append(colors_dict[node])
        nx.draw(g, node_color=colors, with_labels=True)
        plt.show()


if __name__ == '__main__':
    graph = Graph()

    graph.add_edge('1', '2', '1->2')
    graph.add_edge('2', '3', '2->3')
    graph.add_edge('3', '4', '3->4')
    graph.add_edge('4', '5', '4->5')
    graph.add_edge('5', '1', '5->1')
    graph.add_edge('1', '6', '1->6')
    graph.add_edge('2', '7', '2->7')
    graph.add_edge('3', '8', '3->8')
    graph.add_edge('4', '9', '4->9')
    graph.add_edge('6', '9', '6->9')

    print(graph.get_colors_dict())

    graph.visualize()

