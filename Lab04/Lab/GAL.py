def gal_to_dict(filepath):
    gal_lines = open(filepath, 'r').readlines()[1:]
    gal_dict = {}

    current_observation = None
    current_connectivity = None

    for line in gal_lines:
        split_line = line.split(" ")

        if current_observation is None:
            current_observation = int(split_line[0])
            current_connectivity = int(split_line[1])
            continue
        else:
            gal_dict[current_observation] = []
            if current_connectivity > 0:
                gal_dict[current_observation] = list(map(int, line.split(" ")))

        current_observation = None
        current_connectivity = None

    return gal_dict



def histogram(filepath):
    dictionary = gal_to_dict(filepath)
    histogram = {}

    for observation_id in dictionary:
        frequency = len(dictionary[observation_id])
        if frequency in histogram:
            histogram[frequency].append(observation_id)
        else:
            histogram[frequency] = [observation_id]

    return histogram



def has_asymmetries(filepath):
    dictionary = gal_to_dict(filepath)

    for observation_id in dictionary:
        neighbours = dictionary[observation_id]

        for neighbour in neighbours:
            if observation_id in dictionary[neighbour]:
                continue
            else:
                return True

    return False
