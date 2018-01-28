from . scene import *
from core.controller.menu_controller import *

class MainMenu(Scene):

	def __init__(self):
		super(MainMenu, self).__init__()
		self.__menu_controller = MenuController()
		self.add_controller(self.__menu_controller)
		self.set_camera(Camera())
	