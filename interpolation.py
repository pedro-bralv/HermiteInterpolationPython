import matplotlib.pyplot as plt
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
	t1 = (x[1]-x[0])/2, (y[1]-y[0])/2
	t2 = (x[2]-x[0])/2, (y[2]-y[0])/2 
	xnew, ynew = calc_hermite(x[0], x[1], y[0], y[1], t1, t2)
	for j in range(1, len(x)-2):
		x1, x2, x3, x4 = x[j-1], x[j], x[j+1], x[j+2]
		y1, y2, y3, y4 = y[j-1], y[j], y[j+1], y[j+2]
		t1 = (x3-x1)/2, (y3-y1)/2
		t2 = (x4-x2)/2, (y4-y2)/2
		auxx, auxy = calc_hermite(x2, x3, y2, y3, t1, t2)
		for i in auxx: 
			xnew.append(i)
		for i in auxy:
			ynew.append(i)
	l = len(x)-1
	t1 = (x[l]-x[l-2])/2, (y[l]-y[l-2])/2
	t2 = (x[l]-x[l-1])/2, (y[l]-y[l-1])/2
	auxx, auxy = calc_hermite(x[l-1], x[l], y[l-1], y[l], t1, t2)
	for i in auxx: 
		xnew.append(i)
	for i in auxy:
		ynew.append(i)	

	plt.plot(xnew, ynew, '-')
	plt.show()

with open("./pontos3.txt", 'r') as lines:
	points = [i.strip().split(",") for i in lines]	
	x = [float(i[0]) for i in points]
	y = [-1*float(i[1]) for i in points]
	plot_hermite(x, y)

