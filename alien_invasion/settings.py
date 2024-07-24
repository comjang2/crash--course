class Settings:
    """외계인 침공의 설정을 저장하는 클래스"""

    def __init__(self):
        """게임 설정 초기화"""
        # 화면 설정
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 우주선 설정
        self.ship_speed = 1.5