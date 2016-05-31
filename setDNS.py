#!/usr/bin/python2
# -*- coding: utf-8 -*-

from src.QcloudApi.qcloudapi import QcloudApi
import sys
import urllib2
import json
module = 'cvm'
action = 'UpdateResourceRecord'
config = {
    'Region': 'sh',
    'secretId': 'AKIDzG07sb9Clb5ebNqNmnUkbtYMhZbFsJLg',
    'secretKey': 'BBiiBD7Yr78IfOwnH0Y7J0TouwapONJd',
    'method': 'post'
}

try:
    service = QcloudApi(module, config)
    if(len(sys.argv)==1):
        print "你可以使用 " + sys.argv[0] + "+你的ip地址来设置ip"
        print "正在自动获取你的ip地址"
        ip_html = urllib2.urlopen("http://test.ip138.com/query/").read()
        ip_json = json.loads(ip_html)
        ip =  ip_json["ip"]
    else:
        ip = sys.argv[1]

    print "Your IP is" + ip


    params = {
    'type' : 1 ,
    'domain' : 'sasasu.cn',
    'subDomain' : "wave",
    'recordType' : "A",
    'ttl' : 120,
    'recordId' : 194112589,
    'recordLine' : 1,
    'recordValue' :  ip
    }

    print  "设置解析中"
    service.generateUrl(action, params)
    ans = service.call(action, params)
    ans_json = json.loads(ans)
    if(ans_json["code"] == 0):
        raw_input("设置成功,请等几分钟生效")
    else:
        print("看起来设置失败了QAQ，失败信息是:",ans_json["message"],"\n失败代码：",ans_json["code"])
        raw_input()
except Exception, e:
    print 'exception:', e
    raw_input()

