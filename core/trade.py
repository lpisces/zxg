#!/usr/bin/env python
# -*- coding:utf-8 -*- 

import requests
import json
from dateutil.parser import parse
import datetime
import random

# 复权数据
def _fq(market, code, start, end, k = "day", fq = "qfq", size = 640):
  url = "http://web.ifzq.gtimg.cn/appstock/app/fqkline/get?_var=kline_dayqfq&param=%s%s,%s,%s,%s,%s,%s&r=%s" % (market, code, k, start, end, size, fq, random.random())
  return json.loads(requests.get(url).text.split("=")[1])["data"][market + code][fq + k]

def long_fq(market, code, start, end, k = "day", fq = "qfq", size = 640):
  date_s, date_e = parse(start), parse(end)
  data = []
  while True:
    start = date_s.strftime("%Y-%m-%d")
    end = date_e.strftime("%Y-%m-%d")
    if (date_e - date_s).days <= 640:
      data += _fq(market, code, start, end, k, fq, size)
      print start, end
      return data
    else:
      end = (date_s + datetime.timedelta(days = 640)).strftime("%Y-%m-%d")
      data += _fq(market, code, start, end, k, fq, size)
      print start, end
      date_s = parse(end) + datetime.timedelta(days = 1)

