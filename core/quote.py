#!/usr/bin/env python
# -*- coding:utf-8 -*- 

import requests
import numpy as np
import json
import datetime

def qq_quote(market, code):
  url = "http://web.ifzq.gtimg.cn/appstock/app/minute/query?_var=&code=%s%s&r=%s" % (market, code, np.random.uniform(0, 1))
  data = [i.split(" ") for i in json.loads(requests.get(url).text)["data"][market+code]["data"]["data"]]

  data2 = requests.get("http://web.sqt.gtimg.cn/q=%s%s?r=%s" % (market, code, np.random.uniform(0, 1))).text.split("=")[1].replace("\"", "").split("~")
  pre_close = float(data2[4])
  date = datetime.datetime.today().strftime("%Y%m%d")
  
  r = []
  total = 0.0
  total_amount = 0
  for i in data:
    node = {}
    node["date"] = date
    node["preClose"] = pre_close
    node["time"] = int(i[0]) * 10000
    node["price"] = float(i[1])
    node["volumn"] = float(i[2]) * float(i[1])
    node["netChangeRatio"] = (float(i[1]) - pre_close) / pre_close
    node["amount"] = float(i[2])
    total += node["volumn"]
    total_amount += node["amount"]
    node["avgPrice"] = total / total_amount
    r.append(node)
  return r

print qq_quote("sz", "000002")
