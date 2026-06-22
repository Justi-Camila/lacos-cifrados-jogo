import random

from scripts.Background import Background
from scripts.Consts import WIN_WIDTH, WIN_HEIGHT
from scripts.Player import Player
from scripts.Paper import Paper
from scripts.Trap import Trap


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):

        match entity_name:
            case "LevelBg":
                list_bg = []
                for i in range(8):
                    list_bg.append(Background(f"LevelBg{i}", (0, 0)))
                    list_bg.append(Background(f"LevelBg{i}", (WIN_WIDTH, 0)))
                return list_bg
            case "Player":
                return Player("Player", (10, WIN_HEIGHT / 2 + 115))
            case "Paper":
                list_papers = []
                list_text = [
                    "Primeira Pista",
                    "Segunda Pista"
                ]
                posicao_x = 900
                for i in range(2):
                    novo_paper = Paper("Paper", (posicao_x, 390), list_text[i])
                    list_papers.append(novo_paper)
                    posicao_x += 4100
                return list_papers
            case "Trap":
                list_traps = []
                ponteiro_x = 650
                for i in range(25):
                    posicao_aleatoria = random.randint(0, 150)
                    x_desta_trap = ponteiro_x + posicao_aleatoria
                    nova_trap = Trap("Trap", (x_desta_trap, 390))
                    list_traps.append(nova_trap)
                    ponteiro_x = x_desta_trap + 250
                return list_traps
        return None
