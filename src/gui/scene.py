class Scene:

	def __init__(self):
		self.__camera = Camera()
		self.__controllers = []
		self.__entities = []

	def draw(self, screen):
		camera_rect = self.__camera.get_rect()
		for e in self.__entities:
			e_rect = e.get_rect()
			if camera_rect.collide(e_rect):
				e.draw(screen, camera_rect.left, camera_rect.top)
