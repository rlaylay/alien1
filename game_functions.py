import sys 
import pygame
def check_events(ship):
	#响应事件
	for event in pygame.event.get():
		if event.type ==pygame.QUIT:
			sys.exit()
		
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				ship.moving_right =True
			elif event.key ==pygame.K_LEFT:
				ship.moving_left = True
		
		elif event.type == pygame.KEYUP:
			if event.key ==pygame.K_RIGHT:
				ship.moving_right = False
			elif event.key == pygame.K_LEFT:
				ship.moving_left = False
				

def update_screen(ai_settings,screen,ship):
	"""更新屏幕上的图案，并切换到新屏幕"""
	
	screen.fill(ai_settings.bg_color)
	#保证飞船在上方
	ship.blitme()
    #让最近绘制的屏幕可见
	pygame.display.flip()