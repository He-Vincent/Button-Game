# goal of game: 4 white square change to red and then they change back to white then user must press in that order
#sequence is 4 moves, start with same, then import random to do random 4 move sequence, 
#user has 5 seconds to click that same sequence
import pygame
import random
import time


	#assign each square a number 1-4 and if their number called, it changes to red

pygame.init()

win_colour = (50,50,50)
win_size = (500,500)	

button = [(int(win_size[0]/2)),(int(win_size[1]/2))]

button_size = [150,150]

button_space = 5

#above the 1st button, same x axis as 1st button 

button2 = [button[0],button[1] - button_size[1] - button_space]

# to the left of button 2, so same y axis
button3 = [button2[0]-button_size[0]-button_space,button2[1]]

#under the button3, so same x axis

button4 = [button3[0],button3[1] + button_size[1] + button_space]


win = pygame.display.set_mode((500,500))
pygame.display.set_caption("SQUARES")

clock = pygame.time.Clock()


middle_x = int(win_size[0]/2)

middle_y = int(win_size[1]/2)

#create 2x2 grid 

bcolor = (255,255,255)

b2color = (255,255,255)

b3color = (255,255,255)

b4color = (255,255,255)

red = (255,0,0)

white = (255,255,255)

user_moves = []

moves = []

font_name = pygame.font.match_font('impact')

fontsize = 69

middle_x = int(win_size[0]/2)

middle_y = int(win_size[1]/2)

usermovesnum = 0

wins = 0


def draw():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:	
			pygame.quit()
	win.fill(win_colour)
	pygame.draw.rect(win,bcolor,(button,button_size))
	pygame.draw.rect(win,b2color,(button2,button_size))
	pygame.draw.rect(win,b3color,(button3,button_size))
	pygame.draw.rect(win,b4color,(button4,button_size))
	pygame.display.update()

def midtop_text(surf, text, size, x, y, colour):
	font = pygame.font.Font(font_name, size)
	text_surface = font.render(text, True, (colour))
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surf.blit(text_surface, text_rect)

#every 2 seconds button color changes from white to red then user must press the button  within 2 seconds
#if successful display message or else print nub

cycle = True

user_cycle = True

pause_time = 0.75

click = False
          
while True:

	#user_moves not storing ints wtf

	draw()

	#for event in pygame.event.get():
		#mouseX, mouseY = pygame.mouse.get_pos()

		#if event.type == pygame.QUIT:	
			#pygame.quit()
			
	#for i in range(4):
		#moves.append(random.randint(1,4))

     #computer moves
		
		#make so that one button from white to red, pause then back to white, ONE AFTER ANOTHER
		#why still go after 4 moves????
		#keeps running same sequence 
		#stop after 4 moves
	if cycle:
		sequencenum = wins + 4
		usermovesnum = 0
		user_moves = []
		moves = []
		for i in range(sequencenum):
			moves.append(random.randint(1,4))
			if moves[i] == 1:
				time.sleep(pause_time)
				bcolor = red
				draw()
				time.sleep(pause_time)
				bcolor = white
				draw()
			elif moves[i] == 2:
				time.sleep(pause_time)
				b2color = red
				draw()
				time.sleep(pause_time)
				b2color = white
				draw()
			elif moves[i] == 3:
				time.sleep(pause_time)
				b3color = red
				draw()
				time.sleep(pause_time)
				b3color = white
				draw()
			elif moves[i] == 4:
				time.sleep(pause_time)
				b4color = red
				draw()
				time.sleep(pause_time)
				b4color = white
				draw()
		target_time = time.time() + 5 + 1.25 * wins
	cycle = False

	if time.time() >= target_time:
		midtop_text(win, "fail", fontsize, middle_x, middle_y, (255,0,0))
		pygame.display.update()
		time.sleep(2)
		cycle = True
		wins = 0
		
			#user moves, if user does all 4 correctly, at the end display "success"
			#if not, at the end of user's 4 moves, display "nope"
			#give user 5 sec to do moves
		
	for event in pygame.event.get():

		mouseX, mouseY = pygame.mouse.get_pos()



		if event.type == pygame.QUIT:	
			pygame.quit()

		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				click = True


	if click:
 #how to change so that after 4 user moves, instead of exiting program, it checks the users moves against computer moves
 #how to give user 5 seconds to press the same sequence of moves as computer
		
		#button 1
		
		if event.type == pygame.MOUSEBUTTONDOWN and mouseX >= button[0] and mouseX <= button[0] + button_size[0] and mouseY >= button[1] and mouseY <= button[1] + button_size[1]:
			bcolor = red
			draw()
			time.sleep(pause_time)
			bcolor = white
			draw()
			user_moves.append(1)
			usermovesnum += 1
				#button 2
		if event.type == pygame.MOUSEBUTTONDOWN and mouseX >= button2[0] and mouseX <= button2[0] + button_size[0] and mouseY >= button2[1] and mouseY <= button2[1] + button_size[1]:
			b2color = red
			draw()
			time.sleep(pause_time)
			b2color = white
			draw()
			user_moves.append(2)
			usermovesnum += 1
			#button 3
		if event.type == pygame.MOUSEBUTTONDOWN and mouseX >= button3[0] and mouseX <= button3[0] + button_size[0] and mouseY >= button3[1] and mouseY <= button3[1] + button_size[1]:
			b3color = red
			draw()
			time.sleep(pause_time)
			b3color = white
			draw()
			user_moves.append(3)
			usermovesnum += 1
				#button 4
		if event.type == pygame.MOUSEBUTTONDOWN and mouseX >= button4[0] and mouseX <= button4[0] + button_size[0] and mouseY >= button4[1] and mouseY <= button4[1] + button_size[1]:
			b4color = red
			draw()
			time.sleep(pause_time)
			b4color = white
			draw()
			user_moves.append(4)
			usermovesnum += 1

		if usermovesnum == sequencenum:
			if moves == user_moves and time.time() <= target_time:
				midtop_text(win, "success", fontsize, middle_x, middle_y, (0,255,0))
				pygame.display.update()
				time.sleep(2)
				cycle = True
				wins += 1
						#if time runs out and user is idle then lose	
			else:
				midtop_text(win, "fail", fontsize, middle_x, middle_y, (255,0,0))
				pygame.display.update()
				time.sleep(2)
				cycle = True
				wins = 0
		
			# computer 4 moves then user 4 moves, then after, upon click, all buttons remain white
	click = False