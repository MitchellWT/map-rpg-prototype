import pygame

from location import Location
from world_graph import WorldGraph
from direction import Direction
from map_surface import MapSurface

location_list = [
    Location("Home", "This is my home"),
    Location("Backyard", "This is my backyard"),
    Location("River", "This is a river behind my house")
]

connector_list = [
    ("Home", "Backyard", Direction.DOWN),
    # ("Home", "Frontyard", Direction.UP),
    ("Backyard", "Home", Direction.UP),
    ("Backyard", "River", Direction.LEFT)
]

world_graph = WorldGraph(location_list, "Home", connector_list)

pygame.init()
screen = pygame.display.set_mode((500, 500))

map_size = (300, 300)
map_color = (50, 50, 50)
location_color = (100, 255, 100)

map_surface = MapSurface(map_size, map_color, location_color, world_graph)

gaming = True

while gaming:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gaming = False
    screen.blit(map_surface, (100, 100, 100, 100))
    pygame.display.flip()

pygame.quit()
