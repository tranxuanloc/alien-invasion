class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 2

        # Bullet settings
        self.bullet_speed = 10.0
        self.bullet_width = 300
        self.bullet_heght = 10
        self.bullet_color = (60, 60, 60)

        # Alien settings
        self.alien_speed = 3.0
        self.fleet_drop_speed = 30
        # 1 represents right; -1 represents left
        self.fleet_direction = 1
