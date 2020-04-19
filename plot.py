import settings
import matplotlib.pyplot as plt
import fin_conf
import numpy as np

x = np.linspace(0.0, settings.CANVAS_SIZE_X, settings.CXN)
y = np.linspace(0.0, settings.CANVAS_SIZE_Y, settings.CYN)

fig, ax1 = plt.subplots()
ax1.axis([0.0, settings.CANVAS_SIZE_X, 0.0, settings.CANVAS_SIZE_Y])

def draw():
	plt.clf()
	plt.pcolormesh(x,y,fin_conf.conf_matrix)
	plt.draw()