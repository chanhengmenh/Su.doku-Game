# libraries for the game's graphical interface and settings
import pygame, sys
from Settings import width, height, cell_size
from Table import Table
from Home import Home

#  Initialize Pygame and set up the game window
pygame.init()
screen = pygame.display.set_mode((width, height + (cell_size[1] * 3)))
pygame.display.set_caption("Sudoku")

# Initialize font rendering
pygame.font.init()

# Main class for the Sudoku game
class Main:
    def __init__(self, width, height):

        # Initialize Pygame and set up the game window
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sudoku Game")
        self.FPS = pygame.time.Clock()
        self.color = pygame.Color("green")
        self.lives_font = pygame.font.SysFont("monospace", cell_size[0] // 2)
        self.message_font = pygame.font.SysFont('Bauhaus 93', (cell_size[0]))


#Method to start the game
    def start_game(self):   

        #Initialise the game table 
        table = Table(self.screen)
        while True:
            #main game loop
            self.screen.fill(pygame.Color(0, 191, 255))

            #Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Handle mouse click events
                    table.handle_mouse_click(event.pos)
                
                elif event.type == pygame.KEYDOWN:
                    #Handle keyboard input
                    table.handle_keyboard_input(event.key)

            # udate game table state and display
            if not table.game_over:
                my_lives = self.lives_font.render(f"Lives Left: {table.lives}", True, pygame.Color("black"))
                self.screen.blit(my_lives, ((width // table.SRN) - (cell_size[0] // 2), height + (cell_size[1] * 2.2)))
            
            else:
                if table.lives <= 0 or table.clock.elapsed_time >= table.clock.countdown_time:
                    message = self.message_font.render("GAME OVER!!", True, pygame.Color("red"))
                    self.screen.blit(message, (cell_size[0] + (cell_size[0] // 2), height + (cell_size[1] * 2)))
                elif table.lives > 0:
                    message = self.message_font.render("You Made It!!!", True, self.color)
                    self.screen.blit(message, (cell_size[0] , height + (cell_size[1] * 2)))
            
            table.update()
            pygame.display.flip()
            self.FPS.tick(30)
    
    
    #main game loop
    def main(self):
        #create the home screen and capture the username
        home_screen = Home(self.screen)
        username = home_screen.capture_username()
        if username:
            home_screen.main()
            self.start_game()
    
#Entry the point of the game
if __name__ == "__main__":
    game = Main(width, height + (cell_size[1] * 3))
    game.main()
