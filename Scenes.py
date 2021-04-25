from sys import exit
import Entities

class Scene(object):
  def enter(self):
    print("The D&D Game by Nickunj.")



class StartGame(Scene):
  def enter(self):
    print("Welcome to a new adventure.")
    print("Let's get you started with a new hero.")
    self.hero = Entities.Hero()
    self.hero.set_hero_name()
    return "cave_entrance"

  def return_hero_obj(self):
    return self.hero



class CaveEntrance(Scene):
  def enter(self, hero):
    print(f"You stand at a cave entrance.")
    print(f"As you enter - you see three paths: Left, Right, and Middle.")
    chosen_path = input("Which path do you take? > ").lower()

    if chosen_path == "left":
      return "cave_left_encounter"
    elif chosen_path == "right":
      return "cave_right_encounter"
    elif chosen_path == "middle":
      return "cave_middle_encounter"
    elif chosen_path == "cheat":
      #cheat
      return "boss_room"
    else:
      print("Invalid input; try again.")
      return "cave_entrance"



class CaveLeftEncounter(Scene):
  def enter(self, hero):
    print("The hero sees an enemy!")
    dice = Entities.Dice()
    random_enemy = dice.roll(2)
    enemies_list = ['Undead Warrior', 'Shambling Zombie', 'Goblin Scout']
    enemy = Entities.Enemy(enemies_list[random_enemy], 10)
    combat_encounter = Entities.Combat()
    if(combat_encounter.start_combat(hero, enemy, 6, 4)):
      return "cave_chest"
    else:
      return "death"



class CaveRightEncounter(Scene):
  def enter(self, hero):
    print("The hero sees an enemy!")
    dice = Entities.Dice()
    random_enemy = dice.roll(2)
    enemies_list = ['Crazed Bandit', 'Goblin Warrior', 'Orc Scout']
    enemy = Entities.Enemy(enemies_list[random_enemy], 10)
    combat_encounter = Entities.Combat()
    if(combat_encounter.start_combat(hero, enemy, 6, 4)):
      return "cave_chest"
    else:
      return "death"



class CaveMiddleEncounter(Scene):
  def enter(self, hero):
    print("The hero sees an enemy!")
    dice = Entities.Dice()
    random_enemy = dice.roll(2)
    enemies_list = ['Undead Warrior', 'Shambling Zombie', 'Goblin Scout']
    enemy = Entities.Enemy(enemies_list[random_enemy], 12)
    combat_encounter = Entities.Combat()
    if(combat_encounter.start_combat(hero, enemy, 6, 5)):
      return "cave_chest"
    else:
      return "death"



class CaveChest(Scene):
  def enter(self, hero):
    print("You find a treasure chest!")
    print("You open it carefully, and within is a ruby the size of their fist.")
    input("[PRESS ANY KEY to pick up the RUBY] > ")
    print("As soon as you pick it up, your body seizes as a power runs through them.")
    print("You find your grip on reality slipping, when BOOM!")
    print("With a crashing sound, you suddenly find yourself teleported into a huge cavern!")
    print("You look around, and decides that you have no choice but to proceed.")
    return "penultimate_room"



class PenultimateRoom(Scene):
  def enter(self, hero):
    print("Story")
    dice = Entities.Dice()
    random_enemy = dice.roll(4)
    enemies_list = ['Elite Warrior', 'Bandit Leader', 'Orc Shocktrooper', 'Goblin Eviscerator', 'Champion Undead']
    enemy = Entities.Enemy(enemies_list[random_enemy], 15)
    combat_encounter = Entities.Combat()
    if(combat_encounter.start_combat(hero, enemy, 8, 6)):
      return "boss_room"
    else:
      return "death"



class BossRoom(Scene):
  def enter(self, hero):
    print("---- BOSS FIGHT ----")
    print("You come across a huge dragon!")
    print("The ruby you pocketed starts glowing")
    print("This is where I'd describe the encouter with the boss")
    print("IF I HAD ONE!")
    # Now I've changed some lines
    print("And added this line in the login branch")



class GameWin(Scene):
  def enter(self, hero):
    print(f"{hero.name} is victorious!")
    print("You've finished the game. Play again?")
    if(input("Y/N > ").lower() == "y"):
      print("Let's go!")
      return "start_game"
    print("All right. Good bye!")
    exit(0)



class Death(Scene):
  def enter(self, hero):
    print(f"|\t{hero.name} has been vanquished. Game over.\t|")
    print("Play again?")
    if(input("Y/N > ").lower() == "y"):
      print("Let's go!")
      return "start_game"
    print("All right. Good bye!")
    exit(0)