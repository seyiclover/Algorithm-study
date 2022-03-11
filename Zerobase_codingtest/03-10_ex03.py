import numpy


def solution(city):
    """
    :param city: int[][]
    :return: int[][]
    """
    return calc_distance(city)


def calc_distance(city):
    apt_locations = []
    bus_locations = []

    get_locations(city, apt_locations, bus_locations)

    result = create_base_result(city)

    for apt_index in range(len(apt_locations)):
        apt_y = apt_locations[apt_index][0]
        apt_x = apt_locations[apt_index][1]
        for bus_index in range(len(bus_locations)):
            distance = get_distance(apt_locations[apt_index], bus_locations[bus_index])
            result[apt_y][apt_x] = distance if (result[apt_y][apt_x] == 0) else min(result[apt_y][apt_x], distance)

    return result


def get_locations(city, apt_locations, bus_locations):
    y_size = len(city)
    x_size = len(city[0])

    for y in range(y_size):
        for x in range(x_size):
            if city[y][x] == 1:
                apt_locations.append([y, x])
            else:
                bus_locations.append([y, x])


def create_base_result(city):
    y_size = len(city)
    x_size = len(city[0])

    return numpy.zeros(shape=(y_size, x_size), dtype=object).tolist()


def get_distance(apt_location, bus_location):
    return abs(apt_location[0] - bus_location[0]) + abs(apt_location[1] - bus_location[1])
