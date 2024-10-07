import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define colors
WHITE = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Animation Example")

# Load the sprite sheet
sprite_sheet = pygame.image.load("Main Character Male (1).gif").convert_alpha()

# Define frame dimensions and animation sequences
# Adjust these values based on your sprite sheet structure
FRAME_WIDTH = 20
FRAME_HEIGHT = 20
START_X = 100  # X-coordinate of the starting point
START_Y = 0  # Y-coordinate of the starting point
NUM_ROWS = 3   # Number of rows to iterate through
NUM_COLS = 4   # Number of columns to iterate through

# Extract frames from the sprite sheet
frames = []
for row in range(START_Y, START_Y + NUM_ROWS):
    for col in range(START_X, START_X + NUM_COLS):
        frame_rect = pygame.Rect(col * FRAME_WIDTH, row * FRAME_HEIGHT, FRAME_WIDTH, FRAME_HEIGHT)
        print(frame_rect)
        frame_surface = sprite_sheet.subsurface(frame_rect)
        frames.append(frame_surface)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.game=super().__init__()
        self.frames = frames
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def update(self):
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.image = self.frames[self.frame_index]

# Create player object
player = Player()

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player update
    player.update()

    # Clear the screen
    screen.fill(WHITE)

    # Draw player
    screen.blit(player.image, player.rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(10)

# Quit Pygame
pygame.quit()
sys.exit()

