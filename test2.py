

def move_handle(x , y ,direction):
    move_by=0

    return move_by
import pygame
window_width=700
window_height=500
pygame.init()
clock = pygame.time.Clock()
ball_x_pos = 70
ball_y_pos = 70
finish = False
REFRESH_RATE = 60

white=(78,255,255)
radius =8

IMAGE = r"D:\final_networking_project\assets\Pallet Town (1).gif"



size =(window_width,window_height)
screen=pygame.display.set_mode(size)

pygame.display.set_caption("GAME")
img = pygame.image.load(IMAGE)
screen.blit(img, (0, 0))
pygame.display.flip()
finish = False


direction="up"
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ball_x_pos-=2
    if keys[pygame.K_RIGHT]:
        ball_x_pos+=2
    if  keys[pygame.K_UP]:
        ball_y_pos -= 2
    if keys[pygame.K_DOWN]:
        ball_y_pos += 2

    screen.blit(img, (0, 0))
    pygame.draw.circle(screen, white,[ball_x_pos, ball_y_pos],radius)
    pygame.display.flip()
    clock.tick(REFRESH_RATE)

    img = pygame.image.load(IMAGE)
    screen.blit(img, (0, 0))
    player_image = pygame.image.load('plane.png').convert()
    screen.blit(player_image, [220, 300])
    pygame.display.flip()