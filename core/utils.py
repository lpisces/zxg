#!/usr/bin/env python
# -*- coding:utf-8 -*- 

import requests
import time

def get(url, headers = None, retry = 3, pause = 3):
  if headers == None:
    headers = {"Accept-Encoding": "gzip, deflate, sdch", "user_agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"}
  while retry > 0:
    try:
      r = requests.get(url, headers = headers)
    except Exception as e:
      retry -= 1
      time.sleep(pause)
      continue
    if retry > 0:
      return r
  return None
 
