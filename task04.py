from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import numpy as np


x=np.linspace(0,10,100)
y1 = np.cos(2 * np.pi * x) * np.exp(-x)
y2=x*2+3
fig, axes = plt.subplots(1,2,figsize=(10, 8))
font1 = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 16,
        }
font2 = {'family': 'Calibri',
        'weight': 'normal',
        'size': 10,
        }
p1,=axes[0].plot(x,y1,label="line1",color="red")
p2,=axes[1].plot(x,y2,label="line2",color="yellow",linestyle="--")
ticks = np.arange(0., 20.1, 2.)
tickla = [f'{tick:1.1f}' for tick in ticks]
axes[0].xaxis.set_ticks(ticks)
axes[0].xaxis.set_ticklabels(tickla,rotation=30, fontsize='small')
axes[0].set_xlabel('time',fontproperties=font1)
axes[0].set_ylabel('beat',fontproperties=font1)
axes[1].xaxis.set_ticks(np.arange(0.,10.1,2.))
axes[1].xaxis.set_ticklabels([f'{tick:1.2f}' for tick in np.arange(0.,10.1,2.)],rotation=30, fontsize='small')
axes[1].set_xlabel('time',fontproperties=font2)
axes[1].set_ylabel('growth',fontproperties=font2)
axes[0].legend(loc='lower right', prop=font1, fontsize=10)
axes[1].legend(loc='upper left',prop=font2,fontsize=5)
plt.show()



![image](https://user-images.githubusercontent.com/11401076/102869796-1fc91180-4477-11eb-985d-6aef1ee12322.png)
