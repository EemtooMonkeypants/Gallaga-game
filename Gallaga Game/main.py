import pgzrun

WIDTH = 600
HEIGHT = 800
TITLE = 'Gallaga Game'

ship = Actor('galaga')
ship.x = 300
ship.y = 750
game = True
score = 0

bugs = []
for i in range(5):
    for j in range(5):
        bug = Actor('bug')
        bugs.append(bug)
        bug.x = 100 + i * 100
        bug.y = 100 + j * 50

bullets = []

def draw():
    global game
    screen.clear()
    if game:
        ship.draw()
        for bug in bugs:
            bug.draw()
        for bullet in bullets:
            bullet.draw()
    screen.draw.text('score = '+str(score),(50,50), fontsize = 30)
    if game == 'lost':
        screen.fill('black')
        screen.draw.text('You got eaten!',center=(WIDTH/2,HEIGHT/2),fontsize = 50)
        screen.draw.text('Press "r" to play again!', center=(WIDTH/2,HEIGHT/2-200),fontsize = 50)
    if len(bugs) == 0:
        game = False
        screen.draw.text('You win!',center=(WIDTH/2,HEIGHT/2),fontsize = 50)
        screen.draw.text('Press "r" to play again!', center=(WIDTH/2,HEIGHT/2-200),fontsize = 50)

def update():
    global game, score
    if keyboard.left:
        ship.x = ship.x - 10
    if keyboard.right:
        ship.x = ship.x + 10
    for bullet in bullets:
        bullet.y = bullet.y - 10
    for bug in bugs:
        bug.y = bug.y + 0.5
        for bullet in bullets:
            #for bug in bugs:
            if bullet.colliderect(bug):
                score +=1
                bugs.remove(bug)
                bullets.remove(bullet)
        if bug.colliderect(ship):
            game = 'lost'
            
def on_key_down(key):
    global bullets, game, bugs, score
    if key == keys.SPACE:
        bullet = Actor('bullet')
        bullet.x = ship.x
        bullet.y = ship.y
        bullets.append(bullet)
    if game == False or game == 'lost':
        if key == keys.R:
            game = True
            bugs = []
            bullets = []
            score = 0
            for i in range(5):
                for j in range(5):
                    bug = Actor('bug')
                    bugs.append(bug)
                    bug.x = 100 + i * 100
                    bug.y = 100 + j * 50



pgzrun.go()

