import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(9, 6),subplot_kw={'xticks': [0,2,4,6,8,10,12], 'yticks': [0,2,4,6,8,10,12,14,16,18,20]})

from matplotlib.lines import Line2D
count=0
for ax in axs.flat:
    title='f_'+str(count)
    ax.set_title(title)
    ax.xaxis.set_label_text(title+"_scores")
    ax.yaxis.set_label_text(title+"_count")
    if count!=0 and count!=1:
        x=range(0,10)
        y=np.random.randint(0,20,10)
        ax.plot(x,y)
        ax.set_xlim(min(x),max(x))
        ax.set_ylim(min(y),max(y))
    else:
        x=np.arange(0,10,0.1)
        y = -1 * (x - 2) * (x - 8) +10
        ax.plot(x,y,color='red')
        ax.set_xlim(0,10)
        ax.set_ylim(0,20)
        if count==0:
            i= np.linspace(2,9,10)
            y_i=-1 * (i - 2) * (i - 8) +10
            ax.fill_between(i,y_i,interpolate=True,color='green',alpha=0.5)
        elif count==1:
            i= np.linspace(2,9,10)
            y_i=-1 * (i - 2) * (i - 8) +10
            ax.fill_between(i,y_i,step='mid',interpolate=True,color='blue',alpha=0.5)
    count+=1
plt.tight_layout()
plt.show()
