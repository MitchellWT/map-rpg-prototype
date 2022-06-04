import pygame


class MapSurface(pygame.Surface):
    def __init__(self, map_size, map_color, location_color, world_graph):
        super().__init__(map_size)
        self.location_color = location_color
        self.location_rect = pygame.Rect(0, 0, map_size[0] / 4, map_size[1] / 4)
        self.location_rect.center = (map_size[0] / 2, map_size[1] / 2)
        self.fill(map_color)

        traveled = []
        next_loc = []
        cur = world_graph.init_location
        pygame.draw.rect(self, self.location_color, self.location_rect)
        # TODO: graph traversal needs to be refactored
        # TODO: drawing is broken, add frontyard
        while len(traveled) != len(world_graph.init_location):
            if cur not in world_graph.graph:
                traveled.append(cur)
                cur = next_loc.pop()[0]
                continue
            for location in world_graph.graph[cur]:
                pygame.draw.rect(self, self.location_color, self.location_rect.move(location[1].to_coord()))
            traveled.append(cur)
            next_loc.extend(world_graph.graph[cur])
            old = cur
            cur = next_loc.pop()[0]
            for location in world_graph.graph[old]:
                if location[0] == cur:
                    self.location_rect.move_ip(location[1].to_coord())
                    break
