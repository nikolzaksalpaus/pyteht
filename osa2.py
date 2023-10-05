import pygame
import random

naytto = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Piirtäminen")

def piirraKuva(tiedosto, x, y):
    kuva = pygame.image.load(tiedosto).convert()
    naytto.blit(kuva, (x, y))

def main():
    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break

        naytto.fill((0, 0, 0))
        x = random.randint(1,400)
        y = random.randint(1,400)
        piirraKuva("vihrea.png", x, y)
        pygame.display.flip()

main()