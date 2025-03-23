import pygame

# Initialize Pygame
pygame.init()

# Initialize the joystick module
pygame.joystick.init()

# Check for connected joysticks
if pygame.joystick.get_count() == 0:
    print("No joystick detected!")
else:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Joystick Name: {joystick.get_name()}")
    print(f"Number of Axes: {joystick.get_numaxes()}")
    print(f"Number of Buttons: {joystick.get_numbuttons()}")

# Main loop to read joystick input
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Read joystick axis movement
        if event.type == pygame.JOYAXISMOTION:
            print(f"Axis {event.axis} moved to {event.value}")

        # Read button press
        if event.type == pygame.JOYBUTTONDOWN:
            print(f"Button {event.button} pressed")

        # Read button release
        if event.type == pygame.JOYBUTTONUP:
            print(f"Button {event.button} released")

        # Read hat (D-pad) movement
        if event.type == pygame.JOYHATMOTION:
            print(f"Hat {event.hat} moved to {event.value}")

pygame.quit()
