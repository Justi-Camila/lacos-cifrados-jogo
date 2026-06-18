from scripts.Background import Background
from scripts.Consts import WIN_WIDTH, WIN_HEIGHT
from scripts.Player import Player


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
                return Player("Player", (0, WIN_HEIGHT / 2 + 100))
        return None
