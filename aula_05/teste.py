import matplotlib.pyplot as plt
import random as rd
import time

plt.ion()
x=[]
y=[]

fig, ax = plt.subplots()

while True:
    ax.set_xlim(1,100)
    ax.set_ylim(1,100)

    x.append(rd.randint(1,99))
    y.append(rd.randint(1,99))

    ax.plot(x,y)

    time.sleep(10**5)
    input()
    
   

