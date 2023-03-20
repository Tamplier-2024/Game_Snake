# Python - Snake (Tamplier)

import pygame

from random import randrange

pygame.init()

# Шрифты
font_text_snake = pygame.font.SysFont('segoe print', 32, bold = True, italic = False)
font_text_info = pygame.font.SysFont('segoe print', 24, bold = False, italic = True)
font_text_by = pygame.font.SysFont('segoe print', 16, bold = True, italic = False)
font_text_gameover = pygame.font.SysFont('segoe print', 48, bold = False, italic = True)

# Ввод данных (дописать)
game_window_size_x = 800
game_window_size_y = 640
field_window_size_x = 600
field_window_size_y = 600
size = 30

# Переменные
snake_x = randrange(0, field_window_size_x, size)
snake_y = randrange(0, field_window_size_y, size)
snake_move_x = 0
snake_move_y = 0
snake = [(snake_x, snake_y)]
snake_lenght = 1
food = randrange(0, field_window_size_x, size), randrange(0, field_window_size_y, size)
random_food_color = lambda : (randrange(0, 256), randrange(0, 256), randrange(0, 256))
food_color = random_food_color()
speed = 10
score = 0
record = 0

# Запрет движения назад переменные
ignore_move_back = {'W': True, 'S': True, 'A': True, 'D': True,}

# Создание игрового окна, поля для змейки, и сетки поля
game_window = pygame.display.set_mode([game_window_size_x, game_window_size_y])
pygame.display.set_caption('SNAKE')
field_window = pygame.Surface([field_window_size_x, field_window_size_y])
field_grid = [pygame.Rect(grid_x * size, grid_y * size, size, size) for grid_x in range(field_window_size_x // size) for grid_y in range(field_window_size_y // size)]

# Картинка на задний фон
background_image = pygame.image.load("background.jpg").convert()

# Создание таймера
game_clock = pygame.time.Clock()

# Загрузка рекорда
def load_record():
      try:
            with open('record') as file_record:
                  return file_record.readline()
      except FileNotFoundError:
            with open('record', 'w') as file_record:
                  file_record.write('0')

# Сохранение рекорда
def save_record(old_record, new_score):
      new_record = max(int(old_record), new_score)
      with open('record', 'w') as file_record:
                  file_record.write(str(new_record))

# Игра
while True:
       # Закраска игрового окна
       # game_window.fill(pygame.Color(0, 0, 0))
       game_window.blit(background_image, (0, 0))
       # Наложение поля змейки
       game_window.blit(field_window, (20, 20))
       # Закраска поля змейки
       field_window.fill(pygame.Color(63, 63, 63))
       # Сетка на поле змейки
       [pygame.draw.rect(field_window, (0, 0, 0), grid, 1) for grid in field_grid]
       # Название игры и версия
       render_text_snake = font_text_snake.render('SNAKE', 1, pygame.Color(255, 255, 127))
       game_window.blit(render_text_snake, (field_window_size_x + 50, 10))
       # Очки и рекорд
       render_text_score = font_text_info.render(f'Score: {score}', 1, pygame.Color(63, 191, 63))
       game_window.blit(render_text_score, (field_window_size_x + 50, 70))
       record = load_record()
       render_text_record = font_text_info.render(f'Record: {record}', 1, pygame.Color(191, 63, 63))
       game_window.blit(render_text_record, (field_window_size_x + 50, 100))
       # Версия и автор
       render_text_version = font_text_by.render('Version 1.1', 1, pygame.Color(255, 255, 255))
       game_window.blit(render_text_version, (field_window_size_x + 60, game_window_size_y - 70))
       render_text_author = font_text_by.render('by Tamplier', 1, pygame.Color(255, 255, 255))
       game_window.blit(render_text_author, (field_window_size_x + 60, game_window_size_y - 50))
       # Управление
       render_text_control = font_text_info.render('Control', 1, pygame.Color(127, 127, 191))
       game_window.blit(render_text_control, (field_window_size_x + 50, 150))
       render_text_up = font_text_info.render('Up     : w', 1, pygame.Color(127, 127, 191))
       game_window.blit(render_text_up, (field_window_size_x + 50, 175))
       render_text_down = font_text_info.render('Down : s', 1, pygame.Color(127, 127, 191))
       game_window.blit(render_text_down, (field_window_size_x + 50, 200))
       render_text_left = font_text_info.render('Left   : a', 1, pygame.Color(127, 127, 191))
       game_window.blit(render_text_left, (field_window_size_x + 50, 225))
       render_text_right = font_text_info.render('Right : d', 1, pygame.Color(127, 127, 191))
       game_window.blit(render_text_right, (field_window_size_x + 50, 250))

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
             snake_lenght += 1
             score +=1
             # speed += 1
             food_color = random_food_color()
             food = randrange(0, field_window_size_x, size), randrange(0, field_window_size_y, size)
                        
 
       # Проигрыш
       if snake_x < 0 or snake_x > field_window_size_x - size or snake_y < 0 or snake_y > field_window_size_y - size or len(snake) != len(set(snake)):
             while True:
                   save_record(record, score)
                   render_text_gameover = font_text_gameover.render('Game Over Baby', 1, pygame.Color('red'))
                   game_window.blit(render_text_gameover, (game_window_size_x // 7, game_window_size_y // 2.5))
                   pygame.display.flip()                   
                   for event in pygame.event.get():
                         if event.type == pygame.QUIT:
                               exit()

       # Змейка отрисовка
       [(pygame.draw.rect(field_window, pygame.Color('green'), (x, y , size-1, size-1))) for x, y in snake]
       # Еда отрисовка разными цветами
       pygame.draw.rect(field_window, food_color, (*food, size-1, size-1))
       
       pygame.display.flip()
   
       # Закрытие окна крестиком
       for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  exit()