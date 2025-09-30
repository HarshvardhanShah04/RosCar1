import pygame
import math

pygame.init()

dimension = 500
radius = 64
centre = dimension /2
screen = pygame.display.set_mode((dimension, dimension))
pygame.display.set_caption('geek')
clock = pygame.time.Clock()
pygame.draw.circle(screen, (0,255,10), (centre, centre), 64, 2)
pygame.draw.circle(screen, (255,255,255), (centre, centre), 5, )

x_coord = centre
y_coord = centre 

x_value = x_coord/radius
y_value = y_coord/radius

left_pwm = 0
right_pwm = 0

loop = True
while loop:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    
    pygame.display.update()
    
    pos = pygame.mouse.get_pos()

    dx = pos[0] - centre
    dy = pos[1] - centre
    
    check_inside_circle = True if math.sqrt(dx*dx + dy*dy) < radius + 6 else False
    
    click = True if pygame.mouse.get_pressed()[0] and check_inside_circle else False
    if click:
        pygame.mouse.set_cursor(pygame.cursors.diamond)


        x_coord = min(radius, max(-radius, pos[0] - centre))
        y_coord = min(radius, max(-radius, centre - pos))

        x_value = x_coord/radius
        y_value = y_coord/radius

        diff_setter = max(-80, min(80, 80* x_coord/radius))
        forward = 200 * y_coord/radius

        left_pwm = forward + diff_setter 
        right_pwm = forward - diff_setter

        left_pwm = 5 * round(left_pwm/5) 
        right_pwm = 5 * round(right_pwm/5)

        if y_value < 0:
            holder = left_pwm
            left_pwm = right_pwm
            right_pwm = holder



    if click == False:
        pygame.mouse.set_cursor()
        if abs(left_pwm)>20 or abs(right_pwm)>20:
            left_pwm -= int(left_pwm/8)
            right_pwm -= int(right_pwm/8)

        else:
            left_pwm = 0
            right_pwm = 0

    print(f"Pos = {pos}")
    print(f"x_coord {x_coord}", f" y_coord {y_coord}")
    print(f"x_value {x_value}" + f" y_value {y_value}")
    print([left_pwm, right_pwm])
    print()
    clock.tick(5)

pygame.quit()


