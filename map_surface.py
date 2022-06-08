import pygame


class MapSurface(pygame.Surface):
    def __init__(self, map_size, map_color, location_color, world_graph):
        super().__init__(map_size)
        self.location_color = location_color
        self.location_rect = pygame.Rect(0, 0, map_size[0] / 4, map_size[1] / 4)
        self.location_rect.center = (map_size[0] / 2, map_size[1] / 2)
        self.fill(map_color)
        self.render(world_graph)

    def render(self, world_graph):
        frontier = [(world_graph.init_location, None)]
        explored = {world_graph.init_location: self.location_rect.center}
        font = pygame.font.Font(None, 32)
        pygame.draw.rect(self, self.location_color, self.location_rect)
        text = font.render(world_graph.init_location, True, (0, 0, 0))
        self.blit(text, self.location_rect.center)
        while len(frontier) != 0:
            cur = frontier.pop(0)
            if cur[0] not in world_graph.graph:
                continue
            for location in world_graph.graph[cur[0]]:
                if location[0] in explored.keys():
                    continue
                frontier.append(location)
                self.location_rect.center = explored[cur[0]]
                self.location_rect.move_ip(location[1].to_coord())
                pygame.draw.rect(self, self.location_color, self.location_rect)
                text = font.render(location[0], True, (0, 0, 0))
                self.blit(text, self.location_rect.center)
                explored[location[0]] = self.location_rect.center
