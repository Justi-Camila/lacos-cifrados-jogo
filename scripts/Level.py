import sys
from math import factorial

import pygame.time
from pygame import Surface, Rect
from pygame.font import Font

from scripts.Background import Background
from scripts.Consts import WIN_WIDTH, ENTITY_SPEED, WIN_HEIGHT, FONT_PATH, C_PURPLE
from scripts.Entity import Entity
from scripts.EntityFactory import EntityFactory
from scripts.Player import Player


class Level:

    def __init__(self, window: Surface, name: str, game_mode: str):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list:  list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + "Bg"))
        player = EntityFactory.get_entity("Player")
        self.entity_list.append(player)
        self.camera_x = 0
        self.camera_y = 0
        self.em_cutscene = True
        self.contagem = 0
        self.campfire = pygame.image.load("./assets/images/camp.png").convert_alpha()
        self.npc_1 = pygame.image.load("./assets/images/NPC1.png").convert_alpha()
        self.npc_2 = pygame.image.load("./assets/images/NPC2.png").convert_alpha()
        self.cenarios = [
            {"surf": pygame.image.load("./assets/images/paper.png").convert_alpha(), "pos_mundo": (50, 120)},
            {"surf": pygame.image.load("./assets/images/trap.png").convert_alpha(), "pos_mundo": (130, 100)},
        ]

    def run(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            if self.em_cutscene:
                self.camera_x = 0
            else:
                player = next(ent for ent in self.entity_list if isinstance(ent, Player))

                self.camera_x = player.rect.x - (WIN_WIDTH / 5)

            for ent in self.entity_list:
                if isinstance(ent, Player):
                    if not self.em_cutscene:
                        ent.move()
                    if self.em_cutscene:
                        ent.rect.x = 80

                    self.window.blit(ent.surf, (ent.rect.x - self.camera_x, ent.rect.y))
                elif isinstance(ent, Background):
                    factor = ENTITY_SPEED[ent.name] / 10

                    tela_x = -(self.camera_x * factor) % WIN_WIDTH

                    self.window.blit(ent.surf, (tela_x, ent.rect.y))
                    self.window.blit(ent.surf, (tela_x - WIN_WIDTH, ent.rect.y))
                    self.window.blit(ent.surf, (tela_x + WIN_WIDTH, ent.rect.y))

            if self.em_cutscene:
                self.window.blit(self.campfire, (0, 0))
                self.window.blit(self.npc_1, (WIN_WIDTH / 2 - 60, WIN_HEIGHT / 2 + 100))
                self.window.blit(self.npc_2, (WIN_WIDTH / 2 + 30, WIN_HEIGHT / 2 + 100))

                rect = pygame.draw.rect(self.window, C_PURPLE, (70, 70, 400, 100))

            for obj in self.cenarios:
                tela_x = obj["pos_mundo"][0] - self.camera_x
                tela_y = obj["pos_mundo"][1] - self.camera_y

                if -64 < tela_x < WIN_WIDTH + 64:
                    self.window.blit(obj["surf"], (tela_x, tela_y))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.em_cutscene:
                        self.em_cutscene = False

            pygame.display.flip()


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font(FONT_PATH, size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)