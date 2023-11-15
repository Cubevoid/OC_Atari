from .game_objects import GameObject
from .utils import find_objects, find_mc_objects, most_common_color
import numpy as np

objects_colors = {"player": [[26, 102, 26], [111, 111, 111], [74, 74, 74]], "radar":[111, 210, 111], "radar_hud": [236, 236, 236], "tank_blue1": [24, 80, 128],
                  "tank_blue2": [66, 136, 176], "tank_grey": [142, 142, 142], "crosshair1": [0, 0, 0], "crosshair2": [236, 200, 96],
                  "red": [[228, 111, 111], [200, 72, 72], [148, 0, 0]]}
                  #"red": [[228, 111, 111], [214, 92, 92], [200, 72, 72], [184, 50, 50], [167, 26, 26], [148, 0, 0]]}


class Player(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rgb = [26, 102, 26]


class Crosshair(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rgb = [0, 0, 0]


class Shot(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rgb = [236, 236, 236]


class Radar(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rgb = [111, 210, 111]


class Radar_Content(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rgb = [236, 236, 236]


class Blue_Tank(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rgb = [24, 80, 128]


#  ---- HUD -----
class Score(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rgb = [252, 252, 84]


class Life(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rgb = [252, 252, 84]


def _detect_objects_battlezone(objects, obs, hud=False):
    objects.clear()

    player = find_mc_objects(obs, objects_colors["player"], miny=110, maxy=178)
    for bb in player:
            objects.append(Player(*bb))
    
    shot = find_objects(obs, objects_colors["radar_hud"], miny=70, maxy=175)
    for bb in shot:
            objects.append(Shot(*bb))
    
    crosshair = find_objects(obs, objects_colors["crosshair1"], miny=79, maxy=175)
    for bb in crosshair:
            objects.append(Crosshair(*bb))
    
    crosshair = find_objects(obs, objects_colors["crosshair2"], miny=79, maxy=175)
    for bb in crosshair:
            cr = Crosshair(*bb)
            cr.rgb = objects_colors["crosshair2"]
            objects.append(cr)

    radar = find_objects(obs, objects_colors["radar"], maxy=36)
    for bb in radar:
            objects.append(Radar(*bb))

    radar_c = find_objects(obs, objects_colors["radar_hud"], maxy=37, size=(1,1), tol_s=1)
    for bb in radar_c:
            objects.append(Radar_Content(*bb))

    blue = find_mc_objects(obs, [objects_colors["tank_blue1"], objects_colors["tank_blue2"],objects_colors["tank_grey"]], miny=78, maxy=175)
    for bb in blue:
            objects.append(Blue_Tank(*bb))
    
    red = find_mc_objects(obs, objects_colors["red"], miny=78, maxy=175, closing_dist=5)

    if hud:
         pass