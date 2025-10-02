class Icon:
    def __init__(self, value: int):
        self.speed = 0.0
        self.glow = 0.0
        self.energy = 0.0
        self.x = 0
        self.y = 0
        self.subtype = value  # spinner, slider or hopper

        # spinner
        self.clockwise = False
        self.expand = False

        # slider
        self.vertical = False
        self.distance = 0

        # hopper
        self.visible = False
        self.xcoord = 0
        self.ycoord = 0

        # constructor must set subtype: client must pass value
        # use enum for readability in real design

    def spin(self):
        pass

    def slide(self):
        pass

    def hop(self):
        pass

    def move(self):
        if self.subtype == 1:
            self.spin()
        elif self.subtype == 2:
            self.slide()
        else:
            self.hop()

    def flair(self):
        if self.subtype == 1:
            self.spin()
        elif self.subtype == 2:
            self.slide()
        else:
            self.hop()
