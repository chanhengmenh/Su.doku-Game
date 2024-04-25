import pygame, time
from Settings import cell_size

pygame.font.init()

class Clock:
    def __init__(self):
        self.start_time = None
        self.countdown_time = 10 * 60# 10 minutes in seconds
        self.elapsed_time = 0
        self.font = pygame.font.SysFont("monospace", cell_size[0])
        self.message_color = pygame.Color("pink")

    # Start the countdown
    def start_timer(self):
        self.start_time = time.time()

    # Update the countdown
    def update_timer(self):
        if self.start_time is not None:
            self.elapsed_time = time.time() - self.start_time
            # Check if the countdown has reached 0
            if self.elapsed_time >= self.countdown_time:
                self.stop_timer()
                self.elapsed_time = self.countdown_time # Ensure it doesn't go beyond the countdown time

    # Display the countdown timer
    def display_timer(self):
        remaining_time = self.countdown_time - self.elapsed_time
        secs = int(remaining_time % 60)
        mins = int(remaining_time / 60)
        my_time = self.font.render(f"{mins:02}:{secs:02}", True, self.message_color)
        return my_time

    # Stop the countdown
    def stop_timer(self):
        self.start_time = None

    # Check if the countdown has ended
    def is_countdown_over(self):
        return self.elapsed_time >= self.countdown_time