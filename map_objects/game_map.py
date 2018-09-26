from map_objects.tile import Tile

class GameMap:
    def __init__(self, width, height):
        tiles = {{Tile(False) for y in range(self.height)] for x in range(self.width)]
        