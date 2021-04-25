import time
import random

def separator():
  print("-" * 50)

class Hero(object):
  def __init__(self):
    self.name = None
    self.hp = 15
    self.luck = 1

  def set_hero_name(self):
    print("Enter your hero's name")
    confirm = False
    while confirm != True:
      self.name = input("> ")
      print(f"Please confirm: is {self.name} correct?")
      if(input("Y/N > ").lower() == "y"):
        confirm = True
        break

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
    print(f"The {enemy.name} faces {hero.name} and readies their weapon.")
    print(f"{enemy.name} charges at you!")

    time.sleep(1)
    print("\n---- FIGHT ----\n")
    time.sleep(1)
    print("Rolling Initiative")
    separator()

    enemy_initiative = dice.roll(6)
    print(f"{enemy.name} rolled {enemy_initiative}")
    time.sleep(0.5)
    hero_initiative = dice.roll(6) + hero.luck
    print(f"{hero.name} rolled {hero_initiative}")
    time.sleep(0.5)
    separator()

    time.sleep(1)
    print(f"Enemy has {enemy.hp} HP")
    print(f"Hero has {hero.hp} HP")
    separator()
    time.sleep(1)

    if(hero_initiative >= enemy_initiative):
      print(f"{hero.name} goes first!")
      time.sleep(1)
      while True:
        print(f"{hero.name}'s turn!")
        atk_roll = dice.roll(hero_dmg_roll)
        print(f"{hero.name} rolls {atk_roll} damage!")
        time.sleep(1)
        enemy.damage(atk_roll)
        print(f"Enemy has {enemy.hp} HP")
        time.sleep(1)

        if(enemy.dead()):
          print(f"{enemy.name} is struck down!")
          time.sleep(1)
          separator()
          hero.heal(3)
          print(f"{hero.name} healed some HP. You have {hero.hp} HP.")
          separator()
          time.sleep(1)
          print("\n---- COMBAT END ----\n")
          return True # win

        separator()
        print(f"{enemy.name}'s turn!")
        time.sleep(1)
        atk_roll = dice.roll(enemy_dmg_roll)
        print(f"{enemy.name} rolls {atk_roll} damage!")
        time.sleep(1)
        hero.damage(atk_roll)
        print(f"{hero.name} has {hero.hp} HP")
        time.sleep(1)
        if(hero.dead()):
          print(f"{hero.name} is struck down!")
          print("\n---- COMBAT END ----\n")
          return False # lose

    else:
      print(f"{enemy.name} goes first!")
      time.sleep(1)
      while True:
        print(f"{enemy.name}'s turn!")
        atk_roll = dice.roll(enemy_dmg_roll)
        print(f"{enemy.name} rolls {atk_roll} damage!")
        time.sleep(1)
        hero.damage(atk_roll)
        print(f"{hero.name} has {hero.hp} HP")
        time.sleep(1)
        if(hero.dead()):
          print(f"{hero.name} is struck down!")
          print("\n---- COMBAT END ----\n")
          return False # lose

        separator()
        print(f"{hero.name}'s turn!")
        time.sleep(1)
        atk_roll = dice.roll(hero_dmg_roll)
        print(f"{hero.name} rolls {atk_roll} damage!")
        time.sleep(1)
        enemy.damage(atk_roll)
        print(f"{enemy.name} has {enemy.hp} HP")
        time.sleep(1)
        if(enemy.dead()):
          print(f"{enemy.name} is struck down!")
          time.sleep(1)
          separator()
          hero.heal(3)
          print(f"{hero.name} healed some HP. You have {hero.hp} HP.")
          separator()
          time.sleep(1)
          print("\n---- COMBAT END ----\n")
          return True # win