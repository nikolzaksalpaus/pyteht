import pygame

naytto = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Piirtäminen")


def piirraKuva(kuvatiedosto, x, y):
    naytto.blit(kuvatiedosto, (x, y))

def piirtaminen(naytto, hahmot, viholliset):
    naytto.fill((0, 0, 0))
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
                del hahmot[0]

def vihollisenLiikkuminen(viholliset):
    for vihollinen in viholliset:
        if vihollinen[1] > 390:
            vihollinen[1] = 0
        else:
            vihollinen[1] += 0.5

def kontrolli(hahmot, tapahtuma, viholliset):
    paahahmo = hahmot[0]
    if tapahtuma.type == pygame.KEYDOWN:
        if tapahtuma.key == pygame.K_SPACE:
            for vihollinen in viholliset:
                vihollinen[3] = True
        elif tapahtuma.key == pygame.K_RIGHT:
            if rajaTarkastus(paahahmo[1], paahahmo[2], "o"):
                paahahmo[1] += 10
        elif tapahtuma.key == pygame.K_LEFT:
            if rajaTarkastus(paahahmo[1], paahahmo[2], "v"):
                paahahmo[1] -= 10
        elif tapahtuma.key == pygame.K_DOWN:
            if rajaTarkastus(paahahmo[1], paahahmo[2], "a"):
                paahahmo[2] += 10
        elif tapahtuma.key == pygame.K_UP:
            if rajaTarkastus(paahahmo[1], paahahmo[2], "y"):
                paahahmo[2] -= 10


def main():
    vihrea = ["vihrea.png", 100, 100, True]
    punainen = ["punainen.png", 200, 200, False]
    hahmot = [vihrea]
    viholliset = [punainen]
    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break
        kontrolli(hahmot, tapahtuma, viholliset)
        piirtaminen(naytto, hahmot, viholliset)
        vihollinenTarkastus(hahmot, viholliset)
        vihollisenLiikkuminen(viholliset)

main()