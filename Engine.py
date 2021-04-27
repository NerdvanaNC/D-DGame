import Map

class Engine(object):
  def start_game(self, opening_scene):
    game_map = Map.Map()
    next_scene = game_map.return_scene_obj(opening_scene)
    current_scene = game_map.return_scene_obj(opening_scene)
    next_scene = next_scene.enter()
    hero = current_scene.return_hero_obj()

    while True:
      if(next_scene == "start_game"):
        next_scene = current_scene = game_map.return_scene_obj(next_scene)
        next_scene = next_scene.enter()
      else:
        next_scene = current_scene = game_map.return_scene_obj(next_scene)
        next_scene = next_scene.enter(hero)