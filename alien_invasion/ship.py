import pygame

class Ship:
    """우주선을 관리하는 클래스"""

    def __init__(self, ai_game):
        """우주선을 초기화하고 시작 위치를 설정합니다."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 우주선 이미지를 불러오고 사각형을 가져옵니다.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 우주선 초기 위치는 화면 하단 중앙입니다.
        self.rect.midbottom = self.screen_rect.midbottom
        # 움직음 플래그는 정지 상태로 시작합나다.
        self.moving_right = False

    def update(self):
        """움직임 플래그를 바탕으로 우주선 위치를 업데이트합니다."""
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        """우주선을 현재 위치에 그립니다."""
        self.screen.blit(self.image, self.rect)
