import pygame
import sys
from datetime import datetime

# Initialize Pygame
pygame.init()

# Set the display dimensions
screen_width = 240
screen_height = 320
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("7-Segment Date & Time Display")

# Colors
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
GRAY = (50, 50, 50)

# Segment definitions for each digit (a-g segments)
SEGMENTS = {
    '0': 'abcdef',
    '1': 'bc',
    '2': 'abged',
    '3': 'abgcd',
    '4': 'fgbc',
    '5': 'afgcd',
    '6': 'afgedc',
    '7': 'abc',
    '8': 'abcdefg',
    '9': 'abfgcd',
    '-': 'g'
}

def draw_segment(surface, pos, segment, color, size=20, thickness=8, slant= 0):
    x, y = pos
    if segment == 'a':
        x_offset = int(y * slant)
        pygame.draw.line(surface, color, 
                        (x + x_offset, y), 
                        (x + size + x_offset, y), thickness)
    elif segment == 'b':
        x_offset_top = int(y * slant)
        x_offset_bottom = int((y + size) * slant)
        pygame.draw.line(surface, color, 
                        (x + size + x_offset_top, y), 
                        (x + size + x_offset_bottom, y + size), thickness)
    elif segment == 'c':
        x_offset_top = int((y + size) * slant)
        x_offset_bottom = int((y + 2*size) * slant)
        pygame.draw.line(surface, color, 
                        (x + size + x_offset_top, y + size), 
                        (x + size + x_offset_bottom, y + 2*size), thickness)
    elif segment == 'd':
        x_offset = int((y + 2*size) * slant)
        pygame.draw.line(surface, color, 
                        (x + x_offset, y + 2*size), 
                        (x + size + x_offset, y + 2*size), thickness)
    elif segment == 'e':
        x_offset_top = int((y + size) * slant)
        x_offset_bottom = int((y + 2*size) * slant)
        pygame.draw.line(surface, color, 
                        (x + x_offset_top, y + size), 
                        (x + x_offset_bottom, y + 2*size), thickness)
    elif segment == 'f':
        x_offset_top = int(y * slant)
        x_offset_bottom = int((y + size) * slant)
        pygame.draw.line(surface, color, 
                        (x + x_offset_top, y), 
                        (x + x_offset_bottom, y + size), thickness)
    elif segment == 'g':
        x_offset = int((y + size) * slant)
        pygame.draw.line(surface, color, 
                        (x + x_offset, y + size), 
                        (x + size + x_offset, y + size), thickness)

def draw_digit(surface, digit, pos, size=20):
    active_segments = SEGMENTS.get(str(digit), '')
    
    # Draw all segments in gray first (OFF state)
    for segment in 'abcdefg':
        draw_segment(surface, pos, segment, GRAY, size)
    
    # Draw active segments in orange (ON state)
    for segment in active_segments:
        draw_segment(surface, pos, segment, ORANGE, size)

def draw_text(surface, text, start_pos, digit_spacing=30, size=20):
    x, y = start_pos
    for char in text:
        if char.isdigit() or char == '-':
            draw_digit(surface, char, (x, y), size)
        x += digit_spacing

def display_date_time():
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M")
    
    # Create a surface for the rotated display
    text_surface = pygame.Surface((screen_height, screen_width))
    text_surface.fill(BLACK)
    
    # Draw date and time on the temporary surface
    draw_text(text_surface, date_str, (20, 40), 35, 25)
    draw_text(text_surface, time_str, (20, 160), 45, 35)
    
    # Rotate the surface
    rotated_surface = pygame.transform.rotate(text_surface, 270)
    
    # Clear the screen and blit the rotated surface
    screen.fill(BLACK)
    screen.blit(rotated_surface, (0, 0))
    pygame.display.flip()

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    display_date_time()
    clock.tick(30)  # Limit to 30 FPS

pygame.quit()
sys.exit()