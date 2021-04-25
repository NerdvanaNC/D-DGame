import Scenes

class Map(object):
  def __init__(self):
    self.scenes = {
      'start_game': Scenes.StartGame(),
      'cave_entrance': Scenes.CaveEntrance(),
      'cave_left_encounter': Scenes.CaveLeftEncounter(),
      'cave_middle_encounter': Scenes.CaveMiddleEncounter(),
      'cave_right_encounter': Scenes.CaveRightEncounter(),
      'cave_chest': Scenes.CaveChest(),
      'penultimate_room': Scenes.PenultimateRoom(),
      'boss_room': Scenes.BossRoom(),
      'game_win': Scenes.GameWin(),
      'death': Scenes.Death(),
    }

  def return_scene_obj(self, scene_name):
    return self.scenes[scene_name]