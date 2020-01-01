import requests
import os

def spider_baidu():
    """爬取百度"""
    url = "http://www.baidu.com/s"
    kv = {"wd": "python"}
    try:
        r = requests.get(url, param=kv)
        r.raise_for_status()
        print(r.text[:1000])
    except:
        print("爬取失败")