import pygame
import random

liikkuOikealle = False
liikkuVasemalle = False
liikkuYlhaalle = False
liikkuAlhaalle = False

running = False

parasTulos = 0

time = 50

clock = pygame.time.Clock()

naytto = pygame.display.set_mode((700, 600))
pygame.display.set_caption("Piirtäminen")

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)


def piirraKuva(kuvatiedosto, x, y):
    naytto.blit(kuvatiedosto, (x, y))

def piirtaminen(naytto, hahmot, viholliset):
    clock.tick(60)
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
    if (suunta == "v" and x < 10) or (suunta == "o" and x > 590) or (suunta == "y" and y < 10) or (suunta == "a" and y > 500):
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
    global time
    if running:
        for vihollinen in viholliset:
            if vihollinen[1] >= 700:
                vihollinen[1] = -100
                vihollinen[2] = random.randint(0,500)
            else:
                vihollinen[1] += 4*time*0.01

def aloittaaUudestaan():
    global i, running, time
    running = True
    i = 0
    time = 50
    

def kontrolli(hahmot, tapahtuma, viholliset):
    global liikkuOikealle,liikkuVasemalle,liikkuAlhaalle,liikkuYlhaalle,running,time
    paahahmo = hahmot[0]
    if tapahtuma.type == pygame.KEYDOWN:
        if tapahtuma.key == pygame.K_SPACE and not running:
            aloittaaUudestaan()
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
            paahahmo[1] += 6*time*0.01
    if liikkuVasemalle == True:
        if rajaTarkastus(paahahmo[1], paahahmo[2], "v"):
            paahahmo[1] -= 6*time*0.01
    if liikkuAlhaalle == True:
        if rajaTarkastus(paahahmo[1], paahahmo[2], "a"):
            paahahmo[2] += 6*time*0.01
    if liikkuYlhaalle == True:
        if rajaTarkastus(paahahmo[1], paahahmo[2], "y"):
            paahahmo[2] -= 6*time*0.01

def main():
    global i, running, parasTulos, time
    vihrea = ["vihrea.png", 100, 100, True]
    punainen = ["punainen.png", 200, random.randint(0,500), True]
    punainen2 = ["punainen.png",200, random.randint(0,500), True]
    hahmot = [vihrea]
    viholliset = [punainen, punainen2]
    i = 0
    while True:
        if i > parasTulos:
            parasTulos = i
        
        if running:
            time += 0.1
            i += .01 * abs(hahmot[0][1] - 650) / 10
            text_surface3 = my_font.render("", True, (255, 255, 255))
            vihrea[3] = True
            punainen[3] = True
            punainen2[3] = True
        else:
            text_surface3 = my_font.render("Paina välilyöntiä", True, (255, 255, 255))
            vihrea[3] = False
            punainen[3] = False
            punainen2[3] = False
        
        text_surface2 = my_font.render("Paras tulos: "+str(int(parasTulos)), True, (255, 255, 255))
        text_surface = my_font.render("Tulos: "+str(int(i)), True, (255, 255, 255))
       
        naytto.blit(text_surface, (0,0))
        naytto.blit(text_surface2, (0,40))
        naytto.blit(text_surface3, (0,80))
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break
        kontrolli(hahmot, tapahtuma, viholliset)
        piirtaminen(naytto, hahmot, viholliset)
        if vihollinenTarkastus(hahmot, viholliset):
            running = False
            vihrea = ["vihrea.png", 200, 200, False]
            punainen = ["punainen.png", -100, random.randint(0,500), False]
            punainen2 = ["punainen.png", -100, random.randint(0,500), False]
            hahmot = [vihrea]
            viholliset = [punainen, punainen2]
        else:
            naytto.fill((0, 0, 0))
        vihollisenLiikkuminen(viholliset)

main()
