import sys

import pygame.time
from pygame import Surface, Rect, K_BACKSPACE
from pygame.font import Font

from scripts.Background import Background
from scripts.Consts import WIN_WIDTH, ENTITY_SPEED, WIN_HEIGHT, FONT_PATH, CUTSCENE, C_WHITE, C_BLACK
from scripts.Entity import Entity
from scripts.EntityFactory import EntityFactory
from scripts.EntityMediator import EntityMediator
from scripts.Jail import Jail
from scripts.NPC import NPC
from scripts.Paper import Paper
from scripts.Player import Player
from scripts.Trap import Trap


class Level:

    def __init__(self, window: Surface, name: str, game_mode: str):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list:  list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + "Bg"))

        player = EntityFactory.get_entity("Player")
        self.entity_list.append(player)

        papers = EntityFactory.get_entity("Paper")
        self.entity_list.extend(papers)

        traps = EntityFactory.get_entity("Trap")
        self.entity_list.extend(traps)

        jail = EntityFactory.get_entity("Jail")
        self.entity_list.append(jail)

        npc = EntityFactory.get_entity("NPC")
        self.entity_list.extend(npc)

        self.camera_x = 0
        self.camera_y = 0
        self.em_cutscene = True
        self.contagem = 0
        self.campfire = pygame.image.load("./assets/images/camp.png").convert_alpha()
        self.npc_1 = pygame.image.load("./assets/images/NPC1.png").convert_alpha()
        self.npc_2 = pygame.image.load("./assets/images/NPC2.png").convert_alpha()
        self.badending = pygame.image.load("./assets/images/badending.png").convert_alpha()
        self.badend = False
        self.papel_aberto = False
        self.resposta = ""
        self.enigma_resolvido = False
        self.enigma_aberto = False

    def run(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            player = next((ent for ent in self.entity_list if isinstance(ent, Player)), None)

            if self.em_cutscene:
                self.camera_x = 0
            else:
                if player is None:
                    self.badend = True
                else:
                    self.camera_x = player.rect.x - (WIN_WIDTH / 5)

            for ent in self.entity_list:
                if isinstance(ent, Player):
                    if not self.em_cutscene and not self.badend:
                        ent.move()
                    if self.em_cutscene:
                        ent.rect.x = 140
                    if ent.name == 'Player':
                        self.text(14, f"Player - Health {ent.health}", C_WHITE, (80, 20))
                        self.window.blit(ent.surf, (ent.rect.x - self.camera_x, ent.rect.y))

                elif isinstance(ent, Background):
                    factor = ENTITY_SPEED[ent.name] / 10

                    tela_x = -(self.camera_x * factor) % WIN_WIDTH

                    self.window.blit(ent.surf, (tela_x, ent.rect.y))
                    self.window.blit(ent.surf, (tela_x - WIN_WIDTH, ent.rect.y))
                    self.window.blit(ent.surf, (tela_x + WIN_WIDTH, ent.rect.y))

                elif isinstance(ent, (Trap, Paper, Jail, NPC)):
                    tela_x = ent.rect.x - self.camera_x

                    if -ent.rect.width < tela_x < WIN_WIDTH + 64:
                        self.window.blit(ent.surf, (tela_x, ent.rect.y))

                    if isinstance(ent, Paper) and player and not self.em_cutscene and not self.badend and not self.papel_aberto:
                        if player.rect.colliderect(ent.rect):
                            pos_x = tela_x + (ent.rect.width / 2)
                            pos_y = ent.rect.y - 40

                            self.text(20, "Aperte E para ler", C_WHITE, (pos_x, pos_y))

                    if isinstance(ent, Jail) and player and not self.em_cutscene and not self.badend and not self.papel_aberto and not self.enigma_resolvido:

                        if player.rect.colliderect(ent.rect):
                            pos_x = tela_x + (ent.rect.width / 2)
                            pos_y = ent.rect.y - 40

                            self.text(20, "Aperte E para interagir", C_WHITE, (pos_x, pos_y))


            if self.em_cutscene:
                self.window.blit(self.campfire, (0, 0))
                self.window.blit(self.npc_1, (WIN_WIDTH / 2 - 60, WIN_HEIGHT / 2 + 100))
                self.window.blit(self.npc_2, (WIN_WIDTH / 2 + 30, WIN_HEIGHT / 2 + 100))
                rect = pygame.draw.rect(self.window, C_BLACK, (70, 70, 400, 100))
                if self.contagem < len(CUTSCENE):
                    self.text(12, CUTSCENE[self.contagem], C_WHITE, rect.center)

            if self.badend:
                self.window.blit(self.badending, (0, 0))
                self.text(22, "GAME", C_WHITE, (WIN_WIDTH / 2, 70))
                self.text(22, "OVER", C_WHITE, (WIN_WIDTH / 2, 120))
                self.text(15, "Aperte ESC para recomeçar", C_WHITE, (WIN_WIDTH/ 2, WIN_HEIGHT / 2 + 150))

            if self.papel_aberto:
                largura, altura = 500, 150
                x_caixa = (WIN_WIDTH - largura) / 2
                y_caixa = (WIN_HEIGHT - altura) / 2
                pygame.draw.rect(self.window, C_BLACK, (x_caixa, y_caixa, largura, altura))
                self.text(14, self.papel_aberto, C_WHITE, (WIN_WIDTH / 2, WIN_HEIGHT / 2))

            if self.enigma_aberto:
                largura, altura = 500, 150
                x_caixa = (WIN_WIDTH - largura) / 2
                y_caixa = (WIN_HEIGHT - altura) / 2
                pygame.draw.rect(self.window, C_BLACK, (x_caixa, y_caixa, largura, altura))
                self.text(14, self.enigma_aberto, C_WHITE, (WIN_WIDTH / 2, WIN_HEIGHT / 2))
                self.text(14, self.resposta, C_WHITE, (WIN_WIDTH / 2, WIN_HEIGHT / 2 + 50))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e and self.em_cutscene:
                        self.contagem += 1
                        if self.contagem >= len(CUTSCENE):
                            self.em_cutscene = False

                    if event.key == pygame.K_ESCAPE and self.badend:
                        return

                    # Evento de teclado do papel
                    if (event.key == pygame.K_e or event.key == pygame.K_ESCAPE) and self.papel_aberto:
                            self.papel_aberto = False

                    elif event.key == pygame.K_e and not self.papel_aberto:
                        if player:
                            for ent in self.entity_list:
                                if isinstance(ent, Paper):
                                    if player.rect.colliderect(ent.rect):
                                        self.papel_aberto = ent.text

                    #Evento de teclado do enigma
                    if self.enigma_aberto:
                        if event.key == pygame.K_e or event.key == pygame.K_ESCAPE:
                            self.enigma_aberto = False
                        elif event.key == K_BACKSPACE:
                            self.resposta = self.resposta[:-1]
                        elif event.key == pygame.K_RETURN:
                            if self.resposta.strip().lower() == "philia":
                                self.enigma_resolvido = True
                                print("Acertou")
                            else:
                                print("resposta errada")
                                self.resposta = ""
                        else:
                            if len(self.resposta) < 6:
                                self.resposta += event.unicode

                    elif event.key == pygame.K_e and not self.enigma_aberto:
                        if player:
                            for ent in self.entity_list:
                                if isinstance(ent, Jail):
                                    if player.rect.colliderect(ent.rect):
                                        self.enigma_aberto = ent.text



            self.text(14, f"fps: {clock.get_fps():.0f}", C_WHITE, (100, WIN_HEIGHT - 35))
            self.text(14, f"entidades: {len(self.entity_list)}", C_WHITE, (100, WIN_HEIGHT - 20))

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
            pygame.display.flip()

    def text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font(FONT_PATH, size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)