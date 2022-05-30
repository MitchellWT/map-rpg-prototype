import pygame


class MapSurface(pygame.Surface):
    def __init__(self, map_size, map_color, location_color, world_graph):
        super().__init__(map_size)
        self.location_color = location_color
        self.location_rect = pygame.Rect(0, 0, map_size[0] / 4, map_size[1] / 4)
        self.location_rect.center = (map_size[0] / 2, map_size[1] / 2)
        self.fill(map_color)

        for location in world_graph.graph.keys():
            for connection in world_graph.graph[location]:
                # Draw rects based on graph nodes, use:
                # pygame.draw.rect(self, self.location_color, self.location_rect)
                pass
