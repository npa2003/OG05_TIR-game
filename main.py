import pygame
import random

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption('Игра ТИР')
icon = pygame.image.load('image/main_icon.png')
pygame.display.set_icon(icon)

target_image = pygame.image.load('image/target_icon.png')

target_width = target_image.get_width() # получаем размер изображения
target_height = target_image.get_height()
print(target_width, target_height)

target_width, target_width = target_image.get_size() # получаем размер изображения альтернативно
print(target_width, target_height)

target_width = 80
target_height = 80
target_image = pygame.transform.scale(target_image,(target_width, target_height))
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
print(color)


running = True
while running:
    screen.fill(color) # заполняем поле цветом

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(target_image, (target_x, target_y))
    pygame.display.update()



pygame.quit()