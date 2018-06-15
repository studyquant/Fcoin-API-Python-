# -*- coding: utf-8 -*-
"""

@author: 躺着也挣钱
QQ群 ：  422922984

"""


import pandas as pd 
from fcoin3 import Fcoin
from datetime import datetime
#if python3 use 
#from fcoin import Fcoin

fcoin = Fcoin()
fcoin.auth('key ', 'secret') 

#取K线数据 

ft_usdt = fcoin.get_candle('M3','ftusdt')  #M3 = 分钟线，   取150条数据

# 取得当前账户信息
print(fcoin.get_balance())


# 
print(fcoin.get_symbols())


print(fcoin.get_currencies())

#
#print(fcoin.buy('fteth', 0.0001, 10))
#

