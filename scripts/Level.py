import sys
from math import factorial

import pygame.time
from pygame import Surface

from scripts.Background import Background
from scripts.Consts import WIN_WIDTH, ENTITY_SPEED
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
        # self.cenarios = [
        #     {"surf": pygame.image.load("./assets/images/player1.png").convert_alpha(), "pos_mundo": (50, 120)},
        #     {"surf": pygame.image.load("./assets/images/player2.png").convert_alpha(), "pos_mundo": (130, 100)},
        # ]

    def run(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            player = next(ent for ent in self.entity_list if isinstance(ent, Player))

            self.camera_x = player.rect.x - (WIN_WIDTH / 5)

            for ent in self.entity_list:
                if isinstance(ent, Player):
                    ent.move()
                    self.window.blit(ent.surf, (ent.rect.x - self.camera_x, ent.rect.y))
                elif isinstance(ent, Background):
                    factor = ENTITY_SPEED[ent.name] / 10

                    tela_x = -(self.camera_x * factor) % WIN_WIDTH

                    self.window.blit(ent.surf, (tela_x, ent.rect.y))
                    self.window.blit(ent.surf, (tela_x - WIN_WIDTH, ent.rect.y))
                    self.window.blit(ent.surf, (tela_x + WIN_WIDTH, ent.rect.y))


            # for obj in self.cenarios:
            #     tela_x = obj["pos_mundo"][0] - self.camera_x
            #     tela_y = obj["pos_mundo"][1] - self.camera_y
            #
                    # if -64 < tela_x < WIN_WIDTH + 64:
            #           self.window.blit(obj["surf"], (tela_x, tela_y))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
