import math

DISTANCE_PIXEL_CONVERSION = math.floor(1200/30)


def get_coordinates(road):
    x = None
    y = None
    h = None
    relative = None
    orientation = None

    # print(road)

    if road.start_connections['left'] is not None:
        if road.start_connections['left'].x is not None:
            x = road.start_connections['left'].x
            y = road.start_connections['left'].y
            h = road.start_connections['left'].h
            orientation = road.start_connections['left'].orientation
            relative = 'right'
            return x, y, h, relative, orientation

    if road.start_connections['right'] is not None:
        if road.start_connections['right'].x is not None:
            x = road.start_connections['right'].x
            y = road.start_connections['right'].y
            h = road.start_connections['right'].h
            orientation = road.start_connections['right'].orientation
            relative = 'left'
            return x, y, h, relative, orientation

    if road.start_connections['straight'] is not None:
        if road.start_connections['straight'].x is not None:
            x = road.start_connections['straight'].x
            y = road.start_connections['straight'].y
            h = road.start_connections['straight'].h
            orientation = road.start_connections['straight'].orientation
            relative = 'straight'
            return x, y, h, relative, orientation

    if road.end_connections['left'] is not None:
        if road.end_connections['left'].x is not None:
            x = road.end_connections['left'].x
            y = road.end_connections['left'].y
            h = road.end_connections['left'].h
            orientation = road.end_connections['left'].orientation
            relative = 'right'
            return x, y, h, relative, orientation

    if road.end_connections['right'] is not None:
        if road.end_connections['right'].x is not None:
            x = road.end_connections['right'].x
            y = road.end_connections['right'].y
            h = road.end_connections['right'].h
            orientation = road.end_connections['right'].orientation
            relative = 'left'
            return x, y, h, relative, orientation

    if road.end_connections['straight'] is not None:
        if road.end_connections['straight'].x is not None:
            x = road.end_connections['straight'].x
            y = road.end_connections['straight'].y
            h = road.end_connections['straight'].h
            orientation = road.end_connections['straight'].orientation
            relative = 'straight'
            return x, y, h, relative, orientation

    return x, y, h, relative, orientation


def get_in_children_coordinates(road, road_width=20):
    coors = []
    children = []

    if road.start_connections['left'] is not None\
            and road.start_connections['left'].x is None:
        children.append(road.start_connections['left'].num)
        if road.orientation == 0:
            xl = road.x - road_width
            yl = road.y - road_width
            hl = road_width
            wl = road.start_connections['left'].distance * DISTANCE_PIXEL_CONVERSION
        else:
            xl = road.x + road_width
            yl = road.y + road.w
            hl = road.start_connections['left'].distance * DISTANCE_PIXEL_CONVERSION
            wl = road_width
        road.start_connections['left'].x = xl
        road.start_connections['left'].y = yl
        road.start_connections['left'].h = hl
        road.start_connections['left'].w = wl
        coors.append([xl, yl, hl, wl])

    if road.start_connections['right'] is not None \
            and road.start_connections['right'].x is None:
        children.append(road.start_connections['right'].num)
        if road.orientation == 0:
            xr = road.x - road.h
            yr = road.y - road.start_connections['right'].distance * DISTANCE_PIXEL_CONVERSION
            hr = road_width
            wr = road.start_connections['right'].distance * DISTANCE_PIXEL_CONVERSION
        else:
            xr = road.x - road.start_connections['right'].distance * DISTANCE_PIXEL_CONVERSION
            yr = road.y + road.w
            hr = road.start_connections['right'].distance * DISTANCE_PIXEL_CONVERSION
            wr = road_width
        road.start_connections['right'].x = xr
        road.start_connections['right'].y = yr
        road.start_connections['right'].h = hr
        road.start_connections['right'].w = wr
        coors.append([xr, yr, hr, wr])

    if road.start_connections['straight'] is not None \
            and road.start_connections['straight'].x is None:
        children.append(road.start_connections['straight'].num)
        if road.orientation == 0:
            xs = road.x - road_width - road.start_connections['straight'].distance * DISTANCE_PIXEL_CONVERSION
            ys = road.y
            hs = road.start_connections['straight'].distance * DISTANCE_PIXEL_CONVERSION
            ws = road_width
        else:
            xs = road.x
            ys = road.y + road_width + road.w
            hs = road_width
            ws = road.start_connections['straight'].distance * DISTANCE_PIXEL_CONVERSION
        road.start_connections['straight'].x = xs
        road.start_connections['straight'].y = ys
        road.start_connections['straight'].h = hs
        road.start_connections['straight'].w = ws
        coors.append([xs, ys, hs, ws])

    return children, coors

def get_children_coordinates(road, road_width=20):



    coors = []
    children = []

    if road.end_connections['left'] is not None \
            and road.end_connections['left'].x is None:
        children.append(road.end_connections['left'].num)
        if road.orientation == 0:
            xl = road.x + road.h
            yl = road.y - road.end_connections['left'].distance * DISTANCE_PIXEL_CONVERSION
            hl = road_width
            wl = road.end_connections['left'].distance * DISTANCE_PIXEL_CONVERSION
        else:
            xl = road.x - road.end_connections['left'].distance * DISTANCE_PIXEL_CONVERSION
            yl = road.y - road_width
            hl = road.end_connections['left'].distance * DISTANCE_PIXEL_CONVERSION
            wl = road_width
        road.end_connections['left'].x = xl
        road.end_connections['left'].y = yl
        road.end_connections['left'].h = hl
        road.end_connections['left'].w = wl
        coors.append([xl, yl, hl, wl])

    if road.end_connections['right'] is not None \
            and road.end_connections['right'].x is None:
        children.append(road.end_connections['right'].num)
        if road.orientation == 0:
            xr = road.x + road.h
            yr = road.y + road_width
            hr = road_width
            wr = road.end_connections['right'].distance * DISTANCE_PIXEL_CONVERSION
        else:
            xr = road.x + road_width
            yr = road.y - road_width
            hr = road.end_connections['right'].distance * DISTANCE_PIXEL_CONVERSION
            wr = road_width
        road.end_connections['right'].x = xr
        road.end_connections['right'].y = yr
        road.end_connections['right'].h = hr
        road.end_connections['right'].w = wr
        coors.append([xr, yr, hr, wr])

    if road.end_connections['straight'] is not None \
            and road.end_connections['straight'].x is None:
        children.append(road.end_connections['straight'].num)
        if road.orientation == 0:
            xs = road.x + road.h + road_width
            ys = road.y
            hs = road.end_connections['straight'].distance * DISTANCE_PIXEL_CONVERSION
            ws = road_width
        else:
            xs = road.x
            ys = road.y - road_width - road.end_connections['straight'].distance * DISTANCE_PIXEL_CONVERSION
            hs = road_width
            ws = road.end_connections['straight'].distance * DISTANCE_PIXEL_CONVERSION
        road.end_connections['straight'].x = xs
        road.end_connections['straight'].y = ys
        road.end_connections['straight'].h = hs
        road.end_connections['straight'].w = ws
        coors.append([xs, ys, hs, ws])

    children2, coors2 = get_in_children_coordinates(road)
    for i, child in enumerate(children2):
        if child not in children:
            children.append(child)
            coors.append(coors2[i])

    # print('On road: ', road.num)
    # print('setting location for', children)

    return children, coors


def get_new_direction(current_direction, turn):
    if current_direction == 0:
        if turn == 'left':
            return 90
        if turn == 'right':
            return 270
        if turn == 'straight':
            return 0
    if current_direction == 90:
        if turn == 'left':
            return 180
        if turn == 'right':
            return 0
        if turn == 'straight':
            return 90
    if current_direction == 180:
        if turn == 'left':
            return 270
        if turn == 'right':
            return 90
        if turn == 'straight':
            return 180
    if current_direction == 270:
        if turn == 'left':
            return 0
        if turn == 'right':
            return 180
        if turn == 'straight':
            return 270


def get_new_coordinates(road, turn, car):
    if car.current_direction == 0:
        if turn == 'left':
            return road.x, road.y+road.w
        if turn == 'right':
            return road.x+road.h, road.y
        else:
            return road.x, road.y
    if car.current_direction == 90:
        if turn == 'left':
            return road.x+road.h, road.y+road.w
        if turn == 'right':
            return road.x, road.y
        else:
            return road.x, road.y + road.w
    if car.current_direction == 180:
        if turn == 'left':
            return road.x+road.h, road.y
        if turn == 'right':
            return road.x, road.y+road.w
        else:
            return road.x+road.h, road.y + road.w
    else:
        if turn == 'left':
            return road.x, road.y
        if turn == 'right':
            return road.x+road.h, road.y + road.w
        else:
            return road.x+road.h, road.y


def calculate_apparent_distance(road):
    if road.traffic > road.capacity:
        return road.distance * (road.traffic-road.capacity)**0.23
    return road.distance
