画柱状图时会遇到添加显著性标记的问题，因为matplotlib没有自带的接口，所以只好自己画了一个
主要思路是用plot画标注框线，用annotate标注。
具体应用的时候需要根据柱状图的位置，调整x和y的坐标

import numpy as np                 #使用import导入模块numpy，并简写成np
import matplotlib.pyplot as plt    #使用import导入模块matplotlib.pyplot，并简写成plt
plt.figure(figsize=(8,4))          #设置绘图对象的宽度和高度
from PIL import Image
from pylab import *  
mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体  
mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题   

x = np.ones((4))
y = np.arange(0.7,1.0,0.1)
plt.plot(x,y,label="$y$",color="black",linewidth=1)

x = np.arange(1,3.1,0.1)
y = 1+0*x
plt.plot(x,y,label="$y$",color="black",linewidth=1)

x0 = 2
y0=1
plt.annotate(r'$***$', xy=(x0, y0), xycoords='data', xytext=(-15, +1),
             textcoords='offset points', fontsize=16,color="red")
x = np.ones((4))*3
y = np.arange(0.7,1.0,0.1)

 
plt.plot(x,y,label="$y$",color="black",linewidth=1)
 
plt.ylim(0,2)             #使用plt.ylim设置y坐标轴范围
plt.xlim(-1,5)
plt.xlabel("随便画画")         #用plt.xlabel设置x坐标轴名称
'''设置图例位置'''
plt.grid(True)
plt.show()
结果示意


示意图
将代码改写成函数，方便复用
def plot_sig(xstart,xend,ystart,yend,sig):
    x = np.ones((2))*xstart
    y = np.arange(ystart,yend,yend-ystart-0.1)
    plt.plot(x,y,label="$y$",color="black",linewidth=1)
    
    x = np.arange(xstart,xend+0.1,xend-xstart)
    y = 1+0*x
    plt.plot(x,y,label="$y$",color="black",linewidth=1)

    x0 = (xstart+xend)/2
    y0=yend
    plt.annotate(r'%s'%sig, xy=(x0, y0), xycoords='data', xytext=(-15, +1),
                 textcoords='offset points', fontsize=16,color="red")
    x = np.ones((2))*xend
    y = np.arange(ystart,yend,yend-ystart-0.1)
    plt.plot(x,y,label="$y$",color="black",linewidth=1)
    plt.ylim(0,2)             #使用plt.ylim设置y坐标轴范围
    plt.xlim(-1,5)
    plt.xlabel("随便画画")         #用plt.xlabel设置x坐标轴名称
    '''设置图例位置'''
    plt.grid(True)
    plt.show()
plot_sig(1,3.0,0.8,1.1,'***')
将函数的参数都改成列表，使可以同时呈现不同数据之间比较的结果

def plot_sig(xstart,xend,ystart,yend,sig):
    for i in range(len(xstart)):
        x = np.ones((2))*xstart[i]
        y = np.arange(ystart[i],yend[i],yend[i]-ystart[i]-0.1)
        plt.plot(x,y,label="$y$",color="black",linewidth=1)

        x = np.arange(xstart[i],xend[i]+0.1,xend[i]-xstart[i])
        y = yend[i]+0*x
        plt.plot(x,y,label="$y$",color="black",linewidth=1)

        x0 = (xstart[i]+xend[i])/2
        y0=yend[i]
        plt.annotate(r'%s'%sig, xy=(x0, y0), xycoords='data', xytext=(-15, +1),
                     textcoords='offset points', fontsize=16,color="red")
        x = np.ones((2))*xend[i]
        y = np.arange(ystart[i],yend[i],yend[i]-ystart[i]-0.1)
        plt.plot(x,y,label="$y$",color="black",linewidth=1)
        plt.ylim(0,math.ceil(max(yend)+4))             #使用plt.ylim设置y坐标轴范围
    #     plt.xlim(math.floor(xstart)-1,math.ceil(xend)+1)
        #plt.xlabel("随便画画")         #用plt.xlabel设置x坐标轴名称
        '''设置图例位置'''
        #plt.grid(True)
    plt.show()
plot_sig([0.42,1.42],[1.42,2.42],[30,20],[30.8,20.8],'***')
