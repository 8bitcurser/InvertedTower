from dataclasses import dataclass
from enum import Enum
from random import randint


class CharacterType(Enum):
    MONSTER = 0
    NPC = 1
    PC = 2

class ItemType(Enum):
    CONSUMABLE = 0
    ARMOR = 1
    WEAPON = 2
    ATTUNABLE = 3


class CharacterStatus(Enum):
    DEAD = 0
    BLINDED = 1
    SLOWED = 2
    PARALYZED = 3
    BLEEDING = 4
    OK = 5


@dataclass
class Position:
    x: int
    y: int
    floor: int


@dataclass
class Item:
    name: str
    desciption: str
    type: ItemType
    cursed: bool
    defense_modifier: int
    attack_modifier: int
    attack_bonus: int
    defense_bonus: int
    health_bonus: int
    magic_bonus: int
    uses: int
    attune_slots: int


@dataclass
class Character:
    name: str
    type: CharacterType
    level: int
    max_health_points: int
    health_points: int
    max_magic_points: int
    magic_points: int
    status: CharacterStatus
    attack_modifier: int
    attack_dice: int
    defense_points: int
    movement_speed: int
    vision: int
    position: Position
    weapon: Item = None
    armor: Item = None
    attune_slots: int


    def attack(self, target) -> int:
        roll = randint(1, 20) + self.weapon.attack_modifier
        if roll >= target.defense_points + target.armor.defense_bonus:
            return randint(1, self.attack_dice) + self.weapon.attack_bonus
        return 0

    def move(self, destination: Position) -> bool:
        x_change = abs(destination.x - self.position.x)
        y_change = abs(destination.y - self.position.y) 
        if (x_change + y_change) <= self.movement_speed:
            self.position = destination
            return True
        return False

    def rest(self, map):
        # paralyzes a char for X rounds
        # recovers X amount of health points
        # recovers X amount of magic points
        # cannot rest if monsters in vision
        self.health_points = self.max_health_points
        self.magic_points = self.max_magic_points
        return True

    def equip(self, item):
        pass

    def use(self, item):
        pass