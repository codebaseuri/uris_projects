import pygame

# Initialize PyGame
def main(window,socket):
    pygame.init()
    global username_text_input, password_text_input
    # Set up the window
    window_width = 1280
    window_height = 720
    #window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Pokemon Battlegrounds")

    # Define colors
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    cyan = (0, 255, 255)    

    # Load and scale background images
    background_image = pygame.image.load('bk1.jpg')
    background_image = pygame.transform.scale(background_image, (window_width, window_height))
    login_background_image = pygame.image.load('lukario1.jpg')
    login_background_image = pygame.transform.scale(login_background_image, (window_width, window_height))

    # Define buttons
    button_width = 200
    button_height = 50
    button_x = window_width // 2 - button_width // 2
    button_y_start = window_height // 2 - 100

    signup_button_rect = pygame.Rect(button_x, button_y_start, button_width, button_height)
    play_button_rect = pygame.Rect(button_x, button_y_start + 60, button_width, button_height)
    quit_button_rect = pygame.Rect(button_x, button_y_start + 120, button_width, button_height)
    other_button_rect = pygame.Rect(button_x, button_y_start + 180, button_width, button_height)

    # Define button text
    font = pygame.font.Font(None, 36)
    signup_text = font.render("Sign Up", True, WHITE)
    play_text = font.render("Play Game", True, WHITE)
    quit_text = font.render("Quit", True, WHITE)
    other_text = font.render("Other", True, WHITE)

    # Define game title
    title_font = pygame.font.Font(None, 72)
    title_text = title_font.render("Pokemon Battlegrounds", True, RED)
    title_rect = title_text.get_rect(center=(window_width // 2, 100))

    # Define login screen elements
    username_font = pygame.font.Font(None, 36)
    password_font = pygame.font.Font(None, 36)
    username_text = username_font.render("Username:", True, WHITE)
    password_text = password_font.render("Password:", True, WHITE)
    username_input_rect = pygame.Rect(window_width // 2 - 150, window_height // 2 - 50, 300, 50)
    password_input_rect = pygame.Rect(window_width // 2 - 150, window_height // 2 + 50, 300, 50)
    back_button_rect = pygame.Rect(50, 50, 150, 50)
    login_button_rect = pygame.Rect(window_width // 2  -150, window_height // 2 + 150, 200, 50)
    login_text = font.render("Login", True, cyan)
    back_text = font.render("Back", True, WHITE)

    # Game loop
    running = True
    show_login_screen = False
    username_text_input = ""
    password_text_input = ""
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if show_login_screen:
                    if back_button_rect.collidepoint(mouse_pos):
                        show_login_screen = False
                        username_text_input = ""
                        password_text_input = ""
                    elif login_button_rect.collidepoint(mouse_pos):
                        # Handle login button click
                        print("Login button clicked")
                        print("sending username and password to server")
                        username_input_text=""
                        password_input_text=""

                    else:
                        # Handle login screen input
                        if username_input_rect.collidepoint(mouse_pos):
                            username_text_input = ""
                            active_input_rect = username_input_rect

                        elif password_input_rect.collidepoint(mouse_pos):
                            password_text_input = ""
                            active_input_rect = password_input_rect
                else:
                    if signup_button_rect.collidepoint(mouse_pos):
                        # Handle sign up button click
                        print("Sign up button clicked")
                    elif play_button_rect.collidepoint(mouse_pos):
                        # Show login screen
                        show_login_screen = True
                    elif quit_button_rect.collidepoint(mouse_pos):
                        # Handle quit button click
                        running = False
                    elif other_button_rect.collidepoint(mouse_pos):
                        # Handle other button click
                        print("Other button clicked")
            elif event.type == pygame.KEYDOWN:
                if show_login_screen:
                    if event.key == pygame.K_RETURN:
                        if active_input_rect == username_input_rect:
                            print("Username:", username_text_input)
                            #username_text_input = ""
                        elif active_input_rect == password_input_rect:
                            print("Password:", password_text_input)
                            #password_text_input = ""

                    if event.key == pygame.K_BACKSPACE:
                        if active_input_rect == username_input_rect:
                            username_text_input = username_text_input[:-1]
                        else:
                            password_text_input = password_text_input[:-1]
                    else:
                        if active_input_rect == username_input_rect:
                            username_text_input += event.unicode
                        else:
                            password_text_input += event.unicode

        # Clear the window
        window.fill(BLACK)

        if show_login_screen:
            # Draw login screen
            window.blit(login_background_image, (0, 0))
            window.blit(username_text, (window_width // 2 - 150, window_height // 2 - 100))
            window.blit(password_text, (window_width // 2 - 150, window_height // 2))
            pygame.draw.rect(window, WHITE, username_input_rect, 2)
            pygame.draw.rect(window, WHITE, password_input_rect, 2)
            username_input_text = username_font.render(username_text_input, True, WHITE)
            password_input_text = password_font.render(password_text_input, True, WHITE)
            window.blit(username_input_text, (window_width // 2 - 140, window_height // 2 - 40))
            window.blit(password_input_text, (window_width // 2 - 140, window_height // 2 + 60))
            pygame.draw.rect(window, RED, back_button_rect)

            pygame.draw.rect(window, WHITE, login_button_rect)
            window.blit(login_text, (window_width // 2 - 100, window_height // 2 + 150))



            window.blit(back_text, (60, 60))

        else:
            # Draw main screen
            window.blit(background_image, (0, 0))
            pygame.draw.rect(window, RED, signup_button_rect)
            pygame.draw.rect(window, RED, play_button_rect)
            pygame.draw.rect(window, RED, quit_button_rect)
            pygame.draw.rect(window, RED, other_button_rect)
            window.blit(signup_text, (button_x + 50, button_y_start + 10))
            window.blit(play_text, (button_x + 50, button_y_start + 70))
            window.blit(quit_text, (button_x + 75, button_y_start + 130))
            window.blit(other_text, (button_x + 50, button_y_start + 190))
            window.blit(title_text, title_rect)

        # Update display
        pygame.display.flip()

    # Quit PyGame
    pygame.quit()
    return False