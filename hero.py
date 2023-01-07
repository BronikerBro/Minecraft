
import sys
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
        base.accept('w', self.forward)
        base.accept('w' + '-repeat', self.forward)
        base.accept('s', self.backward)
        base.accept('s' + '-repeat', self.backward)
        base.accept('a', self.left)
        base.accept('a' + '-repeat', self.left)
        base.accept('d', self.right)
        base.accept('d' + '-repeat', self.right)
        # taskMgr.add(self.controlCamera, 'camera-task')
        base.accept("escape", sys.exit)


    def changeView(self):
        if self.cameraToFace:
            self.unpinCameraFace()
        else:
            self.setCameraToFace()

    def turn_left(self):
        # angle = self.hero.getH()+ 5 * self.multiplier
        self.hero.setH(-200*self.lastx % 360)

    def turn_right(self):
        # angle = self.hero.getH() - 5 * self.multiplier
        self.hero.setH(-200*self.lastx % 360)

    def turn_up(self):
        # angle = self.hero.getH()+ 5 * self.multiplier
        self.hero.setP(-100*self.lasty % 360)

    def turn_down(self):
        # angle = self.hero.getH() - 5 * self.multiplier
        self.hero.setP(-100*self.lasty % 360)

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


    def move(self, angle):
        pos = self.get_angle(angle)
        self.hero.setPos(pos)


    def fly(self):
        pass


    def difference_angle(self, angle):
        if angle >=0 and angle < 20 or angle >= 335 and angle < 360:
            return 0,-1
        elif angle >= 20 and angle < 65:
            return 1, -1
        elif angle >= 65 and angle < 110:
            return 1, 0
        elif angle >= 110 and angle < 155:
            return 1, 1
        elif angle >= 155 and angle < 200:
            return 0, 1
        elif angle >= 200 and angle < 245:
            return -1, 1
        elif angle >= 245 and angle < 290:
            return -1, 0
        elif angle >= 290 and angle < 335:
            return -1, -1


    def get_angle(self, angle):
        from_x, from_y, from_z = round(self.hero.getPos())
        dx, dy = self.difference_angle(angle)

        return from_x + dx, from_y + dy, from_z

    def forward(self):
        angle = (self.hero.getH()+0) % 360
        self.move(angle)

    def backward(self):
        angle = (self.hero.getH()+ 180) % 360
        self.move(angle)

    def left(self):
        angle = (self.hero.getH()+90) % 360
        self.move(angle)

    def right(self):
        angle = (self.hero.getH()+270) % 360
        self.move(angle)



