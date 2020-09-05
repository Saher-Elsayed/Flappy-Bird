import  pygame, sys, random
pygame.init()
screen=pygame.display.set_mode((576,1024))
##X_max is 576 and Y_max is 1024
clock=pygame.time.Clock()

width=30
height=30
x_pos=30
currentScore = 0
y_pos=200
bottom_width=336*2
bird_gravity=0.1
bird_velocity=0
pipe_x_pos=300
pipe_y_pos = 500
pipe_width=52*2

bg=pygame.image.load("background-day.png").convert()
bg=pygame.transform.scale2x(bg)

bottom_surface=pygame.image.load("base.png").convert()
bottom_surface=pygame.transform.scale2x(bottom_surface)
bottom_x_pos=0

pipe_surface=pygame.image.load("pipe-green.png").convert()
pipe_surface=pygame.transform.scale2x(pipe_surface)
pipe_surface_flipped=pygame.transform.flip(pipe_surface, False, True)
pipe_rect=pipe_surface.get_rect(center=((576//2),(1024//2)))

BirdSprite = mid_surface=pygame.image.load("bluebird-midflap.png").convert()
mid_surface=pygame.transform.scale2x(mid_surface)
bird_rect=mid_surface.get_rect(center=((576//2),(1024//2)))

# list of pregenerated pipes for user to jump through
list_of_pipe_dimensions = [random.randint(400,460) for i in range(1,1000)]

def Floor_merge():
    screen.blit(bottom_surface,(bottom_x_pos,850))
    screen.blit(bottom_surface,(bottom_x_pos-(bottom_width*-1),850))
  
def Bird():
    ##pygame.draw.rect(screen, (255,255,255), (x_pos,y_pos,width,height))
     screen.blit(mid_surface,(bird_rect))

#def Pipe():
    #screen.blit(pipe_surface_flipped,(300,-500))
    #screen.blit(pipe_surface,(300,500))
    #pipes=[]
    #PIPESPAWNER=pygame.USEREVENT ##event that works with no triggers
    #pygame.time.set_timer(PIPESPAWNER,1000)
def Pipe_merge():
    screen.blit(pipe_surface,(pipe_x_pos,pipe_y_pos))
    screen.blit(pipe_surface_flipped,(pipe_x_pos,pipe_y_pos * -1))
    
    
def Create_a_pipe():
    return pipe_rect
    

def background():
    screen.blit(bg,(0,0))


if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
        ##looking for events like moving mouse
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ##print("flap") ## for debugging 
                    ##print(bird_rect.top)##for debugging
                    bird_velocity=-5

        bird_velocity+=bird_gravity
        bird_rect.centery+=round(bird_velocity)
        if bird_rect.top < 0:
            bird_rect.top = 0
        if bird_rect.bottom > 850:  # try not to have value hardcoded
            bird_rect.bottom = 850
        
        background()
        Bird()
        #Pipe()
        Floor_merge()
        Pipe_merge()
        #if event.type == PIPESPAWNER:
        #   pipes.append(Create_a_pipe())
        #   print (pipes)
        bottom_x_pos-=1
        pipe_x_pos-=3
        if bottom_x_pos <= (bottom_width *-1):
            bottom_x_pos=0
      
        if pipe_x_pos <=-100: 
            newYPosition = random.choice(list_of_pipe_dimensions)
            pipe_x_pos = 600
            pipe_y_pos = newYPosition
            currentScore+=1
            print(f"Current Pipe Dimensions: {pipe_x_pos} x {newYPosition}")
            print(f"User's current score: {currentScore}")
        
        

        pygame.display.update()
        clock.tick(120)
       
