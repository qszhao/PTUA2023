import matplotlib.pyplot as plt


def read_gal(path):
    out = {}
    with open(path, 'r') as file:
        lines = file.read().splitlines()
        for i in range(1, len(lines), 2):
            id = lines[i].split(' ')[0]
            num_neighbours = int(lines[i].split(' ')[1])
            neighbours = lines[i+1].split(' ')
            if num_neighbours != len(neighbours):
                raise RuntimeError(id)
            out[id] = neighbours
    return out


def gal_histogram(gal_dictionary):
    out = {}
    for id, neighbours in gal_dictionary.items():
        out[len(neighbours)] = out[len(neighbours)] + 1 if len(neighbours) in out.keys() else 1
    plt.hist([item for s in [[k]*v for k, v in out.items()] for item in s])
    plt.show()
    return out


def asymmetries(gal_dictionary):
    out = []
    for id, neighbours in gal_dictionary.items():
        for n in neighbours:
            if id not in gal_dictionary[n]:
                out.append([id, n])
    return out
