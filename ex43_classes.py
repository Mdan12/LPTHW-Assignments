from sys import exit
from random import randint
from textwrap import dedent


# Make a class named Scene that is-a object
class Scene(object):
# prints a string and exits the code.
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


# Make a class named Engine that is-a object.
class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
# current scene becomes the opening scene.
# last scene becomes the the scene finished.
    def play(self):
        # from scene_map get the function opening_scene.
        current_scene = self.scene_map.opening_scene()
        # From scene_map get the next_scene function, and call it with parameter 'finished'.
        last_scene = self.scene_map.next_scene('finished')
# While current scene does not equal to last scene the next scene
# will become the the current scene and enters it.
# Current scene is the result of the next scene, next scene name.
        while current_scene != last_scene:
            # from current_scene get the funcion enter.
            next_scene_name = current_scene.enter()
            #From scene_map get the next_scene function, and call it with parameters self, next_scene_name.
            current_scene = self.scene_map.next_scene(next_scene_name)
# From current_scene get the function enter()
# Enter is defined in class Death(scene)
        current_scene.enter()


# Make a class named Death that is-a Scene.
class Death(Scene):
# This is a list.
    quips = [
            "You died. You kinda suck at this.",
            "Your Mom would be proud...if she were smarter.",
            "Such a luser.",
            "I have a small puppy that's better at this.",
            "You're worse than your Dad's jokes."
    ]

    def enter(self):
# Returns a random int (randit) between 0 and the number of items contained
# inside the quips list and because lists in python start with 0 rather than
# 1, take away 1 from the length of the list.
        print(Death.quips[randint(0, len(self.quips)-1)])
# Program exits because of an issue / error /  problem
        exit(1)


#Make a class named CentralCorridor that is-a Scene.
class CentralCorridor(Scene):
# enter prints the string, dedent brings the string back if it's indented.
    def enter(self):
        print(dedent("""
            The Gothons of Planet Percal #35 have invaded your ship and
            destroyed your entire crew. You are the last surviving
            member and your last mission is to get the neutron destruct
            bomb from the Weapons Armory, put it in the bridge, and
            blow the ship after getting into an escape pod.

            You're running down the central corridor to the Weapons
            Armory when a Gothon jumps out, red scaly skin, dark grimy
            teeth, and evil clown costume flowing aroud his hate
            filled body. He's blocking the door to the Armory and
            about to pull a weapon to blast you."""))
# user input
        action = input("> ")
# if user input is shoot it prints the string with it dedented.
# returns death
        if action == "shoot!":
            print(dedent("""
                Quick on the draw you yankk out your blaster and fire
                it at the Gothon. His clown costume is flowing and
                moving around his body, which throws off your aim.
                Your laser hihts his costume but misses him entirely.
                This completely ruins his brand new costume his mother
                bought him, which makes him fly into an insane rage
                and blast you repeatedly in the face until you are
                dead. Then he eats you."""))

            return 'death'
# if user input is dodge!, prints text indented and then returns death.
        elif action == "dodge!":
            print(dedent("""
                Like a world class boxer you dodge, weave, slip and
                slide right as the Gothon's blaster cranks a laser
                past your head. In the middle of your artful dodge
                your foot slips and you bang your head on the metal
                wall and pass out. You wake up shortly after only to
                die as the Gothon stomps on your head and east you.
                """))

            return 'death'
# if user input is tell a joke, prints text indented and returns laser_weapon_armory
        elif action == "tell a joke":
            print(dedent("""
                Lucky for you they made you learn Gothon unsults in
                the academy. You tell the one Gothon joke you know:
                Lbhe zbgure vf fb sng, jura fur fbgf nehbaq gur ubhfr,
                fur fvgf nebhaq gur ubhfr. The Gothon stops, trie
                not to laugh, the busts out luaghin and can't move.
                While he's laughing you run up and shoot him square in
                the head putting him down, then jump through the
                Weapon Armory door.
                """))
            return 'laser_weapon_armory'
# if user input is anything else it prints string and returns back to central_corridor.
        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'
# Make a class named LaserWeaponArmory that is-a Scene.
class LaserWeaponArmory(Scene):
# prints the string dedented.
    def enter(self):
        print(dedent("""
                You do a dive roll into the Weapon Armory, crouch and scan
                the room for more Gothons that might be hiding. It's dead
                quiet, too quiet. You stand up and run to the far side of
                the room and find the neutron bomb in its container.
                There's a keypad lock on the box and you need the code to
                get the bomb out. If you get the code wrong 10 times then
                the lock closes forever and you can't get the bomb. The
                code is 3 digits."""))
# code is equal to 3 numbers between 1 and 9.
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
# user input after the string.
        guess = input("[keypad]> ")
# This just puts the guesses as 0 times.
        guesses = 0
# while the guess is wrong and hasn't hit 10 times
        while guess != code and guesses < 10:
# it prints bzzzzeeed
            print("BZZZZZZEDDD!")
# and adds 1 to guesses each time the code is wrong.
            guesses = guesses + 1
# goes back to user input.
            guess = input("[keypad]> ")
# if user input is the code then it prints the string dedented and goes to the_bridge
        if guess == code:
            print(dedent("""
                The container clicks open and the seal breakd, letting
                gas out. You grab the neutron bomb and tun as fast as
                you can to the bridge where you must place it in the
                right spot.
                """))
            return 'the_bridge'
# if the user input is incorrect 10 times it prints the string dedented and goes to death.
        else:
            print(dedent("""
                The lock buzzes one last time and then you hear a
                sckening melting sound as the mechanism is fused
                together. You decide to sit there, and finally the
                Gothons blow up the ship from their ship and you die.
                """))
            return 'death'

#Make a class named TheBridge that is-a Scene.
class TheBridge(Scene):

#prints the string dedented.
    def enter(self):
        print(dedent("""
            You burst onto the Brdige with the neutron descrutct comc
            under your arm and surprise 5 Gothons who are trying to
            take control of the ship. Each of them has an even uglier
            clown costume than the last. THey haven't pulled their
            weapons out yet, as they see the active bomb under your
            arm and don't want to set it off.
            """))
# user input
        action = input("> ")
# if user input is throw the bomb it prints the string dedented and returns death.
        if action == "throw the bomb":
            print(dedent("""
                In a panic you throw the bomb at the group of Gothons
                and make a leap for the door. Right as your drop it a
                Gothon shoots you right in sht back killing you. As
                you die you see another Gothon frantically try to
                disarm the bomb. You die knowing they will probably
                blow up when it goes off.
                """))
            return 'death'
# if user input is slowly place the bomb it prints the string dedented and returns escape_pod
        elif action == "slowly place the bomb":
            print(dedent("""
                You point your blaster at the bomb under your arm and
                the Gothons put their hands up and start to sweat.
                You inch backward to the door, open it, and then
                carefully place the bomb on the floow, pointing your
                blaster at it. Ypu then jump back through the door,
                punch the close button and blast the lock so the
                Gothons can't get out. Now that the bomb is placed
                you run to the escape pod to get off this tin can.
                """))
            return 'escape_pod'

# if user input is anything else it prints the string and returns to the_bridge
        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"
# Make a class named EscapePod that is-a Scene.
class EscapePod(Scene):

# prints the string dedented.
    def enter(self):
        print(dedent("""
            You rush through the ship desperately trying to make it to
            the escape pod before the whole ship explodes. It seems
            like hardly any Gothons are on the ship, so your run is
            clear of intereference. You get to the chamber with the
            escape pods, and now need to pick one to take. Some of
            them could be damaged but you don't have time to look.
            There's 5 pods, which one do you take?
            """))
# good_pod equals to a random number between 1 and 5
        good_pod = randint(1,5)
# user input after [pod #]
        guess = input("[pod #]> ")
# if the user input is incorrect it prints the string dedented and returns death
        if int(guess) != good_pod:
            print(dedent("""
                You jump into pod {guess} and hit the eject button.
                The pod escapes out into the void of space, then
                implodes as the hull ruptures, crushing your body into
                jam jelly"""))
            return 'death'
# if the user input is correct it prints the string and returns finished
        else:
            print(dedent("""
                You jump into pod {guess} and hit the eject button.
                The pod easily slides out into space heading to the
                planet below. As it flies to the planet, you look
                back and see your ship implode then explode like a
                bright star, taking out the Gothon ship at the same
                time. You won!
                """))
            return 'finished'
# Make a class named Finished that is-a Scene.
class Finished(Scene):
# prints the string and returns finished
    def enter(self):
        print("You won! Good job.")
        return 'finished'

#Make a class named Map that is-a object.
class Map(object):

# dictionary!
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
