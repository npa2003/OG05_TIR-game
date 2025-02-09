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

tar_width = target_image.get_width() # получаем размер изображения
tar_height = target_image.get_height()
print(tar_width, tar_height)

tar_width, tar_width = target_image.get_size() # получаем размер изображения альтернативно
print(tar_width, tar_height)

tar_width = 80
tar_height = 80
target_image = pygame.transform.scale(target_image, (tar_width, tar_height)) # трансформируем изображение в новый размер
tar_x = random.randint(0, SCREEN_WIDTH - tar_width)
tar_y = random.randint(0, SCREEN_HEIGHT - tar_height)

color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
print(color)


running = True
while running:
    screen.fill(color) # заполняем поле цветом

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if tar_x < mouse_x < tar_x + tar_width and tar_y < mouse_y < tar_y + tar_height:
                tar_x = random.randint(0, SCREEN_WIDTH - tar_width)
                tar_y = random.randint(0, SCREEN_HEIGHT - tar_height)

    screen.blit(target_image, (tar_x, tar_y))
    pygame.display.update()

pygame.quit()