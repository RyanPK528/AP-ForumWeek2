# A class to store all settings for Alien Invasion.
class Settings():
   def __init__(self):
      # Initialize the game's settings.
      # Screen settings
      self.screen_width = 1200
      self.screen_height = 800
      self.bg_color = (15, 0, 54)

      # Ship settings
      self.ship_speed_factor = 0.8
      self.ship_limit = 2

      # Bullet settings
      self.bullet_speed_factor = 1
      self.bullet_width = 10
      self.bullet_height = 25
      self.bullet_color = 100, 20, 20
      self.bullets_allowed = 3

      # Alien settings
      self.alien_speed_factor = 1
      self.fleet_drop_speed = 10

      # fleet_direction of 1 represents right; -1 represents left.
      self.fleet_direction = 1

      # How quickly the game speeds up
      self.speedup_scale = 1.5
      self.initialize_dynamic_settings()

      # How quickly the alien point values increase
      self.score_scale = 1.5

   def initialize_dynamic_settings(self):
      # Initialize settings that change throughout the game.
      self.ship_speed_factor = 1.5
      self.bullet_speed_factor = 3
      self.alien_speed_factor = 1

      # fleet_direction of 1 represents right; -1 represents left.
      self.fleet_direction = 1

      # Scoring
      self.alien_points = 50

   def increase_speed(self):
      # Increase speed settings and alien point values.
      self.ship_speed_factor *= self.speedup_scale
      self.bullet_speed_factor *= self.speedup_scale
      self.alien_speed_factor *= self.speedup_scale
      self.alien_points = int(self.alien_points * self.score_scale)