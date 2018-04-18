import tushare as ts;
print("Hello world! tushare version ", ts.__version__);
while True :
    stocknum = input("Please input stock number : ")
    if(stocknum == "quit") :
        break;
    df=ts.get_hist_data(stocknum);
    print("stock ", stocknum);
    print(df);
