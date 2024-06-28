import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt("data.txt",usecols=(0,1,2,3), skiprows=1)
HIP = data[:,0]

Vmag = data[:,1] #require vmag to make size of stars not to show them identical;

RA= data[:,2] #RA values are given in degrees; will convert them to hours and make in 24 hour format
RA = RA*24/360

DEC = data[:,3] #declination is given in degrees as required


fig, ax = plt.subplots()

fig.set_facecolor('black')  # Set the figure background color to black
ax.set_facecolor('black')  # Set the axis background color to black

ax.scatter(RA,DEC, color='white', marker='o',s=80*(np.power(10,Vmag/-2.5)))

#ax.grid(color='white', linestyle='--', linewidth=0.5)
ax.tick_params(colors='white')  # Set tick labels color to white
for spine in ax.spines.values():
    spine.set_color('white')  # Set spines color to white


ax.set_xlabel('Right Ascension', color='white')
ax.set_ylabel('Declination', color = 'white')

ax.grid(False)
ax.set_xlim(0,24)
ax.set_ylim(-90,90)


plt.show()





