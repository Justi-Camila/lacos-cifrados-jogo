import random

from scripts.Background import Background
from scripts.Consts import WIN_WIDTH, WIN_HEIGHT
from scripts.Jail import Jail
from scripts.NPC import NPC
from scripts.Player import Player
from scripts.Paper import Paper
from scripts.Spider import Spider
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
                    "Se quiser ver suas amigas inteiras novamente, \ndecifre o caminho. O relógio já está correndo. Não tente nos seguir.",
                    "PHILIA",
                    "CIFRA DE CÉSAR +3"
                ]
                posicao_x = 550
                for i in range(2):
                    novo_paper = Paper("Paper", (posicao_x, 390), list_text[i])
                    list_papers.append(novo_paper)
                    posicao_x += 3000
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

            case "Spider":
                list_spiders = []
                ponteiro_x = 700
                for i in range(18):
                    posicao_aleatoria = random.randint(0, 200)
                    x_desta_trap = ponteiro_x + posicao_aleatoria
                    nova_trap = Spider("Spider", (x_desta_trap, 390))
                    list_spiders.append(nova_trap)
                    ponteiro_x = x_desta_trap + 350
                return list_spiders

            case "Jail":
                return Jail("Jail", (9000, 160), "Digite a resposta (encontre as pistas nos papéis)")

            case "NPC":
                list_npc = []
                ponteiro_x = 9060
                for i in range(2):
                    novo = NPC(f"NPC{i + 1}", (ponteiro_x, 370))
                    list_npc.append(novo)
                    ponteiro_x += 120
                return list_npc
        return None
