import pygame
import math
from simulation import get_roads, Car
import my_utils
import numpy as np
import pygame.freetype  # Import the freetype module.


# PARAMETERS
DISTANCE_PIXEL_CONVERSION = math.floor(1200/30)
MARGIN = 1*DISTANCE_PIXEL_CONVERSION
ROAD_WIDTH = 20
START_X = 10
START_Y = 660//2
TERMINATION_ROAD = 6
ON_ROAD = 1
TERMINATED = 0

# initialize the thing
pygame.init()

# creating the mai screen
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Traffic Simulation")
GAME_FONT = pygame.font.SysFont(None, 24)

# parameters
road_color = (128, 140, 134)
car_color = (235, 64, 52)
white = (255, 255, 255)
yellow = (255, 255, 0)
green = (0, 255, 255)
orange = (255, 100, 0)
LOW = (127, 255, 0)
MEDIUM = (255, 255, 0)
HIGH = (255, 153, 0)
CAR_X = START_X
CAR_Y = START_Y

def generate_road(screen, x, y, h, w, color):
    # Drawing Rectangle
    pygame.draw.rect(screen, color,
                     pygame.Rect(x, y, h, w))


def generate_car(screen, x, y, r=6):
    pygame.draw.circle(screen, car_color, (x, y), r)


# get data for all roads
road_params = []
road_params_ix = []
roads = get_roads()

for road in roads:
    # Putting the first road
    if road.num == 1:
        # generate_road(screen, 0, 700//2 - MARGIN, road.distance)
        road_params.append([START_X, START_Y, road.distance*DISTANCE_PIXEL_CONVERSION, ROAD_WIDTH])
        road_params_ix.append(1)
        road.x = START_X
        road.y = START_Y
        road.h = road.distance*DISTANCE_PIXEL_CONVERSION
        road.w = ROAD_WIDTH

    if road.x is None:
        continue

    children, coor = my_utils.get_children_coordinates(road)

    for i, child in enumerate(children):
        if child not in road_params_ix:
            road_params_ix.append(child)
            road_params.append(coor[i])


cars = []
c = Car(START_X, START_Y)
cars.append(c)

current_time = pygame.time.get_ticks()
next_move = current_time + 1000


new_car_time = pygame.time.get_ticks()
new_car_time_delta = new_car_time + 5000

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((216, 240, 228))

    for j, param in enumerate(road_params):
        this_road = roads[road_params_ix[j]-1]
        if this_road.traffic < 0.75 * this_road.capacity:
            this_road_color = LOW
        elif this_road.traffic < 1.4 * this_road.capacity:
            this_road_color = MEDIUM
        else:
            this_road_color = HIGH
        generate_road(screen, param[0], param[1], param[2], param[3], this_road_color)
    current_time = pygame.time.get_ticks()

    # print cars
    for car in cars:
        generate_car(screen, car.x, car.y)

    if next_move <= current_time:
        # print('Helllloooooooo')
        for car in cars:

            if car.current_road == TERMINATION_ROAD:
                car.termination = True
                TERMINATED += 1
                ON_ROAD -= 1
                continue
            current_road = roads[car.current_road - 1]
            car.covered += current_road.step
            if car.covered >= car.to_cover:
                current_road.traffic -= 1
                current_road.apparent_distance = my_utils.calculate_apparent_distance(current_road)
                current_road.step = current_road.distance/current_road.apparent_distance
                choices = []
                if car.current_direction in [0, 90]:
                    if current_road.end_connections['left'] is not None:
                        choices.append('left')
                    if current_road.end_connections['right'] is not None:
                        choices.append('right')
                    if current_road.end_connections['straight'] is not None:
                        choices.append('straight')
                if car.current_direction in [180, 270]:
                    if current_road.start_connections['left'] is not None:
                        choices.append('left')
                    if current_road.start_connections['right'] is not None:
                        choices.append('right')
                    if current_road.start_connections['straight'] is not None:
                        choices.append('straight')
                next_turn = np.random.choice(choices)
                if car.current_direction in [0, 90]:
                    new_road = current_road.end_connections[next_turn]
                else:
                    new_road = current_road.start_connections[next_turn]
                new_road.traffic += 1
                new_road.apparent_distance = my_utils.calculate_apparent_distance(new_road)
                new_road.step = new_road.distance / new_road.apparent_distance
                car.current_road = new_road.num
                car.to_cover = new_road.apparent_distance
                car.covered = 0
                new_x, new_y = my_utils.get_new_coordinates(new_road, next_turn, car)
                car.x = new_x
                car.y = new_y
                car.current_direction = my_utils.get_new_direction(car.current_direction, next_turn)
            else:
                if car.current_direction == 0:
                    car.x += current_road.step*DISTANCE_PIXEL_CONVERSION
                elif car.current_direction == 90:
                    car.y -= current_road.step*DISTANCE_PIXEL_CONVERSION
                elif car.current_direction == 180:
                    car.x -= current_road.step*DISTANCE_PIXEL_CONVERSION
                else:
                    car.y += current_road.step*DISTANCE_PIXEL_CONVERSION
            generate_car(screen, car.x, car.y)

        next_move = current_time + 1000

    new_car_time = pygame.time.get_ticks()
    if new_car_time_delta <= new_car_time:
        new_car_time_delta = new_car_time + 5000
        c = Car(START_X, START_Y)
        cars.append(c)
        ON_ROAD += 1

    letter1 = GAME_FONT.render("On Road: " + str(ON_ROAD), True, orange)
    letter2 = GAME_FONT.render("Terminated: " + str(TERMINATED), False, orange)
    screen.blit(letter1, (10, 20))
    screen.blit(letter2, (10, 40))

    ## remove terminated cars
    cars = [car for car in cars if car.termination is False]
    pygame.display.update()


