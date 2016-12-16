#!/usr/bin/env python
# -*- coding:utf-8 -*- 

import requests
from bs4 import BeautifulSoup as bs

# 获取股票列表
def _stock_list():
  # A股上市公司列表页面 
  STOCK_LIST_URL = "http://www.cninfo.com.cn/cninfo-new/information/companylist"
  url = STOCK_LIST_URL
  r = requests.get(url)
  soup = bs(r.text, 'html5lib')

  stock = []

  # 深圳主板
  a = soup.select('#con-a-1 > ul > li a')
  for s in a:
    code = s.text.split(" ")[0]
    name = "".join(s.text.split(" ")[1:])
    market = 'sz'
    board = 'szmb'
    stock.append((market, code, board, name))

  # 中小板
  a = soup.select('#con-a-2 > ul > li a')
  for s in a:
    code = s.text.split(" ")[0]
    name = "".join(s.text.split(" ")[1:])
    market = 'sz'
    board = 'szsme'
    stock.append((market, code, board, name))

  #创业板
  a = soup.select('#con-a-3 > ul > li a')
  for s in a:
    code = s.text.split(" ")[0]
    name = "".join(s.text.split(" ")[1:])
    market = 'sz'
    board = 'szcn'
    stock.append((market, code, board, name))

  #上证主板
  a = soup.select('#con-a-4 > ul > li a')
  for s in a:
    code = s.text.split(" ")[0]
    name = "".join(s.text.split(" ")[1:])
    market = 'sh'
    board = 'shmb'
    stock.append((market, code, board, name))

  return stock

def stock_list(board = "all"):
  lst = _stock_list()
  if board == "all":
    return lst
  else:
    return tuple([i for i in lst if i[2] == board])

if __name__ == "__main__":
  print len(stock_list("all"))
