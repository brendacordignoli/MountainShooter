import pygame

print('setup Start')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('setup End')

print('Loop Start')
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # close window
            quit() # end pygame
