"""
...the clashes between different soldiers occurred here and there, and the new troops kept coming. The conflict gradually was starting to look more like a small war.
"Knights, hear my command! Take your shields! Strengthen the armor! We are taking too much beating," - Sir Ronald shouted.
Nobody’s expected that Umbert's soldiers could compete with the well-trained knights, so at the beginning of the battle the knights used exclusively two-handed swords - no one even thought of being on the defensive. But it seems that it's time to back down and take one-handed swords and shields instead of the former deadly weapons. This will slightly reduce the assault capacity of knights, but will allow them to better defend themselves against the dangerous attacks of enemy soldiers.
In the previous mission - Army battles, you've learned how to make a battle between 2 armies. But we have only 2 types of units - the Warriors and Knights. Let's add another one - the Defender. It should be the subclass of the Warrior class and have an additional defense parameter, which helps him to survive longer. When another unit hits the defender, he loses a certain amount of his health according to the next formula: enemy attack - self defense (if enemy attack > self defense). Otherwise, the defender doesn't lose his health.
The basic parameters of the Defender:
health = 60
attack = 3
defense = 2

Input: The warriors and armies.

Output: The result of the battle (True or False).

How it is used: For the computer games development.

Note: From now on, the tests from "check" part will use another type of warrior: the rookie. Its code is

class Rookie(Warrior):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.health = 50
        self.attack = 1

Precondition: 3 types of units
"""

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")