import pygame.key

from scripts.Consts import ENTITY_SPEED, C_WHITE
from scripts.Entity import Entity, text_game


class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.img_andando = pygame.image.load("./assets/images/"+ self.name +"_walk.png").convert_alpha()
        self.img_parado = self.surf
        self.img_andando_esquerda = pygame.transform.flip(self.img_andando, True, False)
        self.img_parado_esquerda = pygame.transform.flip(self.img_parado, True, False)
        self.olhando_direita = True
        self.contador = 0
        self.pulo = False
        self.caindo = False
        self.pos_y_chao = position[1]
        self.altura_max = self.pos_y_chao - 100
        self.andando = ENTITY_SPEED[self.name]

    def move(self):
        pressed_key = pygame.key.get_pressed()
        andando = False

        if pressed_key[pygame.K_d]:
            andando = True
            self.olhando_direita = True
            self.rect.x += ENTITY_SPEED[self.name]
        elif pressed_key[pygame.K_a]:
            andando = True
            self.olhando_direita = False
            self.rect.x -= ENTITY_SPEED[self.name]

        if pressed_key[pygame.K_SPACE] and not self.pulo and not self.caindo:
            self.pulo = True

        if self.pulo:
            self.rect.centery -= ENTITY_SPEED[self.name]
            if self.rect.centery <= self.altura_max:
                self.pulo = False
                self.caindo = True
                print("Caindooo")

        elif self.caindo:
            self.rect.centery += ENTITY_SPEED[self.name]
            if self.rect.centery >= self.pos_y_chao:
                self.rect.y = self.pos_y_chao
                self.caindo = False

        if andando:
            self.contador += 0.1
            if self.contador >= 2:
                self.contador = 0

            if self.olhando_direita:
                self.surf = self.img_parado if int(self.contador) == 0 else self.img_andando
            else:
                self.surf = self.img_parado_esquerda if int(self.contador) == 0 else self.img_andando_esquerda
        else:
            self.surf = self.img_parado if self.olhando_direita else self.img_parado_esquerda
            self.contador = 0

        if self.rect.x < 0:
            self.rect.x = 0


    def render(self, window, camera_x, player=None):
        text_game(window,14, f"Millena - Health {self.health}", C_WHITE, (80, 20))
        window.blit(self.surf, (self.rect.x - camera_x, self.rect.y))


