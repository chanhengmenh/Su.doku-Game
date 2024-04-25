#libraries for the game's graphical interface and input handling
import pygame, sys
import re

# Define the screen dimensions
width, height = 450, 600

# Frame Per Second
FPS = 60 

#define navi and gold
dark_navi_color = pygame.Color(0, 0, 128)
dark_gold_color = pygame.Color(139, 101, 0) # Dark gold

#InputBox class for the input
class InputBox:
    def __init__(self, x, y, width, height, text=''):
        # Initialize the input box with its position, size, and initial text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = pygame.Color('lightskyblue3')
        self.text = text
        self.txt_surface = pygame.font.Font(None, 32).render(text, True, pygame.Color('black'))
        self.active = False
    #Handle event for the input box
    def handle_event(self, event):
        #Handle mouse clicks and keyboard input
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
        if event.type == pygame.KEYDOWN:
            if self.active:
                #Handle special keys and text input
                if event.key == pygame.K_RETURN:
                    print("Enter key pressed.")
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                    print("Text changed:", self.text) # Print message when text is changed
                else:
                    self.text += event.unicode
                    print("Text added:", self.text) # Print message when text is added
                self.txt_surface = pygame.font.Font(None, 32).render(self.text, True, pygame.Color('black'))
    
    #Update the input box's size based on the text
    def update(self):
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    #Draw the input box on the screen
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))

#Button class for clickable Buttons
class Button:
    def __init__(self, screen, text, x, y, width, height, font, color, callback=None):
        
        #Initialize the button with its propertiesand callback function
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = font
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.text_surface = self.font.render(self.text, True, "yellow")
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)
        self.callback = callback

    #Draw the button on the screen
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text_surface, (self.rect.x + 5, self.rect.y + 5))

    #Check if the button was clicked
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    #Handle the button click
    def handle_click(self):
        if self.callback:
            self.callback()

#Hoem class foe the home screen 
class Home:
    def __init__(self, screen):
        #Initialise the home screen with its components
        self.screen = screen
        self.start_button_clicked = False
        self.font = pygame.font.SysFont('Bauhaus 93', 60)
        self.button_font = pygame.font.SysFont('Bauhaus 93', 40)
        
        # Initialize the input box for the username
        self.name_box = InputBox(width // 2 - 150, 2 * height // 3 - 100, 300, 50)
        
        # Initialize buttons
        self.start_button = Button(self.screen, "START", width // 2 - 50 - 150, 4 * height // 5, 150, 60, self.button_font, "red", callback=self.start_game)
        self.exit_button = Button(self.screen, "EXIT", width // 2 + 50, 4 * height // 5, 150, 60, self.button_font, "red", callback=self.exit_game)
        
        # Render the text
        self.text = "Sudoku Game!"
        self.text_surface = self.font.render(self.text, True, pygame.Color(dark_gold_color))

    #Draw the home screen
    def draw(self, screen): # Modify this line to accept screen as a parameter
        self.screen.fill(dark_navi_color) # Fill the screen with a background color
        self.name_box.draw(self.screen) # Draw the name input box
        self.start_button.draw(self.screen) # Draw the start button
        self.exit_button.draw(self.screen) # Draw the exit button
        # Draw the text surface on the screen at the specified location
        screen.blit(self.text_surface, (width // 2 - 190, height // 4))



    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.exit_button.is_clicked(event.pos):
                    pygame.quit()
                    sys.exit()


    #Start the game
    def start_game(self):
        if self.name_box.text:
            print(f"username: {self.name_box.text}")
            print("Starting the game...")
            # Add the logic to start the game here
        else:
            print("User information not provided.")

    #Quit the game
    def exit_game(self):
        print("Exiting the game...")
        pygame.quit()
        sys.exit()

    
    #Capture the username from the GUI
    def capture_username(self):
        # This method should capture the username from the GUI
        # and return it. This is a placeholder implementation.
        username = "example_username" # Replace this with actual GUI input capture
        return username

    #check if the start button was clicked
    def start_game_triggered(self):
        # This method should return True if the "Start" button was clicked
        # You might need to implement logic to track the button click state
        return self.start_button_clicked # Assuming you have a way to track this state


    #Main loop for the home
    def main(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.name_box.handle_event(event)
                if event.type == pygame.MOUSEBUTTONDOWN:    
                    if self.start_button.is_clicked(event.pos):
                        self.start_button.handle_click()
                    elif self.exit_button.is_clicked(event.pos):
                        self.exit_button.handle_click()

            # Draw everything
            self.draw(self.screen)
            pygame.display.flip()

        # Optionally, perform any cleanup or setup for the game here


