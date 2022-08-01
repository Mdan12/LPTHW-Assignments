from nose.tools import *
from ex47.game import Room

def test_room():
    # Room is-a object in game.py but ex47_test is calling Room with 2 parameters (the 2 strings.)
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. There's a
                door to the north.""")
    # This is for nosetests to check if name = GoldRoom and paths dictionary is still empty.
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

def test_room_paths():
    #Once again calling Room with 2 parameters, depending on which direction you're going.
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")
    #This updates the dictionary path with these 2 value pairs.
    center.add_paths({'north': north, 'south': south})
    #checking if paths has these two value pairs in the dictionary. For nosetests
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    #Again calling Room with 2 parameters.
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeons", "It's dark down here, you can go up.")
    #updating 4 value keys to paths the dictionary.
    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})
    #checking if these value keys are in fact a part of paths dictionary. For nosetests.
    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)
