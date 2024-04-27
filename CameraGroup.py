import pygame

class CameraGroup(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.display_surface = pygame.display.get_surface()

		# camera offset 
		self.offset = pygame.math.Vector2()
		self.half_w = self.display_surface.get_size()[0] // 2
		self.half_h = self.display_surface.get_size()[1] // 2

		# ground
		self.ground_surf1 = pygame.image.load('graphics/bg01.png').convert_alpha()
		self.ground_rect1 = self.ground_surf1.get_rect(topleft = (0,0))
		self.ground_surf2 = pygame.image.load('graphics/bg02.png').convert_alpha()
		self.ground_rect2 = self.ground_surf2.get_rect(topleft = (0,0))
		self.ground_surf3 = pygame.image.load('graphics/bg03.png').convert_alpha()
		self.ground_rect3 = self.ground_surf3.get_rect(topleft = (0,0))

	def center_target_camera(self, target):
		self.offset.x = target.rect.centerx - self.half_w
		self.offset.y = target.rect.centery - self.half_h

	def custom_draw(self,player):

		self.center_target_camera(player)

		# ground 
		top_offset = -850
		d = player.rect.centerx % 100
		ground_offset = self.ground_rect1.topleft - self.offset
		for x in range(-10000 + d // 4, 10000, 100):
			self.display_surface.blit(self.ground_surf1, ground_offset + pygame.math.Vector2(x, top_offset))

		ground_offset = self.ground_rect2.topleft - self.offset
		for x in range(-10000 + d // 3, 10000, 100):
			self.display_surface.blit(self.ground_surf2, ground_offset + pygame.math.Vector2(x, top_offset))

		ground_offset = self.ground_rect3.topleft - self.offset
		for x in range(-10000 + d // 2, 10000, 100):
			self.display_surface.blit(self.ground_surf3, ground_offset + pygame.math.Vector2(x, top_offset))

		# active elements
		for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)