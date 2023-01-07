from direct.showbase.ShowBase import ShowBase
from mapmanager import MapManager
from hero import Hero


class Game(ShowBase):
    def __init__(self):
        super().__init__(self)
        # self.model = loader.loadModel('models/environment')
        # self.model.reparentTo(render)
        # self.model.setScale(0.1)
        # self.model.setPos(-2, 25, -3)
        self.land = MapManager()
        base.camLens.setFov(90)
        self.land.loadMap("map.txt")
        self.hero = Hero((10, 5, 2), self.land)


game = Game()
game.run()