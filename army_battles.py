class Warrior:
    def __init__(self):
        self.power = 5
        self.life = 50
        self.is_alive = True

class Knight:
    def __init__(self):
        self.power = 7
        self.life = 50
        self.is_alive = True

def fight(ally, enemy):
    flag = 0
    while flag == 0:
        enemy.life -= ally.power
        if enemy.life <= 0:
            enemy.is_alive = False
            break
        ally.life -= enemy.power
        if ally.life <= 0:
            ally.is_alive = False
            break
    return True if ally.is_alive else False

class Army:
    def __init__(self):
        self.units = []
        pass

    def add_units(self, unit, num):
        self.units += [unit() for x in range(3)]


class Battle:

    def fight(self, allies, enemies):
        pass

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
