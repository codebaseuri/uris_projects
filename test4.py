import pygame
import sys

player_frames={"left1":"image_35.png","left2":"image_34.png","left3":"image_36.png",
               "right1": "image_15.png", "right2": "image_16.png", "right3": "image_17.png"
               ,"up1":"image_24.png","up2":"image_25.png","up3":"image_27.png",
               "down1":"image_34.png","down2":"image_35.png","down3":"image_36.png"}
# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Map dimensions
MAP_WIDTH = 544
MAP_HEIGHT = 452
#EEFB
# Upscale factor for the map
UPSCALE_FACTOR = 2

# Define colors
WHITE = (255, 255, 255)
light_blue=(17,219,255)
# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))#
pygame.display.set_caption("Viewport Example")#

# Load the map image
map_picture=r"D:\final_networking_project\assets\Pallet Town (1).gif"
map_image = pygame.image.load(map_picture).convert()  # Replace "map.png" with your map image file

# Upscale the map
upscaled_map_width = MAP_WIDTH * UPSCALE_FACTOR
upscaled_map_height = MAP_HEIGHT * UPSCALE_FACTOR
upscaled_map = pygame.transform.scale(map_image, (upscaled_map_width, upscaled_map_height))

# Player sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"D:\final_networking_project\assets\image_24.png").convert_alpha()
        self.image=pygame.transform.scale_by(self.image,2)
        self.image.set_colorkey(light_blue)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def update(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

# Create player sprite
player = Player()

# Group for all sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(player)


direction="up"
# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    dx, dy = 0, 0
    if keys[pygame.K_LEFT]:
        dx = -3
    if keys[pygame.K_RIGHT]:
        dx = 3
    if keys[pygame.K_UP]:
        dy = -3
    if keys[pygame.K_DOWN]:
        dy = 3

    # Update player position
    player.update(dx, dy)

    # Ensure the player stays within the bounds of the map
    player.rect.x = max(0, min(player.rect.x, upscaled_map_width - player.rect.width))
    player.rect.y = max(0, min(player.rect.y, upscaled_map_height - player.rect.height))


    # Calculate the viewport (camera) position
    viewport_x = max(0, min(player.rect.x - SCREEN_WIDTH // 2, upscaled_map_width - SCREEN_WIDTH))
    viewport_y = max(0, min(player.rect.y - SCREEN_HEIGHT // 2, upscaled_map_height - SCREEN_HEIGHT))

    # Draw the upscaled map with the viewport
    screen.blit(upscaled_map, (0, 0), (viewport_x, viewport_y, SCREEN_WIDTH, SCREEN_HEIGHT))

    # Draw all sprites
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
