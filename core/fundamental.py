#!/usr/bin/env python
# -*- coding:utf-8 -*- 

from bs4 import BeautifulSoup as bs
import utils
import pandas as pd
import numpy as np

# 公司概况
def brief(board, code):
  url = "http://www.cninfo.com.cn/information/brief/%s%s.html" % (board, code)
  r = utils.get(url)
  if r == None:
    return None
  r.encoding = "gbk"
  soup = bs(r.text, "html5lib")
  tr = soup.select(".zx_left table tr")

  info = {}  
  attrs = ["fullname", "ename", "address", "cname", "legal_representative", "secretary", "registered_capital", "industry", "postcode", "tel", "fax", "site", "time_to_market", "time_to_apply", "ipo_amount", "ipo_price", "ipo_pe", "ipo_method", "ipo_su", "ipo_sponsor", "ipo_org"]

  for i in range(len(attrs)):
    try:
      info[attrs[i]] = tr[i].select("td")[1].text.replace("\n", "")
    except:
      info[attrs[i]] = ""
  return pd.DataFrame(info, index=[0])


#发行筹资 
def issue(board, code):
  url = "http://www.cninfo.com.cn/information/issue/%s%s.html" % (board, code)
  r = utils.get(url)
  if r == None:
    return None
  r.encoding = "gbk"
  soup = bs(r.text, "html5lib")
  tr = soup.select(".zx_left table tr")

  info = {}  
  attrs = ["ipo_type", "ipo_date", "ipo_kind", "stock_type", "ipo_method", "amount", "rmb_price", "foreign_price", "ipo_money", "ipo_fee", "ipo_pe", "net_rate", "market_rate"]

  for i in range(len(attrs)):
    try:
      info[attrs[i]] = tr[i].select("td")[1].text.replace("\n", "")
    except:
      info[attrs[i]] = ""
  return pd.DataFrame(info, index=[0])
    
#高管
def management(board, code):
  url = "http://www.cninfo.com.cn/information/management/%s%s.html" % (board, code)
  r = utils.get(url)
  if r == None:
    return None
  r.encoding = "gbk"
  soup = bs(r.text, "html5lib")
  tr = soup.select(".zx_left table tr")

  info = []
  attrs = ["name", "position", "birth", "sex", "education"]
  for i in range(len(tr)):
    if i == 0:
      continue
    person = {}
    for a in range(len(attrs)):
      person[attrs[a]] = tr[i].select("td")[a].text.replace("\n", "")
    info.append(person)
  return pd.DataFrame(info)

#十大股东
def shareholders(code, circulate = False):
  if circulate:
    url = "http://www.cninfo.com.cn/information/shareholders/%s.html?www.cninfo.com.cn" % (code, )
  else:
    url = "http://www.cninfo.com.cn/information/circulateshareholders/%s.html?www.cninfo.com.cn" % (code, )
  r = utils.get(url)
  if r == None:
    return None
  r.encoding = "gbk"
  soup = bs(r.text, "html5lib")
  tr = soup.select(".zx_left table tr")

  info = []
  date = None
  attrs = ["date", "holder", "amount", "percent", "type"]
  for t in range(len(tr)):
    if t == 0:
      continue
    row = {}
    td = tr[t].select("td")
    if len(td) == 5:
      for i in range(len(attrs)):
        row[attrs[i]] = td[i].text
      date = td[0].text
    if len(td) == 4:
      for i in range(len(attrs[1:])):
        row[attrs[1:][i]] = td[i].text
      row["date"] = date
    row["holder"] = "".join(row["holder"].split(".")[1:])
    info.append(row)
  return pd.DataFrame(info)

# 分红送转
def dividend(board, code):
  url = "http://www.cninfo.com.cn/information/dividend/%s%s.html" % (board, code)
  r = utils.get(url)
  if r == None:
    return None
  r.encoding = "gbk"
  soup = bs(r.text, "html5lib")
  tr = soup.select(".zx_left table tr")

  info = []
  attrs = ["date", "program", "reg_day", "div_day", "day_to_market"]
  for t in range(len(tr)):
    if t == 0:
      continue
    row = {}
    for i in range(len(tr[t].select("td"))):
      row[attrs[i]] = tr[t].select("td")[i].text.replace(" ", "").replace("\n", "")
    info.append(row)
  return pd.DataFrame(info)

# 配股
def allotment(board, code):
  url = "http://www.cninfo.com.cn/information/allotment/%s%s.html" % (board, code) 
  r = utils.get(url)
  if r == None:
    return None
  r.encoding = "gbk"
  soup = bs(r.text, "html5lib")
  tr = soup.select(".zx_left table tr")

  info = []
  attrs = ["date", "program", "price", "reg_date", "base_date", "pay_date", "day_to_market"]
  for t in range(len(tr)):
    if t == 0:
      continue
    row = {}
    for i in range(len(tr[t].select("td"))):
      row[attrs[i]] = tr[t].select("td")[i].text.replace(" ", "").replace("\n", "")
    info.append(row)
  return pd.DataFrame(info)

