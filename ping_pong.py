from pygame import *

window = display.set_mode((700,500))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('fon.jpg'), (700,500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w,h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Platform(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y > 495:
            self.rect.y += self.speed

    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y > 495:
            self.rect.y += self.speed

platform1 = Platform('platform.png', 30, 220, 10, 20, 75)
platform2 = Platform('platform.png', 650, 220, 10, 20, 75)

clock = time.Clock()
FPS = 60

game = True
finish = False

while game:
    

    if finish != True:
        window.blit(background, (0,0))
        
        platform1.reset()
        platform1.update_l()
        platform2.reset()
        platform2.update_r()
        
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
    display.update()
    