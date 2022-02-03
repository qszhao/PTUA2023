class Graph:
    class Node:
        def __init__(self, node_id):
            self.neighbours = set()
            self.id = node_id

        def add_neighbour(self, neighbour):
            self.neighbours.add(neighbour)

        def __eq__(self, other):
            if isinstance(other, Graph.Node):
                return self.id == other.id
            else:
                return False

        def __hash__(self):
            return hash(self.id)

    def __init__(self, path):
        self.nodes = set()
        with open(path, 'r') as file:
            lines = file.read().splitlines()
            for i in range(1, len(lines), 2):
                node_id = lines[i].split(' ')[0]
                num_neighbours = int(lines[i].split(' ')[1])
                neighbours = lines[i + 1].split(' ')
                if num_neighbours != len(neighbours):
                    raise Exception(f"Error in input file: Node with the id "
                                    f"#{node_id} does not have given number of"
                                    f" neighbours")

                this = self._get_or_add_node(node_id)

                for n in neighbours:
                    neighbour_node = self._get_or_add_node(n)
                    this.add_neighbour(neighbour_node)

    def _get_or_add_node(self, node_id):
        new_node = self.Node(node_id)
        if new_node not in self.nodes:
            self.nodes.add(new_node)
        else:
            for old_node in self.nodes:
                new_node = old_node if old_node == new_node else new_node
        return new_node

    def avg_connectivity(self):
        return sum([len(n.neighbours) for n in self.nodes]) / len(self.nodes)

    def max_connectivity(self):
        max_num = 0
        max_nodes = set()
        for node in self.nodes:
            if len(node.neighbours) > max_num:
                max_num = len(node.neighbours)
                max_nodes = set()
            if len(node.neighbours) == max_num:
                max_nodes.add(node)
        return max_num, max_nodes

    def min_connectivity(self):
        head, *tail = self.nodes
        min_num = len(head.neighbours)
        min_nodes = {head}
        for node in tail:
            if len(node.neighbours) < min_num:
                min_num = len(node.neighbours)
                min_nodes = set()
            if len(node.neighbours) == min_num:
                min_nodes.add(node)
        return min_num, min_nodes

    def islands(self):
        return {node for node in self.nodes if not node.neighbours}
