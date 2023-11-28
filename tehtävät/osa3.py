import pygame
import random

liikkuOikealle = False
liikkuVasemalle = False
liikkuYlhaalle = False
liikkuAlhaalle = False

naytto = pygame.display.set_mode((550, 500))
pygame.display.set_caption("Piirtäminen")
pygame.font.init()
pygame.font.init()

my_font = pygame.font.SysFont('Comic Sans MS', 30)


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
    if (suunta == "v" and x < 10) or (suunta == "o" and x > 440) or (suunta == "y" and y < 10) or (suunta == "a" and y > 400):
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
        if vihollinen[1] >= 450:
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
        if rajaTarkastus(paahahmo[1], paahahmo[2], "o"):
            paahahmo[1] += 0.28
    if liikkuVasemalle == True:
        if rajaTarkastus(paahahmo[1], paahahmo[2], "v"):
            paahahmo[1] -= 0.28
    if liikkuAlhaalle == True:
        if rajaTarkastus(paahahmo[1], paahahmo[2], "a"):
            paahahmo[2] += 0.28
    if liikkuYlhaalle == True:
        if rajaTarkastus(paahahmo[1], paahahmo[2], "y"):
            paahahmo[2] -= 0.28

def main():
    vihrea = ["vihrea.png", 100, 100, True]
    punainen = ["punainen.png", 200, random.randint(0,400), True]
    punainen2 = ["punainen.png",200, random.randint(0,400), True]
    hahmot = [vihrea]
    viholliset = [punainen, punainen2]
    i = 0
    while True:
        i += .01 * abs(hahmot[0][1] - 500) / 100
        text_surface = my_font.render(str(int(i)), False, (255, 255, 255))
        naytto.blit(text_surface, (0,0))
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break
        kontrolli(hahmot, tapahtuma, viholliset)
        piirtaminen(naytto, hahmot, viholliset)
        if vihollinenTarkastus(hahmot, viholliset):
            exit()
        else:
            naytto.fill((0, 0, 0))
        vihollisenLiikkuminen(viholliset)

main()
