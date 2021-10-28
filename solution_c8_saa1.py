import pygame,math,random

pygame.init()
screen = pygame.display.set_mode((400,600))

pygame.display.set_caption("Shooting Spaceship")
background_image = pygame.image.load("bg2.jpg").convert()
player_image = pygame.image.load("s4.png").convert_alpha()
enemy_image = pygame.image.load("e3.png").convert_alpha()
player=pygame.Rect(200,200,30,30)

angle=0
change=0
distance=5
forward=False

xvel=[]
yvel=[]
enemies=[]
enemycount=10


score=0
over=False

score_font=pygame.font.Font('freesansbold.ttf', 15)
gameover_font=pygame.font.Font('freesansbold.ttf', 30)



bullet=pygame.Rect(200,200,5,5)
bulletState="ready"
YELLOW=(255,255,0)

# Creating GREEN color using RGB combinations and naming it 'GREEN'
GREEN=(0,255,0)

for i in range(enemycount): 
  enemies.append(pygame.Rect(random.randint(0,400),random.randint(0,600),20,20))
  xvel.append(random.randint(-3,3))
  yvel.append(random.randint(-3,3))

def newxy(x,y,distance,angle):
  angle=math.radians(angle+90)
  xnew=x+(distance*math.cos(angle))
  ynew=y-(distance*math.sin(angle))
  return xnew,ynew

while True:
  screen.blit(background_image,[0,0])
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      
    if event.type == pygame.KEYDOWN:
       if event.key == pygame.K_LEFT:
          change = 6
       if event.key ==pygame.K_RIGHT:
        change = -6 
       if event.key == pygame.K_UP:
        forward = True
       if event.key == pygame.K_SPACE and bulletState=="ready":
           bulletState="fired"
           bangle=angle
        
    if event.type == pygame.KEYUP:
      if event.key ==pygame.K_LEFT or event.key == pygame.K_RIGHT:
          change = 0
      if event.key == pygame.K_UP:
        forward = False 
  i=0    
  for enemy in enemies:
      enemy.x=enemy.x + xvel[i]
      enemy.y=enemy.y + yvel[i]
  
  
      if enemy.x < -250 or enemy.x > 650 :
        xvel[i] = -1*xvel[i]
      
      if enemy.y < -250 or enemy.y > 850:  
        yvel[i] = -1*yvel[i]
      
      if bullet.colliderect(enemy):
          enemy.x=random.choice([random.randint(-250,0),random.randint(400,650)])   
          enemy.y=random.choice([random.randint(-250,0),random.randint(600,850)])  
          # Increment the value of 'score' by 5
          score=score+5
          
     
      if enemy.colliderect(player):
          over=True
          player_image=enemy_image
          
      screen.blit(enemy_image,enemy)  
      i=i+1
  
  if bulletState=="ready":
    bullet.x = player.x+20
    bullet.y = player.y+20
  
  if bulletState=="fired":
      bullet.x ,bullet.y = newxy(bullet.x, bullet.y, 20 , bangle)    
  
  if bullet.y<0 or bullet.x<0 or bullet.y>600 or bullet.x>400:
      bulletState="ready"
      
      
  pygame.draw.rect(screen,YELLOW,bullet)  
  
  if forward:
      player.x,player.y=newxy(player.x, player.y, distance, angle)  
  if player.x<0:
      player.x=400
  if player.x>400:
      player.x=0
  if player.y<0:
      player.y=600
  if player.y>600:
      player.y=0
  
  if over:
      gameover_text=gameover_font.render("GAME OVER!",True,YELLOW)
      screen.blit(gameover_text,(100,250))    
  
  angle = angle + change
  newimage=pygame.transform.rotate(player_image,angle) 
  screen.blit(newimage ,player)
  
  # Create the text to be displayed using 'score_font' and name it 'score_text'
  # Text to be displayed, "True", color are passed as arguments
  score_text=score_font.render("Score : " + str(score),True,GREEN)
  
  # Display the 'score_text' at the location (10,10)
  screen.blit(score_text,(10,10))
 

  pygame.display.update()
  pygame.time.Clock().tick(30)
  
  
