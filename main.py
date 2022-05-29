from location import Location
from world_graph import WorldGraph
from direction import Direction

location_list = [
    Location("Home", "This is my home"),
    Location("Backyard", "This is my backyard"),
    Location("River", "This is a river behind my house")
]

connector_list = [
    ("Home", "Backyard", Direction.DOWN),
    ("Backyard", "Home", Direction.UP),
    ("Backyard", "River", Direction.LEFT)
]

world_graph = WorldGraph(location_list, "Home", connector_list)
