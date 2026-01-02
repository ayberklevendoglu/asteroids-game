import pygame
import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from shot import Shot



def main():
    print("Starting Asteroids with pygame version: VERSION =", pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    updatable.add(player)
    drawable.add(player)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)



    clock = pygame.time.Clock()
    dt = 0
    


    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000  # Delta time in seconds
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()



if __name__ == "__main__":
    main()
