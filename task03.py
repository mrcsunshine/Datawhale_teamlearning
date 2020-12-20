import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

ex1=pd.read_csv("D:/fantastic-matplotlib-main/data/layout_ex1.csv")

ex1['year']=ex1['Time'].apply(lambda x:int(x.split("-")[0]))
ex1['month']=ex1['Time'].apply(lambda x:int(x.split("-")[1]))
ex1.head()

fig,axs=plt.subplots(2,5,figsize=(10,4),sharex=True,sharey=True)
fig.suptitle('墨尔本1981年至1990年月温度曲线')
count=0
for i in range(2):
    for j in range(5):
        title=1981+count
        axs[i][j].set_title(str(title)+"年")
        axs[i][j].set_xlim(1,12)
        axs[i][j].set_xticks(range(1,13))
        axs[i][j].set_ylim(5,15)
        if i==1:axs[i][j].set_xlabel('月份')
        if j==0:axs[i][j].set_ylabel('气温')
        count+=1
fig.tight_layout()
for i,year in enumerate(range(1981,1991)):
    r,c=i//5,i%5
    temperature=ex1.loc[ex1.year == year,'Temperature'].tolist()
    month=ex1.loc[ex1.year==year,'month'].tolist()
    axs[r][c].plot(month,temperature,marker="*")
    
    
data = np.random.randn(2,150)
fig=plt.figure(figsize=(6,6))
spec=fig.add_gridspec(nrows=2,ncols=2,width_ratios=[6,1],height_ratios=[1,6])
main_axes=fig.add_subplot(spec[1,0])
xm_axes=fig.add_subplot(spec[0,0],sharex=main_axes)
ym_axes=fig.add_subplot(spec[1,1],sharey=main_axes)
main_axes.scatter(data[0],data[1])
main_axes.set_xlabel("my_data_x")
main_axes.set_ylabel("my_data_y")
xm_axes.hist(data[0])
ym_axes.hist(data[1],orientation='horizontal')
xm_axes.get_xaxis().set_visible(False)
xm_axes.get_yaxis().set_visible(False)
for s in xm_axes.spines.values():
    s.set_visible(False)
ym_axes.get_xaxis().set_visible(False)
ym_axes.get_yaxis().set_visible(False)
for s in ym_axes.spines.values():
    s.set_visible(False)
