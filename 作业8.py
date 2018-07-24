

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 09:06:50 2018

@author: admirer
"""

#exercise 8
import urllib.request as r;

f = open('data2.txt','w',encoding = 'utf-8')  #换文件名

for i in range(0,100):
    #https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180719&ie=utf8&loc=%E6%B5%8E%E5%8D%97&s=0&ajax=true   0前面换网址
    url = 'https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180719&ie=utf8&loc=%E6%B5%8E%E5%8D%97&s='+str(i*44)+'&ajax=true'
    try:
        data = r.urlopen(url).read().decode('utf-8','ignore')
    except:
        print('第'+str(i+1)+'页读取数据错误')    
    f.write(data+'\n')
    print('写文件中...第'+str(i+1)+'页')

f.close()
print('完成...')





