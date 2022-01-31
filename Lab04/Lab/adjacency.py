class Graph:
    def __init__(self, path):
        self.nodes = []

        with open(path, 'r') as file:
            lines = file.read().splitlines()
            for i in range(1, len(lines), 2):
                id = lines[i].split(' ')[0]
                num_neighbours = int(lines[i].split(' ')[1])
                neighbours = lines[i + 1].split(' ')
                if num_neighbours != len(neighbours):
                    raise RuntimeError(id)

                this = self.get_node_from_id(id)
                if this is None:
                    this = Node(id)
                    self.nodes.append(this)

                for n in neighbours:
                    neighbour_node = self.get_node_from_id(n)
                    if neighbour_node is None:
                        neighbour_node = Node(n)
                        self.nodes.append(neighbour_node)
                    this.add_neighbour(neighbour_node)

    def get_node_from_id(self, id):
        for n in self.nodes:
            if n.id == id:
                return n
        return None

    def avg_connectivity(self):
        return sum([len(n.neighbours) for n in self.nodes]) / len(self.nodes)

    def max_connectivity(self):
        max = 0
        max_nodes = []
        for node in self.nodes:
            if len(node.neighbours) > max:
                max = len(node.neighbours)
                max_nodes = []
            if len(node.neighbours) == max:
                max_nodes.append(node)
        return max, max_nodes

    def min_connectivity(self):
        head, *tail = self.nodes
        min = len(head.neighbours)
        min_nodes = [head]
        for node in tail:
            if len(node.neighbours) < min:
                min = len(node.neighbours)
                min_nodes = []
            if len(node.neighbours) == min:
                min_nodes.append(node)
        return min, min_nodes

    def islands(self):
        return [node for node in self.nodes if not node.neighbours]


class Node:
    def __init__(self, id):
        self.neighbours = []
        self.id = id

    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)
