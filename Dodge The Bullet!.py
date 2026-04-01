import pygame as py

py.init()

window_height = 600
window_width = 800
window_size = (window_width, window_height)
screen = py.display.set_mode(window_size)
font = py.font.SysFont("Arial", 20)
circlesize = 46
circlex = 100
circley = 100
circlecolor = (0, 0, 255)
circlespeed = 0.5
square_color = (0, 255, 0) #Should be Red
squaresize = 25
squarex = 399 - (squaresize/2)
squarey = 299 - (squaresize/2)
squarespeed = 0.5
mu = False
md = False
mr = False
ml = False
Circle_mu = False
Circle_md = True
Circle_ml = False 
Circle_mr = True
py.display.set_caption("Dodge The Bullet!")

running = True
while True:
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
            elif event.type == py.KEYDOWN:
                if event.key == py.K_w:
                    mu = True
                elif event.key == py.K_s:
                    md = True
                elif event.key == py.K_a:
                    ml = True
                elif event.key == py.K_d:
                    mr = True
            elif event.type == py.KEYUP:
                if event.key == py.K_w:
                    mu = False
                elif event.key == py.K_s:
                    md = False
                elif event.key == py.K_d:
                    mr = False
                elif event.key == py.K_a:
                    ml = False
        if mu == True and squarey > 0:
            squarey -= squarespeed
        elif md == True and squarey < window_height - squaresize:
            squarey += squarespeed
        elif mr == True and squarex < window_width - squaresize:
            squarex += squarespeed
        elif ml == True and squarex > 0:
            squarex -= squarespeed
    
        if Circle_md == True:
            circley += circlespeed
        if Circle_mu == True:
            circley -= circlespeed
        if Circle_ml == True:
            circlex -= circlespeed
        if Circle_mr == True:
            circlex = circlex + circlespeed    
    
        if circlex >= window_width - circlesize:
            Circle_mr = False
            Circle_ml = True
        elif circlex <= 0:
            Circle_ml = False
            Circle_mr = True
        elif circley >= window_height - circlesize:
            Circle_md = False
            Circle_mu = True
        elif circley <= 0:
            Circle_mu = False
            Circle_md = True
    
        if squarex >= circlex - circlesize and squarex <= circlex + circlesize and squarey >= circley - circlesize and squarey <= circley + circlesize:
            break
        CircleText = f"cx:{circlex}, cy:{circley}"
        text = f"x:{squarex} y:{squarey}"                   
        GameOverText = "You Lost! Try Again."
        screen.fill((0, 0, 0))
        py.draw.circle(screen, circlecolor, (circlex, circley), circlesize)
        py.draw.rect(screen, square_color, (squarex, squarey, squaresize, squaresize))
        screen.blit(font.render(text, True, (255, 255, 255)), (1, 1))
        screen.blit(font.render(CircleText, True, (255, 255, 255)), (650, 1))
        py.display.flip()

    squarex = -1222
    squarey = -1222
    circlex = -1222
    circley = -1222
    py.draw.circle(screen, circlecolor, (circlex, circley), circlesize)
    py.draw.rect(screen, square_color, (squarex, squarey, squaresize, squaresize))
    screen.fill((0, 0, 0))
    screen.blit(font.render(GameOverText, True, (255, 0, 0)), (1, 1))
    py.display.flip()
    py.time.wait(1250)
    break
py.quit()