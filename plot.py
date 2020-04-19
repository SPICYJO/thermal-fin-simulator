import settings
import matplotlib.pyplot as plt

x = np.linspace(0.0, settings.CANVAS_SIZE_X, settings.CXN)
y = np.linspace(0.0, settings.CANVAS_SIZE_Y, settings.CYN)

fig, ax1 = plt.subplots()
ax1.axis([0.0, settings.CANVAS_SIZE_X, 0.0, settings.CANVAS_SIZE_Y])

def draw():
 	plt.pcolormesh(x,y,fin_conf.conf_matrix)