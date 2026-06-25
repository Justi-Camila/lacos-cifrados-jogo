import pygame.time

from scripts.Entity import Entity
from scripts.Player import Player
from scripts.Spider import Spider
from scripts.Trap import Trap


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Trap):
            if ent.rect.right <= 0:
                ent.health = 0


    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interaction= False
        if isinstance(ent1, Player) and isinstance(ent2, Trap):
            valid_interaction = True
        elif isinstance(ent1, Trap) and isinstance(ent2, Player):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, Spider):
            valid_interaction = True
        elif isinstance(ent1, Spider) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):

                # Aplica o cooldown de dano para evitar perda de vida consecutiva em frames seguidos
                tempo_atual = pygame.time.get_ticks()
                if tempo_atual > ent1.imune and ent2.damage > 0:
                    ent1.health -= ent2.damage
                    ent1.last_dmg = ent2.name
                    ent1.imune = tempo_atual + 1000
                if tempo_atual > ent2.imune and ent1.damage > 0:
                    ent2.health -= ent1.damage
                    ent2.last_dmg = ent1.name
                    ent2.imune = tempo_atual + 1000

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)