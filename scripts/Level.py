import sys

import pygame.time
from pygame import Surface, Rect, K_BACKSPACE
from pygame.font import Font

from scripts.Consts import WIN_WIDTH, WIN_HEIGHT, FONT_PATH, CUTSCENE, C_WHITE, C_BLACK, C_PURPLE, PUZZLE
from scripts.Entity import Entity
from scripts.EntityFactory import EntityFactory
from scripts.EntityMediator import EntityMediator
from scripts.Jail import Jail
from scripts.Paper import Paper
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

        papers = EntityFactory.get_entity("Paper")
        self.entity_list.extend(papers)

        traps = EntityFactory.get_entity("Trap")
        self.entity_list.extend(traps)

        jail = EntityFactory.get_entity("Jail")
        self.entity_list.append(jail)

        npc = EntityFactory.get_entity("NPC")
        self.entity_list.extend(npc)

        spider = EntityFactory.get_entity("Spider")
        self.entity_list.extend(spider)

        self.camera_x = 0
        self.camera_y = 0
        self.em_cutscene = True
        self.contagem = 0
        self.campfire = pygame.image.load("./assets/images/camp.png").convert_alpha()
        self.npc_1 = pygame.image.load("./assets/images/NPC1.png").convert_alpha()
        self.npc_2 = pygame.image.load("./assets/images/NPC2.png").convert_alpha()
        self.badending = pygame.image.load("./assets/images/badending.png").convert_alpha()
        self.badend = False
        self.goodending = pygame.image.load("./assets/images/goodending.png").convert_alpha()
        self.goodend = False
        self.papel_aberto = False
        self.resposta = ""
        self.enigma_resolvido = False
        self.enigma_aberto = False
        self.fonte_dialogo = pygame.font.Font(FONT_PATH, 15)
        self.mostrar_erro = False

    def run(self):
        clock = pygame.time.Clock()
        pygame.mixer.music.load("./assets/audio/ambient-camp.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        while True:
            clock.tick(60)

            player = next((ent for ent in self.entity_list if isinstance(ent, Player)), None)

            if self.em_cutscene:
                self.camera_x = 0
            else:
                if player is None:
                    if not self.badend:
                        self.badend = True
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load("./assets/audio/bad-end-song.mp3")
                        pygame.mixer.music.set_volume(0.5)
                        pygame.mixer.music.play(-1)
                else:
                    self.camera_x = player.rect.x - (WIN_WIDTH / 5)

            for ent in self.entity_list:
                if isinstance(ent, Player):
                    if self.em_cutscene:
                        ent.rect.x = 140
                    elif self.resposta or self.papel_aberto:
                        pass
                    else:
                        ent.move()
                else:
                    ent.move()

                ent.render(self.window, self.camera_x, player)


            if self.em_cutscene:
                self.window.blit(self.campfire, (0, 0))
                if self.contagem < 9:
                    self.window.blit(self.npc_1, (WIN_WIDTH / 2 - 70, WIN_HEIGHT / 2 + 115))
                    self.window.blit(pygame.transform.flip(self.npc_2, True, False), (WIN_WIDTH / 2 + 50, WIN_HEIGHT / 2 + 115))

                rect = pygame.draw.rect(self.window, C_BLACK, (70, 70, 400, 100))

                if self.contagem < len(CUTSCENE):
                    self.desenhar_texto(CUTSCENE[self.contagem], rect, self.fonte_dialogo, C_WHITE)


            if self.badend:
                self.window.blit(self.badending, (0, 0))
                self.text(22, "GAME", C_WHITE, (WIN_WIDTH / 2, 70))
                self.text(22, "OVER", C_WHITE, (WIN_WIDTH / 2, 120))
                self.text(15, "Aperte ESC para recomeçar", C_WHITE, (WIN_WIDTH/ 2, WIN_HEIGHT / 2 + 150))

            if self.goodend:
                self.window.blit(self.goodending, (0, 0))
                self.text(30, "Obrigada por jogar", C_PURPLE, (WIN_WIDTH / 2, 100))
                self.text(15, "Aperte ESC para recomeçar", C_WHITE, (WIN_WIDTH/ 2, 140))
                self.final_text(10, "Imagens feitas no Pixel Studio", C_WHITE, (WIN_WIDTH - 180, 300))
                self.final_text(10, "Audios pelo Freesound.org", C_WHITE, (WIN_WIDTH - 180, 320))
                self.final_text(10, "Fonte pela dafont.com.br", C_WHITE, (WIN_WIDTH - 180, 340))

            if self.papel_aberto:
                largura, altura = 500, 150
                x_caixa = (WIN_WIDTH - largura) / 2
                y_caixa = (WIN_HEIGHT - altura) / 2
                pygame.draw.rect(self.window, C_BLACK, (x_caixa, y_caixa, largura, altura))
                linhas = self.papel_aberto.split('\n')
                y_inicial = (WIN_HEIGHT / 2) - ((len(linhas) - 1) * 12)
                for i, linha in enumerate(linhas):
                    self.text(14, linha, C_WHITE, (WIN_WIDTH / 2, y_inicial + (i * 22)))

                self.text(11, "[ Aperte ESC para fechar ]", C_PURPLE, (WIN_WIDTH / 2, y_caixa + altura - 20))

            if self.enigma_aberto:
                largura, altura = 500, 150
                x_caixa = (WIN_WIDTH - largura) / 2
                y_caixa = (WIN_HEIGHT - altura) / 2
                pygame.draw.rect(self.window, C_BLACK, (x_caixa, y_caixa, largura, altura))
                self.text(14, self.enigma_aberto, C_WHITE, (WIN_WIDTH / 2, WIN_HEIGHT / 2))

                if self.mostrar_erro:
                    self.text(12, "Senha incorreta, tente novamente!!! (Aperte qualquer letra)", C_WHITE, (WIN_WIDTH / 2, WIN_HEIGHT / 2 + 30))
                else:
                    self.text(14, self.resposta, C_WHITE, (WIN_WIDTH / 2, WIN_HEIGHT / 2 + 30))

                self.text(11, "[ Aperte ESC para fechar ]", C_PURPLE, (WIN_WIDTH / 2, y_caixa + altura - 20))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e and self.em_cutscene:
                        self.contagem += 1

                        # Gerenciando os áudios da cutscene dependendo do diálogo
                        if self.contagem == 5:
                            pygame.mixer.music.stop()
                            explosion = pygame.mixer.Sound("./assets/audio/explosion.mp3")
                            explosion.set_volume(0.7)
                            explosion.play()

                        elif self.contagem == 6:
                            pygame.mixer.music.stop()
                            suspense = pygame.mixer.Sound("./assets/audio/suspense.mp3")
                            suspense.set_volume(0.7)
                            suspense.play()

                        elif self.contagem == 9:
                            scream = pygame.mixer.Sound("./assets/audio/scream.mp3")
                            scream.set_volume(0.7)
                            scream.play()

                        if self.contagem >= len(CUTSCENE):
                            self.em_cutscene = False
                            pygame.mixer.stop()
                            pygame.mixer.music.load("./assets/audio/ambient-game.mp3")
                            pygame.mixer.music.play(-1)

                    if event.key == pygame.K_ESCAPE and (self.badend or self.goodend):
                        return


                    # Evento de teclado do papel
                    if event.key == pygame.K_ESCAPE and self.papel_aberto:
                            self.papel_aberto = False

                    elif event.key == pygame.K_e and not self.papel_aberto:
                        if player:
                            for ent in self.entity_list:
                                if isinstance(ent, Paper):
                                    if player.rect.colliderect(ent.rect):
                                        self.papel_aberto = ent.text

                    #Evento de teclado do enigma
                    if self.enigma_aberto:
                        if event.key == pygame.K_ESCAPE:
                            self.enigma_aberto = False
                        elif event.key == K_BACKSPACE:
                            self.mostrar_erro = False
                            self.resposta = self.resposta[:-1]
                        elif event.key == pygame.K_RETURN:
                            if self.resposta.strip().lower() == PUZZLE:
                                self.enigma_resolvido = True
                                self.enigma_aberto = False
                                self.goodend = True
                                pygame.mixer.music.stop()
                                pygame.mixer.music.load("./assets/audio/good-end-song.mp3")
                                pygame.mixer.music.set_volume(0.5)
                                pygame.mixer.music.play(-1)
                            else:
                                self.mostrar_erro = True
                                self.resposta = ""
                        else:
                            if len(self.resposta) < 6:
                                self.mostrar_erro = False
                                self.resposta += event.unicode

                    elif event.key == pygame.K_e and not self.enigma_aberto:
                        if player:
                            for ent in self.entity_list:
                                if isinstance(ent, Jail):
                                    if player.rect.colliderect(ent.rect):
                                        self.enigma_aberto = ent.text


            # self.text(14, f"fps: {clock.get_fps():.0f}", C_WHITE, (100, WIN_HEIGHT - 35))
            # self.text(14, f"entidades: {len(self.entity_list)}", C_WHITE, (100, WIN_HEIGHT - 20))

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
            pygame.display.flip()

    def text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font(FONT_PATH, size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def desenhar_texto(self, text, rect, font, color):
        words = text.split(' ')
        lines = []
        linha_atual = ""
        padding = 25

        for word in words:
            test_line = linha_atual + word + " "
            if font.size(test_line)[0] < (rect.width - padding * 2):
                linha_atual = test_line
            else:
                lines.append(linha_atual)
                linha_atual = word + " "
        lines.append(linha_atual)

        y_offset = rect.top + padding
        for line in lines:
            text_surf = font.render(line.strip(), True, color)
            self.window.blit(text_surf, (rect.left + padding, y_offset))
            y_offset += font.get_linesize() + 10

    def final_text(self, text_size: int, text: str, text_color: tuple, text_left_pos: tuple):
        text_font: Font = pygame.font.Font(FONT_PATH, size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(bottomleft=text_left_pos)
        self.window.blit(source=text_surf, dest=text_rect)
