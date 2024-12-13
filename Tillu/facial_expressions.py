import pygame
import cv2
import os
import time

# Initialize Pygame
pygame.init()

# Set the display dimensions
SCREEN_WIDTH = 240
SCREEN_HEIGHT = 320
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Initialize a clock for frame rate control
CLOCK = pygame.time.Clock()

# Specify the display duration for each video (in seconds)
DISPLAY_TIME = 5  # You can change this value as needed

def play_expression(video_path: str):
    """
    Plays a facial expression video on the Pygame window for a specified duration.
    :param video_path: Path to the video file for the facial expression.
    """
    if not os.path.exists(video_path):
        print(f"Error: Video file {video_path} not found.")
        return

    video = cv2.VideoCapture(video_path)
    start_time = time.time()

    try:
        while True:
            # Check elapsed time
            elapsed_time = time.time() - start_time
            if elapsed_time > DISPLAY_TIME:
                break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # Read a frame from the video
            ret, frame = video.read()
            if not ret:
                video.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Loop the video
                continue

            # Process the frame for Pygame display
            flipped_frame = cv2.flip(frame, 0)  # Flip vertically to match orientation
            frame_resized = cv2.resize(flipped_frame, (SCREEN_HEIGHT, SCREEN_WIDTH))
            frame_rgb = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)
            frame_surface = pygame.surfarray.make_surface(frame_rgb)

            # Display the frame
            SCREEN.fill((0, 0, 0))
            SCREEN.blit(frame_surface, (0, 0))
            pygame.display.update()

            CLOCK.tick(30)  # Limit the frame rate

    finally:
        video.release()

# Define facial expression functions
def blink():
    play_expression("videos/blink.mp4")

def angry():
    play_expression("videos/angry.mp4")

def heart():
    play_expression("videos/heart.mp4")

def love():
    play_expression("videos/love.mp4")

def loading():
    play_expression("videos/loading.mp4")

def music():
    play_expression("videos/music.mp4")

def scarry():
    play_expression("videos/scarry.mp4")

def cute():
    play_expression("videos/cute.mp4")

# Clean up resources when the module is exited
def cleanup():
    pygame.quit()
    quit()
