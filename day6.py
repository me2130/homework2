# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:48:12 2018

@author: me2130
"""
import urllib.request as r
ls=open('all_school.txt',encoding='utf_8').readlines()
schoolls=[]

for line in ls:
    schoolls.append(line.split('-jianjie-')[1].split('.')[0])
    
'北京大学    北京http://www.gaokaopai.com/daxue-jianjie-477.html'.split('-jianjie-')[1].split('.')[0]
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
	       'X-Requested-With': 'XMLHttpRequest'}

f=open('33_2.txt','a',encoding='utf-8')
cnt = 1
for schoolid in schoolls:
    for kemu in [2]:
        for city in [33]:
            try:
                req=r.Request(url,data='id={}&type={}&city={}&state=1'.format(schoolid,kemu,city).encode(),headers=headers)
                data = r.urlopen(req).read().decode('utf-8',' ignore')
                if data[0]!='{':
                    print('error_1')
                else:
                    f.write(data+"\n")
                    print(cnt)
                    cnt += 1
            except:
                print("error_2")
f.close()
print('finish')  #exercise10.3


#exercise1

f = open('all_school.txt','r',encoding='utf-8')
idls = f.readlines()

print("school id are as follows:")
for i in range(0,len(idls)):
    sid = idls[i].split('-jianjie-')[1].split('.')[0]
    f1 = open("all_id.txt",'a+',encoding='utf-8')
    print(sid)
    f1.write(sid+'\n')

f1.close()
f.close()


#exercise 10.2

f = open('city_info_xml.txt','r',encoding = 'utf-8')
cities = f.readlines()

w = open('city_id.txt','a',encoding = 'utf-8')
print("city id are as follows:")
for i in range(0,len(cities)):
    cid = cities[i].split(')\\">')[0][-2:]
    city = cities[i].split(')\\">')[1][0:2]
    print(cid+" "+city)
    w.write(cid+" "+city+'\n')
    
f.close()
w.close()



