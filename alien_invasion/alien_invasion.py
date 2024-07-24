import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """게임 자원과 동작을 전체적으로 관리하는 클래스"""

    def __init__(self):
        """게임을 초기화하고 게임 자원을 만듭니다."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """게임의 메인 루프를 시작합니다."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
            # 키보드와 마우스 이벤트에 응답합니다.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """키를 누를 때 응답합니다."""
        if event.key == pygame.K_RIGHT:
             self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
             self.ship.moving_left = True

    def _check_keyup(self, event):
        """키에서 손을 뗄 때 응답합니다."""
        if event.key == pygame.K_RIGHT:
             self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
             self.ship.moving_left = False

    def _update_screen(self):
            """화면의 이미지를 업데이트하고 화면을 새로 그립니다."""
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()

