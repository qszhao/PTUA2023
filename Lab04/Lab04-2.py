
class Graph:
    """My class for Lab04"""
    def __init__(self, gal_file):

        # get file name
        self.gal_file = gal_file


        # open and read gal file
        fp = open(gal_file)
        lines = fp.readlines()
        fp.close()
        self.lines = lines

        # build the dictionary
        line0 = lines[0]
        line0 = line0.strip().split()
        self.line0 = line0
        self.n_polygons = int(line0[1])
        neighbors = {}
        lines = lines[1:]
        processing = True 
        i = 0
        while i < self.n_polygons * 2:
            header = lines[i].strip().split()
            i_neighbors = lines[i+1].strip().split()
            node_i = header[0]
            neighbors[node_i] = i_neighbors
            i += 2
        self.neighbors = neighbors


        # answer questions under 2

    def summary(self):
        n_neighbors = 0
        mc = 0
        for node in self.neighbors:
            n_neighbors += len(self.neighbors[node])
            n_node = len(self.neighbors[node])
            if n_node > mc:
                mc = n_node


        average = n_neighbors * 1. / self.n_polygons
        results = {}
        results['average'] = average
        results['max card'] = mc

        return results


if __name__ == '__main__':

    my_gal = Graph("Lab04-1.gal")
