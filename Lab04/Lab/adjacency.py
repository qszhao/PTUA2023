import statistics

class Graph:
    def __init__(self, filename = None):
        self.nodes = []

        if filename is not None:
            self.__init_from_file(filename)

    def __init_from_file(self, filename):
        gal_lines = open(filename, 'r').readlines()[1:]

        current_observation = None
        current_connectivity = None
    
        for line in gal_lines:
            split_line = line.split(" ")

            if current_observation is None:
                current_observation = int(split_line[0])
                current_connectivity = int(split_line[1])
                continue
            else:
                node = self.Node(current_observation)
                if current_connectivity > 0:
                    node.adjacents = list(map(int, line.split(" ")))
                self.nodes.append(node)

            current_observation = None
            current_connectivity = None

    def __enumerate_edges(self):
        return [len(node.adjacents) for node in self.nodes]

    class Node:
        def __init__(self, obs_id, adjacents = []):
            self.obs_id = obs_id
            self.adjacents = adjacents

        def __str__(self):
            return str(self.obs_id)

    class ConnectivityReport:
        def __init__(self, msg, value, nodes = None):
            self.msg = msg
            self.value = value
            self.nodes = nodes

        def __str__(self):
            report = "\n(Connectivity Report: " + str(self.msg) + " connectivity: " + str(self.value)
            if self.nodes is not None:
                report += ", node IDs: [" + ",".join(map(str, self.nodes)) + "]"
            return report + ")"

    def nodes_with_connectivity(self, conn):
        return [node for node in self.nodes if len(node.adjacents) == conn]

    def mean_connectivity(self):
        return self.ConnectivityReport("Mean", statistics.mean(self.__enumerate_edges()))

    def max_connectivity(self):
        max_conn = max(self.__enumerate_edges())
        return self.ConnectivityReport("Max", max_conn, self.nodes_with_connectivity(max_conn))

    def min_connectivity(self):
        min_conn = min([conn for conn in self.__enumerate_edges() if conn > 0])
        return self.ConnectivityReport("Min", min_conn, self.nodes_with_connectivity(min_conn))

    def disconnected_nodes(self):
        return list(map(str, self.nodes_with_connectivity(0))) if len(self.nodes_with_connectivity(0)) > 0 else None
