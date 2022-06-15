import pygame.display


class Screen:
    def __init__(self, screen_size, small_map_surface, small_map_coord, big_map_surface):
        self.screen = pygame.display.set_mode(screen_size)
        self.surface_map = {}
        self.small_map = True

        self.small_map_surface = small_map_surface
        self.surface_map[small_map_surface] = small_map_coord
        self.big_map_surface = big_map_surface
        self.surface_map[big_map_surface] = (0, 0)

    def render(self):
        self.screen.fill((0, 0, 0))
        if self.small_map:
            self.screen.blit(self.small_map_surface, self.surface_map[self.small_map_surface])
        else:
            self.screen.blit(self.big_map_surface, self.surface_map[self.big_map_surface])

    def add_static(self, surface, blit_coord):
        self.surface_map[surface] = blit_coord
        self.screen.blit(surface, blit_coord)

    def check_point_collide(self, surface, coord):
        return surface.get_rect().move(self.surface_map[surface]).collidepoint(coord)

    def toggle_map(self):
        self.small_map = not self.small_map
