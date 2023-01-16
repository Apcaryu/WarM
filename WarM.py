# Author : LucasTriolet, Apcaryu

import random
import sys
from typing import List, Union

weapons  = ["GreatSword","LongSword","Sword & Shield","Dual Blades",
			"GreatHammer","HunterHorn","Lance","GunLance","SwitchBlade","ChargeBlade",
			"InsectGlaive","Light BowGun","Heavy BowGun","Bow"]
armors   = ["Head", "Mail", "Vambraces", "Coil", "Greaves"]

monster_csv = "monster.csv"

# Pour lancer le programme il faut lui donner en argument le tier max et sois "weapon" ou "armor"
# exemple: python3 WarM.py 3 weapon
# 		   python3 WarM.py 5 armor
# 		   python3 WarM.py 8

# ================= FONCTIONNEMENT =================== #
# choisi un tier en fonction du paramètre max_tier     #
# choisi un monstre en fonction du tier choisi         #
# si "weapon" a été passer en pararmetre alors         #
# 		choisi une weapon parmi les 14 types d'arme    #
# si "armor" a été passer en parametre alors           #
# 		choisi un monstre pour chaque element d'armure #
# si il n'y a pas de deuxieme argument alors           #
# 		genere un full set                             #
# ==================================================== #

class Monster() :
    def __init__(self, name : str, lr : int, hr : int, mr : int) -> None:
        self.name = name
        self.lr = lr
        self.hr = hr
        self.mr = mr

    def __str__(self) -> None:
        return f"{self.name} : {self.lr} | {self.hr} | {self.mr}"

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Monster) :
            if self.name == __o.name : return True
            else : return False
        elif isinstance(__o, str) :
            if self.name == __o : return True
            else : return False
        else :
            return Exception
    
    def has_tier(self, tier : int) :
        if tier == self.lr : return True
        if tier == self.hr : return True
        if tier == self.mr : return True
        return False

def load_monster_csv(csv : str) -> List[Monster]:
    tab = []
    with open(csv) as file :
        lines = file.readlines()
        for line in lines :
            name, lr, hr, mr = line.split(",")
            try :
                tab.append(Monster(name, int(lr), int(hr), int(mr)))
            except Exception : continue
    return tab

def get_rand_tier(spread : int = 1) -> int:
    if not sys.argv[1].isdecimal() :
        print("Dood ! You did not gave me a tier number here !")
        exit()
    user_tier = int(sys.argv[1])
    min_tier = user_tier - spread
    max_tier = user_tier + spread

    if (min_tier < 2) : min_tier = 2
    if (12 < max_tier): max_tier = 12
    rand_tier = random.randint(min_tier, max_tier)
    return rand_tier
    
def get_rand_monster(monsters : List[Monster], tier : int = 0) -> Union[Monster, None]:
    if (tier == 0) :
        print("Dood ! This tier is so wrong dood !")
        return
    if monsters == [] :
        print("I think the list is empty dood !")
        return
    nb_monsters = len(monsters)
    r = random.randint(0, nb_monsters-1)
    monster = monsters[r]
    if (monster.has_tier(tier)) : return monster
    else : return get_rand_monster(monsters, tier)

def get_rand_weapon(weapons : List[str]) -> str : 
    return weapons[random.randint(0, len(weapons) - 1)]

def generation(monsters : List[Monster], nb_arg : int = len(sys.argv)) :
    global weapons
    global armors 
    if (nb_arg == 2) :
        tier = get_rand_tier()
        print(f"weapon : {get_rand_weapon(weapons)} | monster : {get_rand_monster(monsters, tier).name} | tier : {tier}")
        for armor in armors : 
            tier = get_rand_tier()
            print(f"armor : {armor} | monster : {get_rand_monster(monsters, tier).name} | tier : {tier}")

    elif (nb_arg == 3) :
        if (sys.argv[2] == "weapon") :
            tier = get_rand_tier()
            print(f"weapon : {get_rand_weapon(weapons)} | monster : {get_rand_monster(monsters, tier).name} | tier : {tier}")
        elif (sys.argv[2] == "armor") :
            for armor in armors : 
                tier = get_rand_tier()
                print(f"armor : {armor} | monster : {get_rand_monster(monsters, tier).name} | tier : {tier}")
        else :
            print(f"wsh dood {sys.argv} are not good argument, use 'weapon' or 'armor' dood !")
            
    else :
        print(f"Dood, I expected 2 or 3 argmuments but you gave me {nb_arg} dood !")
        return

def main() :
    global weapons
    global armors
    
    monsters = load_monster_csv(monster_csv)
    debug = "nodebug"
    argv = sys.argv
    if argv[-1].find("debug") > -1 : debug = argv.pop()
    
    # ===== ONLY FOR TEST ===== #
    if debug == "debug" :
        print(f"monster :")
        for m in monsters : print(m)
        print("\n")
        print(f"armors  : {armors}\n")
        print(f"weapons : {weapons}\n")
        print(f"{sys.argv}")
    # ========================= #
    generation(monsters, len(argv))

main()