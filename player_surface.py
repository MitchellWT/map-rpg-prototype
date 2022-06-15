import pygame


class PlayerSurface(pygame.Surface):
    def __init__(self, display_size, display_color, stat_color, player, size_factor):
        super().__init__(display_size)
        self.stat_color = stat_color
        self.player = player
        self.size_factor = size_factor
        self.stat_rect = pygame.Rect(0, 0, size_factor * 3, size_factor * 0.5)
        self.stat_rect.center = (display_size[0] / 2, 30)
        self.render(display_color)

    def render(self, display_color=(255, 255, 255)):
        self.fill(display_color)
        font = pygame.font.Font(None, 32)
        for key, val in self.player.__dict__.items():
            stat_text = "{}: {}".format(key, val)
            self.draw_stat(font, stat_text)
            self.stat_rect.move_ip((0, self.size_factor * 0.6))

    def draw_stat(self, font, stat_text):
        pygame.draw.rect(self, self.stat_color, self.stat_rect)
        text = font.render(stat_text, True, (0, 0, 0))
        text_rect = text.get_rect()
        # Centers text on rect
        self.blit(text, (
            self.stat_rect.left + (self.size_factor / 4),
            self.stat_rect.center[1] - (text_rect.height / 2)
        ))
