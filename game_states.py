class GameStats():
    """跟踪游戏的统计数据"""

    def __init__(self,ai_settings):
        """初始化统计数据"""
        #在任何情况下都不应该重置最高分数
        self.high_score = 0
        self.ai_settings = ai_settings
        self.reset_stats()
    #游戏刚启动时处于活动状态
        self.game_active = True


    def reset_stats(self):
        """初始化游戏运行期间可能变化的游戏数据"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

