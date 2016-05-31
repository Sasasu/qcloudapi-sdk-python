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
params = {
    'type' : 1 ,
    'domain' : 'sasasu.cn',
    'subDomain' : "wave",
    'recordType' : "A",
    'ttl' : 120,
    'recordId' : 194112589,
    'recordLine' : 1,
    'recordValue' :  "0.0.0.0"
}

def getip():
    if(len(sys.argv)==1):
        print "You can use " + sys.argv[0] + "+ ip"
        print "Getting your ip"
        ip_html = urllib2.urlopen("http://test.ip138.com/query/").read()
        ip_json = json.loads(ip_html)
        ip =  ip_json["ip"].decode()
    else:
        ip = sys.argv[1].decode()
    return ip

def main():
        service = QcloudApi(module, config)
        params["recordValue"] = getip()
        print "Your IP is " + params["recordValue"]

        print  "Setting record"
        service.generateUrl(action, params)
        ans = json.loads(service.call(action,params))
        if(ans["code"] == 0):
            raw_input("设置成功,请等几分钟生效")
        else:
            print("看起来设置失败了QAQ，失败信息是:",ans["message"],"\n失败代码：",ans["code"])
            raw_input()

if (__name__ == '__main__'):
    main()

