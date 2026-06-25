import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from scripts.Consts import C_WHITE, WIN_WIDTH, MENU_OPTION, C_PURPLE, TUTORIAL, FONT_PATH


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./assets/images/menu.png").convert_alpha()
        self.rect = self.surf.get_rect()

    def run(self):
        menu_option = 0
        pygame.mixer.music.load("./assets/audio/menu.mp3")
        pygame.mixer_music.play(-1)  # -1 para a musica rodar infinitamente

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(45, "Laços Cifrados", C_WHITE, ((WIN_WIDTH / 2), 70))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(30, MENU_OPTION[i], C_PURPLE, ((WIN_WIDTH / 2), 220 + 40 * i))
                else:
                    self.menu_text(30, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 220 + 40 * i))

            for i in range(len(TUTORIAL)):
                self.tutorial_text(10, TUTORIAL[i], C_PURPLE, ((WIN_WIDTH / 5), 200 + 25 * i))

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_w:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1


                    if event.key == pygame.K_RETURN:  # Enter
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font(FONT_PATH, size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


    # Define o ponto de ancoragem no canto inferior direito, o texto se expande para a esquerda.
    def tutorial_text(self, text_size: int, text: str, text_color: tuple, text_right_pos: tuple):
        text_font: Font = pygame.font.Font(FONT_PATH, size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(bottomright=text_right_pos)
        self.window.blit(source=text_surf, dest=text_rect)
