import pygame
import random

liikkuOikealle = False
liikkuVasemalle = False
liikkuYlhaalle = False
liikkuAlhaalle = False

naytto = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Piirtäminen")


def piirraKuva(kuvatiedosto, x, y):
    naytto.blit(kuvatiedosto, (x, y))

def piirtaminen(naytto, hahmot, viholliset):
    for hahmo in hahmot:
        if hahmo[3] == True:
            kuva = pygame.image.load(hahmo[0]).convert()
            naytto.blit(kuva, (hahmo[1], hahmo[2]))
    for vihollinen in viholliset:
        if vihollinen[3] == True:
            kuva = pygame.image.load(vihollinen[0]).convert()
            naytto.blit(kuva, (vihollinen[1], vihollinen[2]))
    pygame.display.flip()

def rajaTarkastus(x, y, suunta):
    if (suunta == "v" and x < 10) or (suunta == "o" and x > 390) or (suunta == "y" and y < 10) or (suunta == "a" and y > 390):
        return False
    else:
        return True
    
def vihollinenTarkastus(hahmot, viholliset):
    for vihollinen in viholliset:
        for hahmo in hahmot:
            if vihollinen[1] - 100 < hahmo[1] < vihollinen[1] + 100 and vihollinen[2] - 100 < hahmo[2] < vihollinen[2] + 100:
                return True
    return False
                

def vihollisenLiikkuminen(viholliset):
    for vihollinen in viholliset:
        if vihollinen[1] >= 400:
            vihollinen[1] = 0
            vihollinen[2] = random.randint(0,400)
        else:
            vihollinen[1] += 0.2  

def kontrolli(hahmot, tapahtuma, viholliset):
    global liikkuOikealle,liikkuVasemalle,liikkuAlhaalle,liikkuYlhaalle
    paahahmo = hahmot[0]
    if tapahtuma.type == pygame.KEYDOWN:
        if tapahtuma.key == pygame.K_SPACE:
            for vihollinen in viholliset:
                vihollinen[3] = True
        elif tapahtuma.key == pygame.K_RIGHT:
            if rajaTarkastus(paahahmo[1], paahahmo[2], "o"):
                liikkuOikealle = True
            else:
                liikkuOikealle = True
        elif tapahtuma.key == pygame.K_LEFT:
            if rajaTarkastus(paahahmo[1], paahahmo[2], "v"):
                liikkuVasemalle = True
            else:
                liikkuVasemalle = False
        elif tapahtuma.key == pygame.K_DOWN:
            if rajaTarkastus(paahahmo[1], paahahmo[2], "a"):
                liikkuAlhaalle = True
            else:
                liikkuAlhaalle = False
        elif tapahtuma.key == pygame.K_UP:
            if rajaTarkastus(paahahmo[1], paahahmo[2], "y"):
                liikkuYlhaalle = True
            else:
                liikkuYlhaalle = False
    elif tapahtuma.type == pygame.KEYUP:
        if tapahtuma.key == pygame.K_RIGHT:
            liikkuOikealle = False
        elif tapahtuma.key == pygame.K_LEFT:
            liikkuVasemalle = False
        elif tapahtuma.key == pygame.K_DOWN:
            liikkuAlhaalle = False
        elif tapahtuma.key == pygame.K_UP:
            liikkuYlhaalle = False
    if liikkuOikealle == True:
        paahahmo[1] += 0.25
    if liikkuVasemalle == True:
        paahahmo[1] -= 0.25
    if liikkuAlhaalle == True:
        paahahmo[2] += 0.25
    if liikkuYlhaalle == True:
        paahahmo[2] -= 0.25

def main():
    vihrea = ["vihrea.png", 100, 100, True]
    punainen = ["punainen.png", 200, random.randint(0,400), True]
    punainen2 = ["punainen.png",200, random.randint(0,400), True]
    hahmot = [vihrea]
    viholliset = [punainen, punainen2]
    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break
        kontrolli(hahmot, tapahtuma, viholliset)
        piirtaminen(naytto, hahmot, viholliset)
        if vihollinenTarkastus(hahmot, viholliset):
            naytto.fill((100, 100, 100))
        else:
            naytto.fill((0, 0, 0))
        vihollisenLiikkuminen(viholliset)

main()