# -*- coding:UTF-8 -*-
import requests
import re


def get_token():
  url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
  data = {"corpid":"ww21ec0118cc6fdc69","corpsecret":"KYZ2bs4XeZsXADJCDfW86F38iXOnutoTe4gMhV4j4tc"}
  r = requests.get(url,data)
  return r


def send_msg(token_result,alert_msg):
  url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" +  str(token_result)
  header = {'Content-Type':'application/json;charset=UTF-8'}
  data = {
    "touser" : "GuGuangTong|LuoZhaoFei|YangFuShan",
    "msgtype" : "text",
    "agentid" : "1000003",
    "text" : {"content" : alert_msg},
    "safe" : 0,
    "enable_id_trans": 0,
    "enable_duplicate_check": 0,
    "duplicate_check_interval": 1800
  }
  post_result = requests.request("post",url,json=data,headers=header)
  return


def alert_run(alert_from,alert_content):
  if alert_from == "alert@h3c.com":
     alert_from = "IMC"
  alert_msg = "告警平台:\t" + alert_from + '\n' + '告警内容:' + alert_content
  res = get_token()
  xml_data = res.content.decode("utf-8")
  iter_rules = '"access_token":"(\S+)",'
  token_result = re.search(iter_rules,xml_data).group(1)
  send_msg(token_result,alert_msg)
