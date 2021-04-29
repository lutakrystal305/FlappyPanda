import pygame
import numpy as np
pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Flappy panda')
font1 = pygame.font.SysFont('san', 50)
font2 = pygame.font.SysFont('san', 20)
bg_x = 0
bg_y = 0
panda_x = 300
panda_y = 30
tree_x1 = 800
tree_x2 = -800
tree_y1 = 400
tree_y2 = -100
tree_y3 = 400
tree_y4 = -100
drop_velocity = 0
gravity = 0.25
bg = pygame.image.load('./img/bamboo.png')
panda = pygame.image.load("./img/koala1.png")
panda = pygame.transform.scale(panda, (50, 50))
tree = pygame.image.load('./img/tree1.png')
tree = pygame.transform.scale(tree, (500, 450))
shit = pygame.image.load('./img/poo.png')
x_velocity = 1.5
shit_x = -1000
shit_y = 0
clock = pygame.time.Clock()
score = 0
jump  = False
check = False
PAUSE = False
RUN = True
while RUN:
    clock.tick(100)
    #screen.fill((255, 255, 255))
    bg1_rect = screen.blit(bg, (bg_x, bg_y))
    bg2_rect = screen.blit(bg, (bg_x + 1000, bg_y))
    panda_rect = screen.blit(panda, (panda_x, panda_y))
    tree1_rect = screen.blit(tree, (tree_x1, tree_y1))
    tree2_rect = screen.blit(tree, (tree_x1, tree_y2))
    tree3_rect = screen.blit(tree, (tree_x2, tree_y3))
    tree4_rect = screen.blit(tree, (tree_x2, tree_y4))
    shit_rect = screen.blit(shit, (shit_x, shit_y))
    score_txt = font2.render("Score: " + str(score), True, (60, 147, 255))
    screen.blit(score_txt, (30, 30))
    tree_x1 -= x_velocity
    tree_x2 -= x_velocity
    if (tree1_rect and tree_x1 > 0) :
        
        if (200 < tree_x1 <= 201.5) :
            tree_x2 = 800
            tree_y3 = np.random.randint(300, 500)
            tree_y4 = tree_y3 - 500
    if (tree3_rect and tree_x2 > 0) :
    
        if (200 < tree_x2 <= 201.5) :
            tree_x1 = 800
            tree_y1 = np.random.randint(300, 500)
            tree_y2 = tree_y1 - 500
    if (bg_x + 1000 <= 0):
        bg_x = 0
    if (100 < tree_x1 <= 102.5):
        if (PAUSE == False):
            score += 1
        else :
            score -= 1
    if (100 < tree_x2 <= 102.5):
        if (PAUSE == False):
            score += 1
        else :
            score -= 1
    bg_x -= x_velocity
    #fall
    panda_y += drop_velocity
    drop_velocity += gravity
    if (panda_y >= 600):
        PAUSE = True
    if (score >= 10 and shit_x <= 0) :
        shit_x = 800
        shit_y = np.random.randint(200, 500)
    shit_x -= 5
    if (tree_x1 + 120 < panda_x < tree_x1 + 240
        and tree_y1 - 45 <= panda_y <= tree_y1+300
    ):
        PAUSE = True
        check = True
    if (tree_x2 + 120 < panda_x < tree_x2 + 240
        and tree_y3 - 45 <= panda_y <= tree_y3+300
    ):
        PAUSE = True
        check = True
    if ((tree_x1 +120 <= panda_x <= tree_x1 + 240)
        and (tree_y2 <= panda_y <= tree_y2+310)
    ):
        PAUSE = True
    if ((tree_x2 +120 <= panda_x <= tree_x2 + 240)
        and (tree_y4 <= panda_y <= tree_y4+310)
    ):
        PAUSE = True
    if  shit_x <= panda_x <= shit_x + 40 and shit_y <= panda_y <= shit_y + 40:
        PAUSE = True
    '''
    a = [tree1_rect, tree2_rect, tree3_rect, tree4_rect]
    for b in a:
        if panda_rect.colliderect(b):
            print(b)
            x_velocity = 0
            drop_velocity = 0
            PAUSE = True
    '''
    if PAUSE == True:
        x_velocity = 0
        if (check) :
            drop_velocity = 0
        gameover_txt = font1.render("GAME OVER", True, (0, 255, 0))
        screen.blit(gameover_txt, (400, 250))
        txt = font2.render("'SPACE' to restart!!", True, (0, 255, 0))
        screen.blit(txt, (400, 300)) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        if (PAUSE == False) :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    drop_velocity = 0
                    drop_velocity -= 7
        else :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    PAUSE = False
                    x_velocity = 1.5
                    bg_x = 0
                    bg_y = 0
                    panda_x = 300
                    panda_y = 30
                    tree_x1 = 800
                    tree_x2 = -800
                    tree_y1 = 400
                    tree_y2 = -100
                    score = 0
                    check = False
                    drop_velocity = 0
                    gravity = 0.25
    pygame.display.flip()
pygame.quit()