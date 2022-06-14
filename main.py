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
    ("Home", "Frontyard", Direction.UP),
    ("Backyard", "Home", Direction.UP),
    ("Backyard", "River", Direction.LEFT),
    ("Backyard", "BBQ", Direction.RIGHT),
    ("River", "Tree", Direction.LEFT)
]

world_graph = WorldGraph(location_list, "Home", connector_list)

pygame.init()
screen_size = (1000, 720)  # Need to make tile spacing in map dependent on screen_size
screen = pygame.display.set_mode(screen_size)

map_size = (screen_size[0] / 4, screen_size[0] / 4)
map_color = (50, 50, 50)
location_color = (100, 255, 100)

map_surface = MapSurface(map_size, map_color, location_color, world_graph)

gaming = True

while gaming:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gaming = False
    # screen.blit(map_surface, ((screen_size[0] / 2) - map_size[0] / 2, (screen_size[1] / 2) - map_size[1] / 2))
    screen.blit(map_surface, (0, screen_size[1] - map_size[1]))
    pygame.display.flip()

pygame.quit()
