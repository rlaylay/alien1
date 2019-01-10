
import sys
import pygame
from settings import Settings
from ship import Ship
#from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_states import GameStats
from button import Button
from scoreboard import Scoreboard
def run_game():
    #
    pygame.init()
    ai_settings = Settings()
	
    screen =  pygame.display.set_mode(
	(ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("LOL Finals")
    #创建Play按钮
    play_button = Button(ai_settings,screen,"Play")

    #创建一艘飞船
    ship=Ship(ai_settings,screen)
    #bg_color = (230,230,230)
    bullets = Group()
    aliens = Group()
    #川建一个外星人
    #alien = Alien(ai_settings,screen)
    gf.create_fleet(ai_settings,screen,ship,aliens)
    #开始游戏主循环
    #创建一个用于存储游戏数据统计信息的实例,加记分牌
    stats =GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)


    while True:

        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)

        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)

run_game()
