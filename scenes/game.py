from ursina import *

class Game(Entity):
    def __init__(self):
        super().__init__(enabled=False)
        self.player = Entity(model='cube', color=color.orange)
        self.ground = Entity(model='plane', scale=20, texture='white_cube')

    def update(self):
        speed = 5 * time.dt
        if held_keys['w']:
            self.player.z += speed
        if held_keys['s']:
            self.player.z -= speed