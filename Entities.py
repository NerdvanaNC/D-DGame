import time
import random

# One variable to control all the pauses
# used in the print_desc function
default_pause = 2

def separator():
  print("\n", "=" * 50, "\n")

def print_desc(desc, sleepTime):
  print(desc)
  time.sleep(sleepTime)

class Hero(object):
  def __init__(self):
    self.name = None
    self.hp = 15
    self.luck = 1

  def set_hero_name(self):
    print_desc("Enter your hero's name", default_pause)
    confirm = False
    while confirm != True:
      self.name = input("Name > ")
      print_desc(f"Please confirm: is {self.name} correct?", default_pause)
      if(input("Y/N > ").lower() == "y"):
        confirm = True
        break

  def hero_hp_max(self):
    self.hp = 200
    return self.hp

  def damage(self, dmg):
    self.hp -= dmg
    return self.hp

  def heal(self, heal):
    if(self.hp < 15):
      self.hp += heal
    return self.hp

  def dead(self):
    return True if self.hp <= 0 else False



class Enemy(object):
  def __init__(self, name, health):
    self.name = name
    self.hp = health

  def damage(self, dmg):
    self.hp -= dmg
    return self.hp

  def dead(self):
    return True if self.hp <= 0 else False



class Dice(object):
  
  def roll(self, faces):
    return random.randint(1, faces)



class Combat(object):

  def start_combat(self, hero, enemy, hero_dmg_roll, enemy_dmg_roll):
    dice = Dice()
    print_desc(f"The {enemy.name} faces {hero.name} and readies their weapon.", default_pause)
    print_desc(f"{enemy.name} charges at you!", default_pause)

    print_desc("\n---- FIGHT ----\n", default_pause)
    print_desc("Rolling Initiative", default_pause)
    separator()

    enemy_initiative = dice.roll(6)
    print_desc(f"{enemy.name} rolled {enemy_initiative}", default_pause)
    time.sleep(0.5)
    hero_initiative = dice.roll(6) + hero.luck
    print_desc(f"{hero.name} rolled {hero_initiative}", default_pause)
    time.sleep(0.5)
    separator()

    print_desc(f"Enemy has {enemy.hp} HP", default_pause)
    print_desc(f"Hero has {hero.hp} HP", default_pause)
    separator()

    if(hero_initiative >= enemy_initiative):
      print_desc(f"{hero.name} goes first!", default_pause)
      while True:
        print_desc(f"{hero.name}'s turn!", default_pause)
        atk_roll = dice.roll(hero_dmg_roll)
        print_desc(f"{hero.name} rolls {atk_roll} damage!", default_pause)
        enemy.damage(atk_roll)
        print_desc(f"Enemy has {enemy.hp} HP", default_pause)

        if(enemy.dead()):
          print_desc(f"{enemy.name} is struck down!", default_pause)
          separator()
          hero.heal(3)
          print_desc(f"{hero.name} healed some HP. You have {hero.hp} HP.", default_pause)
          separator()
          print_desc("\n---- COMBAT END ----\n", 1)
          input("Press any key to continue > ")
          return True # win

        separator()
        print_desc(f"{enemy.name}'s turn!", default_pause)
        atk_roll = dice.roll(enemy_dmg_roll)
        print_desc(f"{enemy.name} rolls {atk_roll} damage!", default_pause)
        hero.damage(atk_roll)
        print_desc(f"{hero.name} has {hero.hp} HP", default_pause)
        if(hero.dead()):
          print_desc(f"{hero.name} is struck down!", default_pause)
          print_desc("\n---- COMBAT END ----\n", 1)
          input("Press any key to continue > ")
          return False # lose

    else:
      print_desc(f"{enemy.name} goes first!", default_pause)
      while True:
        print_desc(f"{enemy.name}'s turn!", default_pause)
        atk_roll = dice.roll(enemy_dmg_roll)
        print_desc(f"{enemy.name} rolls {atk_roll} damage!", default_pause)
        hero.damage(atk_roll)
        print_desc(f"{hero.name} has {hero.hp} HP", default_pause)
        if(hero.dead()):
          print_desc(f"{hero.name} is struck down!", default_pause)
          print_desc("\n---- COMBAT END ----\n", 1)
          input("Press any key to continue > ")
          return False # lose

        separator()
        print_desc(f"{hero.name}'s turn!", default_pause)
        atk_roll = dice.roll(hero_dmg_roll)
        print_desc(f"{hero.name} rolls {atk_roll} damage!", default_pause)
        enemy.damage(atk_roll)
        print_desc(f"{enemy.name} has {enemy.hp} HP", default_pause)
        if(enemy.dead()):
          print_desc(f"{enemy.name} is struck down!", default_pause)
          separator()
          hero.heal(3)
          print_desc(f"{hero.name} healed some HP. You have {hero.hp} HP.", default_pause)
          separator()
          print_desc("\n---- COMBAT END ----\n", 1)
          input("Press any key to continue > ")
          return True # win