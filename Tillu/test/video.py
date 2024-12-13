import pygame
import cv2

# Initialize Pygame
pygame.init()

# Set the display dimensions
screen_width = 240
screen_height = 320
screen = pygame.display.set_mode((screen_width, screen_height))

# Load the video
video_path = "music.mp4"  # Replace with the path to your video file
video = cv2.VideoCapture(video_path)

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Read a frame from the video
    ret, frame = video.read()
    if not ret:
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Loop the video
        continue

    # Process the frame for Pygame display
    flipped_frame = cv2.flip(frame, 0)  # Flip vertically to match orientation
    frame_resized = cv2.resize(flipped_frame, (screen_height, screen_width))
    frame_rgb = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)
    frame_surface = pygame.surfarray.make_surface(frame_rgb)

    # Display the frame
    screen.fill((0, 0, 0))
    screen.blit(frame_surface, (0, 0))
    pygame.display.update()

    clock.tick(30)  # Limit the frame rate

# Clean up resources
video.release()
pygame.quit()
quit()
