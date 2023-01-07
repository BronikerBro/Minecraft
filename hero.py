class Hero:
    def __init__(self, position, land):
        self.land = land
        self.hero = loader.loadModel("smiley")
        self.hero.setPos(position)
        self.hero.setColor(1, 0.5, 0, 1)
        self.hero.setScale(0.3)
        self.hero.reparentTo(render)
        self.setCameraToFace()
        self.events()
        self.lastx = 0
        self.lasty = 0
        self.multiplier = 0.1
        taskMgr.add(self.getmouse, 'getmouse')


    def setCameraToFace(self):
        base.disableMouse()
        base.camera.reparentTo(self.hero)
        base.camera.setH(180)
        base.camera.setPos(0, 0, 1.5)
        self.cameraToFace = True

    def unpinCameraFace(self):
        # base.mouseInterfaceNode.setPos(self.hero.getX(), self.hero.getY(), self.hero.getZ()+3)
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2]-3)
        base.camera.reparentTo(render)
        base.enableMouse()

        self.cameraToFace = False

    def events(self):
        self.keyMap = {"left": 0, "right": 0, "forward": 0, "back": 0, }
        self.prevtime = 0
        base.accept('f5', self.changeView)
        base.accept('q', self.turn_left)
        base.accept('q'+"-repeat", self.turn_left)
        base.accept('e', self.turn_right)
        base.accept('e' + "-repeat", self.turn_right)

    def changeView(self):
        if self.cameraToFace:
            self.unpinCameraFace()
        else:
            self.setCameraToFace()

    def turn_left(self):
        # angle = self.hero.getH()+ 5 * self.multiplier
        self.hero.setH(-190*self.lastx % 360)

    def turn_right(self):
        # angle = self.hero.getH() - 5 * self.multiplier
        self.hero.setH(-190*self.lastx % 360)

    def turn_up(self):
        # angle = self.hero.getH()+ 5 * self.multiplier
        self.hero.setP(-90*self.lasty % 360)

    def turn_down(self):
        # angle = self.hero.getH() - 5 * self.multiplier
        self.hero.setP(-90*self.lasty % 360)

    def getmouse(self, task):
        if base.mouseWatcherNode.hasMouse():
            x = round(base.mouseWatcherNode.getMouseX(), 2)
            y = round(base.mouseWatcherNode.getMouseY(), 2)
            if self.lastx != x:
                if 90*x<0:
                    self.turn_left()
                if 90*x>0:
                    self.turn_right()
            if self.lasty != y:
                if 90*y<0:
                    self.turn_up()
                if 90*y>0:
                    self.turn_down()
            # if x < -0.25:
            #     self.turn_left()
            # if x > 0.25:
            #     self.turn_right()
            # if self.lastx != x:
            #     self.multiplier = abs(self.lastx-x) * 10
            self.lastx = x
            self.lasty = y

        return task.again