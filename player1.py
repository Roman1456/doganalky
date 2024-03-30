import pygame



class Pogonec:
    def __init__(self,x,y,w,h,img,speed):
        self.photo = pygame.transform.scale(pygame.image.load(img),(w,h))
        self.hitbox = self.photo.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), self.hitbox)
        window.blit(self.photo, (self.hitbox.x, self.hitbox.y))


    def move1(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.hitbox.y -= self.speed

        if keys[pygame.K_DOWN]:
            self.hitbox.y += self.speed

        if keys[pygame.K_LEFT]:
            self.hitbox.x += self.speed

        if keys[pygame.K_RIGHT]:
            self.hitbox.x -= self.speed