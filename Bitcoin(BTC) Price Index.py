#!/usr/bin/env python
# coding: utf-8
# ORIGINALLY CREATED BY PARV ASHWANI (ALL RIGHTS RESERVED)
# API BY COINDESK(JSON)

import requests, json




#https://api.coindesk.com/v1/bpi/currentprice/<CODE>.json
base_url = "https://api.coindesk.com/v1/bpi/currentprice/"
resol = input("Enter currency code:")
Currency_code = resol.upper()
complete_url = base_url + Currency_code + ".json"




response = requests.get(complete_url)




x = response.json()




TimeLog =x['time']['updated']




United_States_Dollar_description = x['bpi']['USD']['description']




United_States_Dollar_value = x['bpi']['USD']['rate']




user_cur_des = x['bpi'][Currency_code]['description']




user_cur_value = x['bpi'][Currency_code]['rate']
print()
print("TIMELOG:-:",TimeLog)
print()
print("1 BTC(Bitcoin) equals:-:",United_States_Dollar_value,"USD(United States Dollar)")
print()
print("Requested Currency:-:",user_cur_des)
print()
print("1 BTC(Bitcoin) equals:-:",user_cur_value + str(Currency_code) + str(user_cur_des))
print()
print("Thank You for using the application"),print("HANDCRAFTED BY PARV ASHWANI")
