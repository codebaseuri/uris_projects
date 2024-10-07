import pygame

# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Player Movement")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define player properties
PLAYER_SIZE = (64, 64)
PLAYER_SPEED = 0

# Load the sprite sheet
sprite_sheet = pygame.image.load("player_sprites.png")

# Define the sprite sheet layout
sprite_layout = {
    "down": [(0, 0), (64, 0), (128, 0), (192, 0)],
    "left": [(0, 64), (64, 64), (128, 64), (192, 64)],
    "right": [(0, 128), (64, 128), (128, 128), (192, 128)],
    "up": [(0, 192), (64, 192), (128, 192), (192, 192)]
}

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface(PLAYER_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.player_direction = "down"
        self.frame = 0
        self.moving = False
        self.vector = pygame.Vector2(0, 0)
        self.direction=(0,0)
        self.sprite_layout = sprite_layout
        self.sprite_sheet=sprite_sheet

    def update(self):
        keys =pygame.key.get_pressed()
        input_vector=pygame.Vector2(0,0)
        spead=3
        if keys[pygame.K_LEFT]:        
            input_vector.x-=spead
            self.direction=input_vector
            self.player_direction = "left"
            self.moving = True
            
               
        elif keys[pygame.K_RIGHT]:
            input_vector.x+=spead
            self.direction=input_vector
            self.player_direction = "right"
            self.moving = True
           
        elif keys[pygame.K_UP]:
            input_vector.y-=spead
            self.direction=input_vector
            self.player_direction = "up"
            self.moving = True
            
        
        elif keys[pygame.K_DOWN]:
            input_vector.y+=spead
            self.direction=input_vector
            self.player_direction = "down"
            self.moving = True
            
        else:
            self.moving = False
        
        if self.moving:
            self.frame = (self.frame + 1) % len(self.sprite_layout[self.player_direction])
        sprite_x, sprite_y = sprite_layout[self.player_direction][self.frame]
        sprite_rect = pygame.Rect(sprite_x, sprite_y, PLAYER_SIZE[0], PLAYER_SIZE[1])
        self.image = pygame.transform.scale(sprite_sheet.subsurface(sprite_rect), PLAYER_SIZE)  
        self.direction=input_vector
        return self.moving
        


# Create the player sprite
player = Player(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Update and draw the player sprite
    player.update()
    screen.blit(player.image, player.rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()