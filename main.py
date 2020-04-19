import numpy as np
import matplotlib as mpl

import settings
import fin_conf

x = np.linspace(0.0, settings.CANVAS_SIZE_X, settings.CXN)
y = np.linspace(0.0, settings.CANVAS_SIZE_Y, settings.CYN)


fig, ax1 = plt.subplots()
ax1.axis([0.0, settings.CANVAS_SIZE_X, 0.0, settings.CANVAS_SIZE_Y])


iom = fin_conf.IO_Manager()
iom.connect(fig)

plt.pcolormesh(x,y,fin_conf.conf_matrix)



plt.show()
