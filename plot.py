import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

import fin_conf
import settings
import solve

x = np.linspace(0.0, settings.CANVAS_SIZE_X, settings.CXN)
y = np.linspace(0.0, settings.CANVAS_SIZE_Y, settings.CYN)

#plt.gca().set_aspect('equal', adjustable='box')

fig, ax1 = plt.subplots()
#ax1.axes.set_aspect('equal')
#ax1.axis([0.0, settings.CANVAS_SIZE_X, 0.0, settings.CANVAS_SIZE_Y])


pos = None
anim = None


def draw():
	plt.clf()
	postemp = plt.pcolormesh(x,y,fin_conf.conf_matrix, vmin=0, vmax=2)
	plt.gca().set_aspect('equal')
	fig.colorbar(postemp, label='Type')
	plt.draw()

def showSteady():
	print("showSteady!")
	global pos
	plt.clf()
	pos = plt.pcolormesh(x,y,solve.solution_matrix[0], vmin=settings.T_inf, vmax=settings.T_base)
	plt.gca().set_aspect('equal')
	fig.colorbar(pos, label='temperature')
	plt.show()

def showAnimation():
	print("showAnimation!")
	global pos
	global anim
	plt.clf()
	pos = plt.pcolormesh(x,y,solve.solution_matrix[0], vmin=settings.T_inf, vmax=settings.T_base)
	plt.gca().set_aspect('equal')
	fig.colorbar(pos, label='temperature')
	anim = FuncAnimation(
		fig, animate, interval=20, frames=settings.TN-1, repeat_delay = 1000)
	plt.show()

def animate(i):
	pos = plt.pcolormesh(x,y,solve.solution_matrix[i], vmin=settings.T_inf, vmax=settings.T_base)
	current = settings.TIME_SLICE*i
	if i != settings.TN:
		print("%s seconds elapsed" % current )

