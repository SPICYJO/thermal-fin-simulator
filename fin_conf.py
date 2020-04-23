import numpy as np
import math
import matplotlib as mpl
import matplotlib.pyplot as plt

import settings
import plot
import solve

x = np.linspace(0.0, settings.CANVAS_SIZE_X, settings.CXN)
y = np.linspace(0.0, settings.CANVAS_SIZE_Y, settings.CYN)

# 0: Not fin, 1: Fin, 2: Base(Constant Temp)
conf_matrix = np.zeros((settings.CYN,settings.CXN,), dtype=np.int32)

# Fin, Base constraint (for mechlab2)
conf_matrix[3:27, 100:150] = 1
conf_matrix[0:3, 100:150] = 2

def getFinNodeCount():
	unique, counts = np.unique(conf_matrix, return_counts=True)
	d = dict(zip(unique, counts))
	if 1 in d:
		return d[1]
	else:
		return 0

def setRect(start, end, mask, thickness=0):
	global conf_matrix
	old_one = conf_matrix.copy()

	conf_matrix[min(start[1],end[1])-thickness :max(start[1],end[1])+thickness, min(start[0],end[0])-thickness:max(start[0],end[0])+thickness] = mask
	
	# Fin, Base constraint (for mechlab2)
	conf_matrix[3:27, 100:150] = 1
	conf_matrix[0:2, 100:150] = 2

	num_fin_node = getFinNodeCount()
	print("Current number of Fin node : %d / %d" % (num_fin_node, settings.MAX_FIN_NODE))
	if (num_fin_node > settings.MAX_FIN_NODE):
		print("Reached MAX_FIN_NODE, Cannot draw!")
		conf_matrix = old_one
		return
	


class IO_Manager:
	def __init__(self):
		self.pressed = False
		self.X_NODE = 0
		self.Y_NODE = 0
		self.mask = 0

		self.linemode = 0
		self.thickness = 1

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
		self.START_NODE = (self.X_NODE,self.Y_NODE)

		#print('clicking %d %d' % (X_NODE, Y_NODE))

	def onRelease(self, event):
		self.pressed = False
		self.END_NODE = (self.X_NODE,self.Y_NODE)
		self.onDragCompletion()
		

	def onMotion(self, event):
		if (not self.pressed):
			return
		if (event.xdata == None or event.ydata == None):
			return
		X_NODE = math.floor(settings.CXN * (event.xdata / settings.CANVAS_SIZE_X))
		Y_NODE = math.floor(settings.CYN * (event.ydata / settings.CANVAS_SIZE_Y))
		self.X_NODE = X_NODE
		self.Y_NODE = Y_NODE
		if(self.linemode == 1):
			self.onLineModeCompletion()
		#print('dragging %d %d' % (X_NODE, Y_NODE))

	def onKeyPress(self, event):
		print('%s pressed!' % event.key)
		if (event.key == 'f'):
			print('Change into Fin mode')
			self.mask = 1
		if (event.key == 'a'):
			print('Change into Ambient mode')
			self.mask = 0
		if (event.key == 'b'):
			print('Change into Base mode')
			self.mask = 2
		if (event.key == 'r'):
			print('Change Draw mode into Rectangle')
			self.linemode = 0
		if (event.key == 'l'):
			print('Change Draw mode into Line')
			self.linemode = 1
		if (event.key == '+' and self.linemode == 1):
			self.thickness += 1
			print('Thickness : %d' % self.thickness)
		if (event.key == '-' and self.linemode == 1):
			self.thickness -= 1
			if(self.thickness < 1):
				self.thickness = 1
			print('Thickness : %d' % self.thickness)	
		if (event.key == 't'):
			print('Solve & Show (Transient)')
			solve.solve_transient()
			plot.showAnimation()
		if (event.key == 's'):
			print('Solve & Show (Steady-state)')
			solve.solve_steady()
			plot.showSteady()
		if (event.key == 'q'):
			print('Return to fin configuration')
			plot.draw()

	def onDragCompletion(self):
		print("START: (%d, %d), END: (%d, %d)" % (self.START_NODE[0], self.START_NODE[1], self.END_NODE[0], self.END_NODE[1]))
		setRect(self.START_NODE, self.END_NODE, self.mask)
		plot.draw()

		#plt.clf()
		#plt.pcolormesh(x,y,conf_matrix)

	def onLineModeCompletion(self):
		thickness = self.thickness - 1
		self.END_NODE = (self.X_NODE,self.Y_NODE)
		setRect(self.START_NODE, self.END_NODE, self.mask, thickness)
		print("Line Mode : START: (%d, %d), END: (%d, %d)" % (self.START_NODE[0], self.START_NODE[1], self.END_NODE[0], self.END_NODE[1]))
		self.START_NODE = self.END_NODE

	def connect(self, fig):
		mpl.rcParams['keymap.fullscreen'].remove('f')
		mpl.rcParams['keymap.save'].remove('s')
		mpl.rcParams['keymap.quit'].remove('q')
		mpl.rcParams['keymap.yscale'].remove('l')

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



