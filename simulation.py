from road_network import Network


class Road:
    def __init__(self, num, start_connections, end_connections, distance, capacity):
        self.num = num
        self.start_connections = start_connections
        self.end_connections = end_connections
        self.distance = distance
        self.capacity = capacity
        self.traffic = 0
        self.step = 1
        self.apparent_distance = distance
        self.orientation = None
        self.x = None
        self.y = None
        self.h = None
        self.w = None


    def get_start_connections(self):
        turns = ['left', 'right', 'straight']
        a = ''
        for turn in turns:
            if self.start_connections[turn] is not None:
                a = a + ':' + str(self.start_connections[turn].num)
        return a.strip()

    def get_end_connections(self):
        turns = ['left', 'right', 'straight']
        a = ''
        for turn in turns:
            if self.end_connections[turn] is not None:
                a = a + ':' + str(self.end_connections[turn].num)
        return a.strip()

    def __str__(self):
        return str(self.num) + ' - ' + 'Orientation: ' + str(self.orientation) \
               + '. Start: ' + self.get_start_connections() + '. End: ' + self.get_end_connections()

class Car:
    def __init__(self, x, y):
        self.current_road = 1
        self.current_direction = 0
        self.to_cover = 3
        self.covered = 0
        self.x = x
        self.y = y
        self.termination = False

    def __str__(self):
        return str(self.current_road) + '-' + str(self.x) + '-' + str(self.y)

roads = []

network = Network().get_network()

for n in network.keys():
    # print(network[n])
    r = Road(n, {}, {}, network[n]['distance'], network[n]['capacity'])
    roads.append(r)

print(len(roads))

for n in network.keys():
    road = roads[n-1]

    # road.start_connections = network[n]['in']
    turns = ['left', 'right', 'straight']
    for turn in turns:
        if len(network[n]['in'][turn]) > 0:
            road.start_connections[turn] = roads[network[n]['in'][turn][0] - 1]
        else:
            road.start_connections[turn] = None
        if len(network[n]['out'][turn]) > 0:
            road.end_connections[turn] = roads[network[n]['out'][turn][0] - 1]
        else:
            road.end_connections[turn] = None
    # road.end_connections = network[n]['out']

    if n == 1:
        road.orientation = 0

    if road.orientation is not None:
        turns = ['left', 'right', 'straight']
        for turn in turns:
            temp = road.start_connections[turn]
            if temp is not None:
                # print(temp)
                if temp.orientation is None:
                    if turn in ['left', 'right']:
                        temp.orientation = 90 - road.orientation
                    else:
                        temp.orientation = road.orientation
            temp = road.end_connections[turn]
            if temp is not None:
                # print(temp)
                if temp.orientation is None:
                    if turn in ['left', 'right']:
                        temp.orientation = 90 - road.orientation
                    else:
                        temp.orientation = road.orientation


# for road in roads:
#     print(road)

def get_roads():
    return roads