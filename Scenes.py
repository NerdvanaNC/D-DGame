from sys import exit
import Entities

# One variable to control all the pauses
# used in the print_desc function
default_pause = 2

class Scene(object):
  def enter(self):
    print("The D&D Game by Nickunj.")



class StartGame(Scene):
  def enter(self):
    Entities.separator()
    Entities.print_desc("\t     Welcome to a new adventure.", 0)
    Entities.separator()
    Entities.print_desc("Let's get you started with a new hero.", default_pause)
    self.hero = Entities.Hero()
    self.hero.set_hero_name()
    return "cave_entrance"

  def return_hero_obj(self):
    return self.hero



class CaveEntrance(Scene):
  def enter(self, hero):
    Entities.separator()
    Entities.print_desc("\t     Then let us begin.", 0)
    Entities.separator()
    Entities.print_desc("You're a Dragon Knight by profession, a dragon slayer.", default_pause)
    Entities.print_desc("You've been called upon by your guild to hunt down an [ELDERWYRM].", default_pause)
    Entities.print_desc("This [ELDERWYRM] has been terrorizing nearby cities, and you've been tracking it for days to no avail.", default_pause)
    Entities.print_desc("The only trail you have to follow is of the wanton destruction it leaves in its wake...", default_pause)
    Entities.print_desc("But strangely you still have no clue where it makes its lair.", default_pause)
    Entities.print_desc("Still, you haven't given up and have been closely following it for days.", default_pause)
    Entities.print_desc("Right now, the hunt has brought you to a small valley a day away from the nearest city.", default_pause)
    Entities.print_desc("You've followed the trail and you find yourself standing at a [CAVE ENTRANCE].", default_pause)
    Entities.print_desc("You enter, and you see three paths: [LEFT], [RIGHT], and [MIDDLE].", default_pause)
    chosen_path = input("Which path do you take? > ").lower()

    if chosen_path == "left":
      return "cave_left_encounter"
    elif chosen_path == "right":
      return "cave_right_encounter"
    elif chosen_path == "middle":
      return "cave_middle_encounter"
    else:
      Entities.print_desc("Invalid input; try again.", default_pause)
      return "cave_entrance"



class CaveLeftEncounter(Scene):
  def enter(self, hero):
    Entities.print_desc("The hero sees an [ENEMY]!", default_pause)
    input("\n[PRESS ANY KEY] to continue...\n")
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
    Entities.print_desc("The hero sees an [ENEMY]!", default_pause)
    input("\n[PRESS ANY KEY] to continue...\n")
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
    Entities.print_desc("The hero sees an [ENEMY]!", default_pause)
    input("\n[PRESS ANY KEY] to continue...\n")
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
    Entities.print_desc("As you strike down the enemy and move ahead into the small cavern...", default_pause)
    Entities.print_desc("You see a glint underneath a pile of rubbish in the corner.", default_pause)
    Entities.print_desc("You approach, and sweep aside the trash with your sword. Underneath...", default_pause)
    input("\n[PRESS ANY KEY] to continue...\n")
    Entities.print_desc("You find a [TREASURE CHEST]!", 2)
    Entities.print_desc("As you open it carefully, its weathered hinges creak in protest.", default_pause)
    Entities.print_desc("You pry it open, and inside...", default_pause)
    Entities.print_desc("A [RUBY] the size of your fist!", default_pause)
    input("[PRESS ANY KEY] to pick up the [RUBY] > ")
    Entities.print_desc("You reach down and as you go to pick up the [RUBY], your hand buzzes with energy.", default_pause)
    Entities.print_desc("You hesitate, but only for a moment. As soon as you pick it up...", default_pause)
    Entities.print_desc("Your hand burns with an extreme energy! Your fingers lose all feeling even as they helplessly grasp the [RUBY]!", default_pause)
    Entities.print_desc("The numbness extends quickly from your hands into your entire body...", default_pause)
    Entities.print_desc("And you find your grip on reality slipping, when BOOM!", default_pause)
    input("\n[PRESS ANY KEY] to continue...\n")
    Entities.print_desc("With a deafening crash, you suddenly find yourself teleported into a [HUGE CAVERN]!", default_pause)
    Entities.print_desc("You look around, and decide that you have no choice but to proceed.", default_pause)
    return "penultimate_room"



class PenultimateRoom(Scene):
  def enter(self, hero):
    Entities.print_desc("As you walk forward along a narrow path leading further into the [MOUNTAIN],", default_pause)
    Entities.print_desc("You reach a small opening where you see a haphazard [CAMPFIRE] burning.", default_pause)
    Entities.print_desc("The hair on the back of your neck stands at end as you sense [ENEMIES] approaching.", default_pause)
    input("\n[PRESS ANY KEY] to continue...\n")
    dice = Entities.Dice()
    random_enemy = dice.roll(4)
    enemies_list = ['Elite Warrior', 'Bandit Leader', 'Orc Shocktrooper', 'Goblin Eviscerator', 'Champion Undead']
    enemy = Entities.Enemy(enemies_list[random_enemy], 15)
    combat_encounter = Entities.Combat()
    if(combat_encounter.start_combat(hero, enemy, 8, 6)):
      Entities.print_desc(f"As you strike down the [{enemy.name.upper()}] and take a breath, you hear a small shuffle...", default_pause)
      Entities.print_desc("You look behind you - and a blur leaps at you to attack!", default_pause)
      random_enemy = dice.roll(4)
      enemies_list = ['Tiny Sprute', 'Snotnosed Bandit', 'Orc Chintu', 'Goblin Gob Lin', 'Almost-dead Undead']
      enemy = Entities.Enemy(enemies_list[random_enemy], 4)
      if(combat_encounter.start_combat(hero, enemy, 6, 2)):
        return "boss_room"
    else:
      return "death"



class BossRoom(Scene):
  def enter(self, hero):
    Entities.print_desc("Having dealt with both the elite [ENEMY] and the tiny one, you make your way further into the [MOUNTAIN].", default_pause)
    Entities.print_desc("Even from afar you can feel a slight vibration in the air, every questing hair on your body is abuzz with anticipation.", default_pause)
    Entities.print_desc("You see a darkened entrance at the end of your path, and you know what lies beyond is a fight worthy of songs.", default_pause)
    Entities.print_desc("You steel yourself, and enter.", 2)
    input("\n[PRESS ANY KEY] to continue...\n")
    Entities.separator()
    Entities.print_desc("\t     BOSS FIGHT", 0)
    Entities.separator()
    Entities.print_desc("As soon as you enter, the [RUBY] in your pocket starts heating up intensely!", default_pause)
    Entities.print_desc("With a glow so bright you barely get to shield your eyes, it [EXPLODES]!", default_pause)
    Entities.print_desc("You feel a rush of energy consume you, every fiber of your being is pulsing with [DIVINE ENERGY]!", default_pause)
    Entities.print_desc("You feel much [STRONGER]!", default_pause)
    Entities.print_desc("The cacophony awakens the [DRAGON] in the [CAVERN], and it roars with all its might upon seeing a challenger.", default_pause)
    input("\n[PRESS ANY KEY] to continue...\n")
    enemy = Entities.Enemy("ELDERWYRM", 200)
    combat_encounter = Entities.Combat()
    if(combat_encounter.start_combat(hero, enemy, 20, 20)):
      return "game_win"
    else:
      return "death"



class GameWin(Scene):
  def enter(self, hero):
    Entities.print_desc(f"{hero.name} is victorious!", default_pause)
    Entities.print_desc("You've finished the game. Play again?", default_pause)
    if(input("Y/N > ").lower() == "y"):
      Entities.print_desc("Let's go!", default_pause)
      return "start_game"
    Entities.print_desc("All right. Good bye!", default_pause)
    exit(0)



class Death(Scene):
  def enter(self, hero):
    Entities.print_desc(f"|\t{hero.name} has been vanquished. Game over.\t|", default_pause)
    Entities.print_desc("Play again?", default_pause)
    if(input("Y/N > ").lower() == "y"):
      Entities.print_desc("Let's go!", default_pause)
      return "start_game"
    Entities.print_desc("All right. Good bye!", default_pause)
    exit(0)