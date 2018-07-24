# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 19:27:09 2018

@author: xndx
"""
#五天天气
import urllib.request as r
url='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
city=input('please input the city name:   ')
data=r.urlopen(url.format(city)).read().decode('utf-8','ignore')
import json
data=json.loads(data)
def tips(a):
    if a=='Clear':
        print('tips:不要忘记涂防晒霜！')
    elif a=='Clouds':
        print('tips:美好的天气莫过于此！')
    elif a=='Rain':
        print('tips:记得带雨伞！')
def weather(day):
    print('day'+str(day)+':  ')
    t=2+(int(day)-1)*8
    print('tempreture:'+str(data['list'][t]['main']['temp']))
    print('cityname:'+str(data['city']['name']))
    print('description:'+str(data['list'][t]['weather'][0]['description']))
    print('temp_min:'+str(data['list'][t]['main']['temp_min']))
    print('temp_max:'+str(data['list'][t]['main']['temp_max']))
    print('pressure:'+str(data['list'][t]['main']['pressure']))
    tips(str(data['list'][t]['weather'][0]['main']))
for day in range(1,5):
    weather(day)
def chart(day):
    t=2+(int(day)-1)*8
    a='-'*int(data['list'][t]['main']['temp'])
    return a 
print('the day line chart is')
for day in range(1,5):
    print(chart(day))
    
    
#淘宝数据
import urllib.request as r
import json
url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&type=p&tmhkh5=&spm=a21wu.241046-us.a2227oh.d100&from=sea_1_searchbutton&catId=100&ajax=true'
data=r.urlopen(url).read().decode('utf-8','ignore')
data=json.loads(data)
for i in range(35):
    if i==5:break
    if i==10:continue
    print('price ='+data['mods']['itemlist']['data']['auctions'][i+1]['view_price'])
    print('title ='+data['mods']['itemlist']['data']['auctions'][i+1]['raw_title'])
    print('sale ='+data['mods']['itemlist']['data']['auctions'][i+1]['view_sales'])
    if (i+1)%4==0:
        print('——————————————————————————————————————')