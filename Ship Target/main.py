import pgzrun
import random
import itertools

WIDTH = 400
HEIGHT = 400

blockpos = [(350,50),(350,350),(50,350),(50,50)]
bpos = itertools.cycle(blockpos)
block = Actor('block',center=(50,50))
ship = Actor('ship',center=(200,200))

def draw():
    screen.clear()
    ship.draw()
    block.draw()
def move_block():
    animate(
        block, 
        'bounce_end',
        duration = 1,
        pos = next(bpos)

    )
move_block()
clock.schedule_interval(move_block,2)

def ship_target():
    x = random.randint(300,300)
    y = random.randint(300,300)
    ship.target = x,y
    target_angle = ship.angle_to(ship.target)

pgzrun.go()