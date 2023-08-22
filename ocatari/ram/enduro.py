from .game_objects import GameObject
import sys 

"""
RAM extraction for the game Enduro.
"""

MAX_NB_OBJECTS = {"Player": 1, "Bird": 8, "Crab":8, "Clam":8,"GreenFish":8,"WhitePlate":24, "BluePlate":24,"Bear":1, "House":1,"CompletedHouse":1,"FrostBite":1}
MAX_NB_OBJECTS_HUD = {"LifeCount":1, "PlayerScore":4, "Degree":2}# 'Score': 1}

class Player(GameObject):
    
    def __init__(self):
        super().__init__()
        self._xy = 0, 0
        self.wh = (16,10)
        self.rgb = 192,192,192
        self.hud = False

class PlayerScore(GameObject):
    """
    The player's score display.
    """
    
    def __init__(self):
        super().__init__()
        self.rgb =132,144,252
        self.hud = True
        self.wh = (8, 18)
        self._xy = 0, 0


# parses MAX_NB* dicts, returns default init list of objects
def _get_max_objects(hud=False):

    def fromdict(max_obj_dict):
        objects = []
        mod = sys.modules[__name__]
        for k, v in max_obj_dict.items():
            for _ in range(0, v):
                objects.append(getattr(mod, k)())    
        return objects

    if hud:
        return fromdict(MAX_NB_OBJECTS_HUD)
    return fromdict(MAX_NB_OBJECTS)


def _init_objects_enduro_ram(hud=False):
    """
    (Re)Initialize the objects
    """
    objects = [Player()]
    if hud:
        objects.extend([])
    return objects

def _detect_objects_enduro_revised(objects, ram_state, hud=False):
    """
    For all 3 objects:
    (x, y, w, h, r, g, b)
    """
    # 106 ram_state is somewhat controlling the y of the player when it's dying by sinking
    player,= objects[:1]
    player.xy=int(-0.566*ram_state[54]+146),144

    if hud:
        # ram_state[45] indicates the level 
        pass