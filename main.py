import pygame

from location import Location
from screen import Screen
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

small_map_size = (screen_size[0] / 4, screen_size[0] / 4)
big_map_size = (screen_size[0], screen_size[1])
map_color = (50, 50, 50)
location_color = (100, 255, 100)

small_map_surface = MapSurface(small_map_size, map_color, location_color, world_graph, 75)
big_map_surface = MapSurface(big_map_size, map_color, location_color, world_graph, 75)

screen = Screen(screen_size, small_map_surface, (0, screen_size[1] - small_map_size[1]), big_map_surface)
gaming = True

while gaming:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gaming = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if screen.small_map and screen.check_point_collide(small_map_surface, mouse_pos):
                screen.toggle_map()
            elif not screen.small_map and screen.check_point_collide(big_map_surface, mouse_pos):
                screen.toggle_map()
    screen.render()
    pygame.display.flip()

pygame.quit()
