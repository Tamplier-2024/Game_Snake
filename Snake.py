# Python - Snake (Tamplier)

import pygame

from random import randrange

pygame.init()

# Поле для змейки
def game_screen(screen_width, screen_height):
    return pygame.display.set_mode([screen_width, screen_height])

# Змейка отрисовка
def snake_render(game_field, snake_size, snake_draw):
       [(pygame.draw.rect(game_field, pygame.Color('green'), (x, y , snake_size-1, snake_size-1))) for x, y in snake_draw]

# Еда отрисовка
def food_render(game_field, food_size, food_draw):
      pygame.draw.rect(game_field, pygame.Color('purple'), (*food_draw, food_size-1, food_size-1))

# Шрифты
font_text_score = pygame.font.SysFont('segoe print', 32, bold = False, italic = True)
font_text_gameover = pygame.font.SysFont('segoe print', 64, bold = False, italic = True)

# Ввод данных (дописать)
window_size_x = 700
window_size_y = 700
size = 20

# Переменные
snake_x = randrange(0, window_size_x, size)
snake_y = randrange(0, window_size_y, size)
snake_move_x = 0
snake_move_y = 0
snake = [(snake_x, snake_y)]
snake_lenght = 1
food = randrange(0, window_size_x, size), randrange(0, window_size_y, size)
speed = 10
score = 0

# Запрет движения назад переменные
ignore_move_back = {'W': True, 'S': True, 'A': True, 'D': True,}

# Создание окна
game_window = game_screen(window_size_x, window_size_y)

# Картинка заднего фона
# background = pygame.image.load('background.jpg').convert()

# Создание таймера
game_clock = pygame.time.Clock()

# Игра
while True:
       # Отрисовка
       game_window.fill(pygame.Color('black'))
       # game_window.blit(background, (0, 0))

       render_text_score = font_text_score.render(f'Score: {score}', 1, pygame.Color('red'))
       game_window.blit(render_text_score, (10,10))
       
       snake_render(game_window, size, snake)
       food_render(game_window, size, food)
       pygame.display.flip()

       # Таймер
       game_clock.tick(speed)
       
       # Движение змейки
       pressed_key = pygame.key.get_pressed()
       if pressed_key[pygame.K_w] and ignore_move_back['W']:
            snake_move_x, snake_move_y = 0, -1
            ignore_move_back = {'W': True, 'S': False, 'A': True, 'D': True,}      
       if pressed_key[pygame.K_s] and ignore_move_back['S']:
            snake_move_x, snake_move_y = 0, 1            
            ignore_move_back = {'W': False, 'S': True, 'A': True, 'D': True,}
       if pressed_key[pygame.K_a] and ignore_move_back['A']:
            snake_move_x, snake_move_y = -1, 0
            ignore_move_back = {'W': True, 'S': True, 'A': True, 'D': False,}
       if pressed_key[pygame.K_d] and ignore_move_back['D']:
            snake_move_x, snake_move_y = 1, 0            
            ignore_move_back = {'W': True, 'S': True, 'A': False, 'D': True,}            

       snake_x += snake_move_x * size
       snake_y += snake_move_y * size
       snake.append((snake_x, snake_y))
       snake = snake[-snake_lenght:]
       
       # Змейка кушает :)
       if snake[-1] == food:
             food = randrange(0, window_size_x, size), randrange(0, window_size_y, size)
             snake_lenght += 1
             score +=1
             # speed += 1
       
       # Проигрыш
       if snake_x < 0 or snake_x > window_size_x - size or snake_y < 0 or snake_y > window_size_y - size or len(snake) != len(set(snake)):
             while True:
                   render_text_gameover = font_text_gameover.render('Game Over Baby', 1, pygame.Color('red'))
                   game_window.blit(render_text_gameover, (window_size_x // 10, window_size_y // 3))
                   pygame.display.flip()
                   for event in pygame.event.get():
                         if event.type == pygame.QUIT:
                               exit()
       
       # Закрытие окна крестиком
       for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  exit()