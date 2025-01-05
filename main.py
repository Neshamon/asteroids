import pygame
from constants import *
from player import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable = pygame.sprite.Group(player)
    drawable = pygame.sprite.Group(player)
    player.containers = (updatable, drawable)
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        clock.tick(60)
        dt = int(clock.tick(60)) / 1000
        for ele in updatable:
            ele.update(dt)
        for ele in drawable:
            ele.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
