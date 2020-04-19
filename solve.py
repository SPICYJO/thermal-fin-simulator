import numpy as np

import settings
import fin_conf

solution_matrix = np.zeros((settings.TN,settings.CYN,settings.CXN,))

def nodeType(y,x):
	if (y<0 or y>=settings.CYN):
		return 0
	if (x<0 or x>=settings.CXN):
		return 0
	return fin_conf.conf_matrix[y][x]

def solve_transient():
	global solution_matrix

	# initial condition
	for m in range(settings.CXN):
		for n in range(settings.CYN):
			solution_matrix[0][n][m] = (settings.T_base if (nodeType(n,m) == 2) else settings.T_inf)
	
	# transient values
	for timeframe in range(0,settings.TN-1):
		for m in range(settings.CXN):
			for n in range(settings.CYN):
				if(nodeType(n,m) == 0):
					solution_matrix[timeframe+1][n][m] = settings.T_inf
				elif(nodeType(n,m) == 2):
					solution_matrix[timeframe+1][n][m] = settings.T_base
				else:
					solution_matrix[timeframe+1][n][m] = solution_matrix[timeframe][n][m] + heat_transfer_into(n,m,timeframe)/(settings.rho*settings.NODE_SIZE*settings.NODE_SIZE*settings.THICKNESS*settings.cp)

	print("solve_transient completed!")

def heat_transfer_into(y,x,timeframe):
	heat_in_sum = 0

	for (ext_y, ext_x) in [(y-1,x), (y+1,x), (y,x-1), (y,x+1)]:
		if (nodeType(ext_y, ext_x) == 0):
			heat_in_sum += (settings.T_inf-solution_matrix[timeframe][y][x]) * settings.h * settings.THICKNESS * settings.NODE_SIZE * settings.TIME_SLICE
		else :
			heat_in_sum += (solution_matrix[timeframe][ext_y][ext_x]-solution_matrix[timeframe][y][x]) * settings.k * settings.THICKNESS * settings.TIME_SLICE

	# convection heat transfer at surface
	heat_in_sum += 2 * (settings.T_inf-solution_matrix[timeframe][y][x]) * settings.h * settings.NODE_SIZE * settings.NODE_SIZE * settings.TIME_SLICE

	return heat_in_sum

