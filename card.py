
import pygame
default_speed = 120

class Card:
    def __init__(self, fname, x1, y1, x2, y2, speed = default_speed ):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.tx1 = x1
        self.ty1 = y1
        self.tx2 = x2
        self.ty2 = y2
        self.speed = speed
        self.fname = fname
        self.frame_count = 0
        self.live = True

        # print(fname)
        self.image = pygame.image.load(fname)
        self.image = pygame.transform.scale(self.image, (self.x2 - self.x1, self.y2 - self.y1))

    def set_target(self, tx1, ty1, tx2, ty2):
        self.tx1 = tx1
        self.ty1 = ty1
        self.tx2 = tx2
        self.ty2 = ty2
    
    def update(self):

        self.frame_count += 1

        if self.frame_count % 3 == 0:
            self.image = pygame.image.load(self.fname)
            self.image = pygame.transform.scale(self.image, (self.x2 - self.x1, self.y2 - self.y1))
            self.frame_count = 0

        # Calculate distance to target position
        dx1 = self.tx1 - self.x1
        dy1 = self.ty1 - self.y1
        dx2 = self.tx2 - self.x2
        dy2 = self.ty2 - self.y2
        dist1 = (dx1**2 + dy1**2)**0.5
        dist2 = (dx2**2 + dy2**2)**0.5
        # If distance is greater than speed, move towards target
        if dist1 > self.speed:
            self.x1 += int(dx1/dist1*self.speed)
            self.y1 += int(dy1/dist1*self.speed)
        if dist2 > self.speed:
            self.x2 += int(dx2/dist2*self.speed)
            self.y2 += int(dy2/dist2*self.speed)
        # If distance is less than speed, set position to target
        if dist1 <= self.speed:
            self.x1 = self.tx1
            self.y1 = self.ty1
        if dist2 <= self.speed:
            self.x2 = self.tx2
            self.y2 = self.ty2
    
    def render(self, screen):
        # rescale image into target size
        self.image = pygame.transform.scale(self.image, (self.x2 - self.x1, self.y2 - self.y1))
        # Draw image onto screen
        screen.blit(self.image, (self.x1, self.y1))
