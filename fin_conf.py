import numpy as np
import math
import matplotlib as mpl

import settings



# 0: Not fin, 1: Fin, 2: Base(Constant Temp)
Conf_matrix = np.zeros((settings.CXN,settings.CYN))

class IO_Manager:
	def __init__(self):
		self.pressed = False
		self.X_NODE = 0
		self.Y_NODE = 0

		self.START_NODE = (0,0)
		self.END_NODE = (0,0)

	def onClick(self, event):
		self.pressed = True
		if (event.xdata == None or event.ydata == None):
			return
		X_NODE = math.floor(settings.CXN * (event.xdata / settings.CANVAS_SIZE_X))
		Y_NODE = math.floor(settings.CYN * (event.ydata / settings.CANVAS_SIZE_Y))
		self.X_NODE = X_NODE
		self.Y_NODE = Y_NODE
		print('clicking %d %d' % (X_NODE, Y_NODE))

	def onRelease(self, event):
		self.pressed = False

	def onMotion(self, event):
		if (not self.pressed):
			return
		if (event.xdata == None or event.ydata == None):
			return
		X_NODE = math.floor(settings.CXN * (event.xdata / settings.CANVAS_SIZE_X))
		Y_NODE = math.floor(settings.CYN * (event.ydata / settings.CANVAS_SIZE_Y))
		self.X_NODE = X_NODE
		self.Y_NODE = Y_NODE
		print('dragging %d %d' % (X_NODE, Y_NODE))

	def onKeyPress(self, event):
		print('%s pressed!' % event.key)

	def connect(self, fig):
		mpl.rcParams['keymap.fullscreen'].remove('f')
		mpl.rcParams['keymap.save'].remove('s')
		mpl.rcParams['keymap.quit'].remove('q')

		self.fig = fig
		self.cid1 = fig.canvas.mpl_connect('button_press_event', self.onClick)
		self.cid2 = fig.canvas.mpl_connect('key_press_event', self.onKeyPress)
		self.cid3 = fig.canvas.mpl_connect('button_release_event', self.onRelease)
		self.cid4 = fig.canvas.mpl_connect('motion_notify_event', self.onMotion)

	def disconnect(self, fig):
		self.fig.canvas.mpl_disconnect(self.cid1)
		self.fig.canvas.mpl_disconnect(self.cid2)
		self.fig.canvas.mpl_disconnect(self.cid3)
		self.fig.canvas.mpl_disconnect(self.cid4)


