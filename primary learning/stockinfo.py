import tushare as ts
import matplotlib.pyplot as mp_plt
from matplotlib.pylab import date2num
import matplotlib.finance as mpf
import datetime
print("Hello world! tushare version ", ts.__version__)
#while True:
if(True):
    stocknum = '601166'
    #stocknum = input("Please input stock number : ")
    df=ts.get_hist_data(stocknum)

    print("stock ", stocknum)
    data_list = []

    for dates, row in df.iterrows():
        # 将时间转换为数字
        date_time = datetime.datetime.strptime(dates, '%Y-%m-%d')
        t = date2num(date_time)
        open, high, low, close = row[:4]
        datas = (t, open, high, low, close)
        data_list.append(datas)

    # 创建子图
    fig, ax = mp_plt.subplots()
    fig.subplots_adjust(bottom=0.2)
    # 设置X轴刻度为日期时间
    ax.xaxis_date()
    mp_plt.xticks(rotation=45)
    mp_plt.yticks()
    mp_plt.title("stock K line ")
    mp_plt.xlabel("date")
    mp_plt.ylabel("price")
    mpf.candlestick_ohlc(ax, data_list, width=1.5, colorup='r', colordown='green')
    mp_plt.grid()
    mp_plt.show()
