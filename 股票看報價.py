import twstock
import time
import os
a = "-"
while True:
    xx = input("請輸入股票代號，多張請加小數點分割 : ").split(".")
    for i in xx :
        print(twstock.codes[i].ㄓname)
        print(a*80)
    gg = input("確認以上股票名稱是否正確，前往報價請按[Y]、重新選擇請按[R]、離開請按[Q] :")
    print(a*80)
    if gg.upper() == "Y":
        break
    elif gg.upper() =="R":
        print("請重新選擇，謝謝。")
        print(a*80)
    elif gg.upper() == "Q":
        os._exit() 
    else:
        print("請認真輸入，別鬧了!!!!")
        print(a*80)
while True:
    time.sleep(30)
    for zzz in range(len(xx)) :
        gginin = twstock.realtime.get(xx[zzz])
        print("股票代號:{0} 股票名稱:{1} 時間{2}".format(xx[zzz],gginin["info"]["name"],gginin["info"]["time"]))
        print("現在股價: ",gginin["realtime"]["latest_trade_price"])
        print(a*80)