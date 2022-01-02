import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
import numpy as np
from datetime import datetime
from time import strftime, gmtime
import os
import function.status as status

path = os.getcwd()

title_f = fm.FontProperties(fname=f"{path}/TaipeiSansTCBeta-Regular.ttf", size = 20)
f = fm.FontProperties(fname=f"{path}/TaipeiSansTCBeta-Regular.ttf", size = 12)

point_table = ['愛情進度', '學業成績', '養生', '聲望']


def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = 'center')


def score_illu(love_progress, grade, yang_sheng, prestige):
    global point_table
    

    points = [love_progress, grade, yang_sheng, prestige]  # 應該要讀入結尾數值
    # 圖形長與寬可以再討論
    x = np.arange(len(point_table))
    addlabels(point_table, points)
    plt.bar(x, points, color=['red', 'green', 'blue', 'yellow'])
    plt.xticks(x, point_table, font = f)
    plt.xlabel('評分值', font = f)
    plt.ylabel('分數', font = f)
    plt.savefig("figure/ability/finalpix.png")  # 這裡會選擇存檔路徑與檔名
    return 'finalpix'
    
