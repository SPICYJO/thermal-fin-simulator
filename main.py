import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

import settings
import fin_conf
import plot

x = np.linspace(0.0, settings.CANVAS_SIZE_X, settings.CXN)
y = np.linspace(0.0, settings.CANVAS_SIZE_Y, settings.CYN)


iom = fin_conf.IO_Manager()
iom.connect(plot.fig)

plot.draw()

plt.show()
