# 0과 아파트의 인덱스 값 이용해서 거리를 구한다.
# 빈 중첩 리스트를 생성해 줄 때 반복문 활용 

def solution(city):
    # 0의 위치 정보를 position에 담아준다. 
    position = []

    for i in range(len(city)):
        for j in range(len(city[i])):
            if city[i][j] == 0:
                position.append(i)
                position.append(j)
                
    # 결과값을 담아줄 빈 리스트 생성
    result = [[0] * len(city[0]) for _ in range(len(city))]
    
    # 인덱스 값을 하나씩 순회하면서 0의 인덱스 값과의 차이를 넣어준다. 
    for i in range(len(city)):
        for j in range(len(city[i])):
            result[i][j] = abs(i - position[0]) + abs(j - position[1])

    return result

print(solution([[1, 0, 1], [1, 1, 1,], [1, 1, 1]]))



<정답코드>
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
