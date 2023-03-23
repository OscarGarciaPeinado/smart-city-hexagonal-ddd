class LightStatus:
    def __init__(self, active: bool):
        self.active = active

    def turn(self):
        self.active = not self.active

