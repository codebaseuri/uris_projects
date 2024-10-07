import pygame
window_width=700
window_height=500
pygame.init()

white=(255,255,255)

IMAGE = r"D:\final_networking_project\assets\Pallet Town (1).gif"



size =(window_width,window_height)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("GAME")
#load the screen
#screen.fill(white)
#pygame.display.flip()
img = pygame.image.load(IMAGE)
screen.blit(img, (150, 0))
pygame.display.flip()
finish = False

while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True


