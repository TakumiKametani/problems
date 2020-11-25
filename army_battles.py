"""
問題文：
...Sir Ronald’s opponent - Umbert, has proved to be a very skillful warrior.
In addition, he was a good fifteen years younger, which gave him a certain advantage.
But Sir Ronald was also very strong - he had the experience of participation in many battles and in several major wars behind his back.
And besides that, in his youth he was known as the best duelist in this land.
Realizing that the forces are equal, each of them had followed the only course possible - to call for help.
Umbert sent for the reinforcement his coachman on a horse, and Sir Ronald used a family horn that sounded more than once in hot battles.
The knight's castle was close enough for the call to arms was heard back there.
Nobody quite knew where the Umbert's accomplices were located, and this made it difficult to come up with a strategy for the battle ahead.
Fortunately, the reinforcements for both sides arrived almost simultaneously.
Now it was more than a question of the girl's honor. There was no peaceful solutions to this matter.
One of the two armies must be destroyed.
In the previous mission - Warriors - you've learned how to make a duel between 2 warriors happen.
Great job! But let's move on to something that feels a little more epic - armies!
In this mission your task is to add new classes and functions to the existing ones.
The new class should be the Army and have the method add_units() - for adding the chosen amount of units to the army.
The first unit added will be the first to go to fight, the second will be the second, ...
Also you need to create a Battle() class with a fight() function, which will determine the strongest army.
The battles occur according to the following principles:
at first, there is a duel between the first warrior of the first army and the first warrior of the second army.
As soon as one of them dies - the next warrior from the army that lost the fighter enters the duel,
and a new fight begins between him and the surviving warrior, who keeps his remaining health.
This continues until all the soldiers of one of the armies die. In this case, the fight() function should return True,
if the first army won, or False, if the second one was stronger.
Note that army 1 has the advantage to start every fight!
"""

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