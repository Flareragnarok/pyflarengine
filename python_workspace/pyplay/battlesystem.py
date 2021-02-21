import pygame
pygame.init()
pygame.font.init() 
myfont = pygame.font.SysFont('Comic Sans MS', 10)
hpsurface = myfont.render('HP', False, 0x000000)
tpsurface = myfont.render('TP', False, 0x000000)
statElements = {}
cancel = pygame.K_s
confirm = pygame.K_a

#global variables
screenH = 500
screenW = 800
uiH = 500
uiW = 150
healthbarW = 100
healthbarH = 10

keys = pygame.key.get_pressed()
win = pygame.display.set_mode((screenW,screenH))
clock = pygame.time.Clock()
playerui = pygame.Surface((uiW, uiH))
enemyui = pygame.Surface((uiW, uiH))
selectionui = pygame.Surface((screenW, screenH))

battleElements = {0 : "players", 1: "Enemies"}
players = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0}
enemies = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0}


def modifyPlayergroup(n,aid,attack,defense,agility,maxhp,currHp,maxTp, currTp):
    players[n] = participant(aid,attack,defense,agility,maxhp,currHp,maxTp, currTp)
    


class participant:
    def __init__(self,aid,attack,defense,agility,maxhp,currHp,maxTp, currTp):
        self.aid = aid
        self.attack = attack
        self.defense = defense
        self.agility = agility
        self.maxhp = maxhp
        self.currHp = currHp
        self.maxTp = maxTp
        self.currTp = currTp

        

    def iterator(self):
        p = 0
        for item in vars(self):
            statElements[p] = myfont.render(item + " = " + str(vars(self)[item]), False, 0x000000)
            p+=1
    



    def showstats(self):
        self.iterator()
        selectionui.fill(0x505050)
        selectionui.set_alpha(80)
        d = 1
        for i in statElements:
            selectionui.blit(statElements.get(i),(200,(d*20)))
            d=d+1
            

        win.blit(selectionui, (0,0))
        
        pygame.display.update()

        selection = True
        
        while (selection):
            pygame.time.wait(50)
            
            selection = (not pygame.key.get_pressed()[cancel])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    selection = False
                    run = False



player = participant(1,10,10,10,100,85,100,0)
enemy = participant(1,10,10,10,100,85,100,0)




#UI elements
class battlescreen:
    def __init__(self, surfaceplayer, surfaceenemy):
        self.surfaceenemy = surfaceenemy
        self.surfaceplayer = surfaceplayer

    def playerS(self, participant):
        hpbar = pygame.draw.rect(self.surfaceplayer, 0x00EE00, (self.surfaceplayer.get_rect().x, self.surfaceplayer.get_rect().y, healthbarW, healthbarH))
        hpred = pygame.draw.rect(self.surfaceplayer, 0xFF0000, (self.surfaceplayer.get_rect().x + healthbarW*(participant.currHp/participant.maxhp), self.surfaceplayer.get_rect().y, healthbarW*(abs(1-(participant.currHp/participant.maxhp))), healthbarH))
        tpbar = pygame.draw.rect(self.surfaceplayer, 0x00EEFF, (self.surfaceplayer.get_rect().x, self.surfaceplayer.get_rect().y+healthbarH, healthbarW, healthbarH))
        win.blit(hpsurface,(screenW-uiW,-3))
        win.blit(tpsurface,(screenW-uiW,8))

    def enemyS(self, participant):            
        hpbar = pygame.draw.rect(self.surfaceenemy, 0x00EE00, (self.surfaceenemy.get_rect().x, self.surfaceenemy.get_rect().y, healthbarW, healthbarH))
        hpred = pygame.draw.rect(self.surfaceenemy, 0xFF0000, (self.surfaceenemy.get_rect().x + healthbarW*(participant.currHp/participant.maxhp), self.surfaceenemy.get_rect().y, healthbarW*(abs(1-(participant.currHp/participant.maxhp))), healthbarH))
        tpbar = pygame.draw.rect(self.surfaceenemy, 0x00EEFF, (self.surfaceenemy.get_rect().x, self.surfaceenemy.get_rect().y+healthbarH, healthbarW, healthbarH))
        win.blit(hpsurface,(0,-3))
        win.blit(tpsurface,(0,8))



bs = battlescreen(playerui,enemyui)


def drawGW():
    win.fill(0xAAAAAA)
    win.blit(playerui, (screenW-uiW,0))
    win.blit(enemyui, (0,0))
    playerui.fill(0x220044)
    enemyui.fill(0x440022)
    bs.playerS(player)
    bs.enemyS(enemy)
    pygame.display.update()

def drawSelection():
    e = 1


run = True
while run:
    clock.tick(27)
    pygame.time.delay(27)
    pygame.time.wait(27)
   

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    drawGW()

    if pygame.key.get_pressed()[confirm]:
        player.showstats()

