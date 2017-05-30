import scipy.interpolate as si
import matplotlib.pyplot as plt
from numpy.polynomial.hermite import hermfit, hermval
import numpy as np
LOD = 15;

def calc_hermite(x1, x2, y1, y2, t1, t2):
	xnew = []
	ynew = []
	for i in range(LOD):
			t = float(i)/float(LOD-1);
			b1 =  2*t*t*t - 3*t*t + 1;
			b2 = -2*t*t*t + 3*t*t;
			bt1 = t*t*t - 2*t*t + t;
			bt2 = t*t*t - t*t;
			xnew.append(b1*x1+b2*x2+bt1*t1[0]+bt2*t2[0])
			ynew.append(b1*y1+b2*y2+bt1*t1[1]+bt2*t2[1])
	return xnew, ynew

def plot_hermite(x, y):
	t1 = float(x[1]-x[0])/float(2), float(y[1]-y[0])/float(2)
	t2 = float(x[2]-x[0])/float(2), float(y[2]-y[0])/float(2) 
	xnew, ynew = calc_hermite(x[0], x[1], y[0], y[1], t1, t2)
	for j in range(1, len(x)-3):
		x1, x2, x3, x4 = x[j-1], x[j], x[j+1], x[j+2]
		y1, y2, y3, y4 = y[j-1], y[j], y[j+1], y[j+2]
		t1 = float(x3-x1)/float(2), float(y3-y1)/float(2)
		t2 = float(x4-x2)/float(2), float(y4-y2)/float(2)
		auxx, auxy = calc_hermite(x2, x3, y2, y3, t1, t2)
		for i in auxx: 
			xnew.append(i)
		for i in auxy:
			ynew.append(i)
	l = len(x)-1
	t1 = float(x[l]-x[l-2])/float(2), float(y[l]-y[l-2])/float(2)
	t2 = float(x[l]-x[l-1])/float(2), float(y[l]-y[l-1])/float(2)
	auxx, auxy = calc_hermite(x[l-1], x[l], y[l-1], y[l], t1, t2)
	for i in auxx: 
		xnew.append(i)
	for i in auxy:
		ynew.append(i)	

	plt.plot(x, y, 'kx', xnew, ynew, 'b-')
	plt.show()

with open("./pontos2.txt", 'r') as lines:
	points = [i.strip().split(",") for i in lines]	
	x = [float(i[0]) for i in points]
	y = [-1*float(i[1]) for i in points]
	plot_hermite(x, y)

