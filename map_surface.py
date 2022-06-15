import pygame


class MapSurface(pygame.Surface):
    def __init__(self, map_size, map_color, location_color, world_graph, size_factor):
        super().__init__(map_size)
        self.location_color = location_color
        self.location_rect = pygame.Rect(0, 0, size_factor * 0.80, size_factor * 0.80)
        self.location_rect.center = (map_size[0] / 2, map_size[1] / 2)
        self.fill(map_color)
        self.render(world_graph, size_factor)

    def render(self, world_graph, size_factor):
        frontier = [(world_graph.init_location, None)]
        explored = {world_graph.init_location: self.location_rect.center}
        font = pygame.font.Font(None, 32)
        self.draw_tile(font, world_graph.init_location)
        while len(frontier) != 0:
            cur = frontier.pop(0)
            if cur[0] not in world_graph.graph:
                continue
            for location in world_graph.graph[cur[0]]:
                if location[0] in explored.keys():
                    continue
                frontier.append(location)
                self.location_rect.center = explored[cur[0]]
                self.location_rect.move_ip(location[1].to_coord(size_factor))
                self.draw_tile(font, location[0])
                explored[location[0]] = self.location_rect.center

    def draw_tile(self, font, location_text):
        pygame.draw.rect(self, self.location_color, self.location_rect)
        text = font.render(location_text, True, (0, 0, 0))
        text_rect = text.get_rect()
        # Centers text on tile
        self.blit(text, (
            self.location_rect.center[0] - (text_rect.width / 2),
            self.location_rect.center[1] - (text_rect.height / 2)
        ))
