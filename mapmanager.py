class MapManager():
    def __init__(self):
        self.model = "resources/block.egg"
        self.texture = "resources/block.png"
        # self.color = (0,0,0.4,0.7)
        self.colors = (
            (0.3, 0.2, 0.9, 0.7),
            (0.6, 0.8, 0.4, 0.9),
            (0.2, 0.4, 0.6, 0.4)
        )
        self.floor = 0
        self.color = self.colors[self.floor]
        self.startNew()

    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setHpr(0, 90, -90)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)

    def change_color(self):
        self.floor += 1
        if self.floor >= len(self.colors):
            self.floor = 0
        self.color = self.colors[self.floor]

    def startNew(self):
        self.land = render.attachNewNode("Land")

    def loadMap(self,filename):
        with open(filename, 'r', encoding = "utf-8") as file:
            y = 0
            for line in file:
                line = line.split(" ")
                line = line[0:-1]
                x = 0
                for i in line:
                    for z in range(int(i)):
                        self.addBlock((x, y, z))
                    x += 1
                y += 1
                self.change_color()