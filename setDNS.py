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
        print "useage: " + sys.argv[0] + "+ your id"
        print "get you ip"
        ip_json = urllib2.urlopen("https://httpbin.org/ip").read()
        ip = json.loads(ip_json)["origin"]
    else:
        ip = sys.argv[1]
    print "your ip " + ip
    
    
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

    print service.generateUrl(action, params)
    print service.call(action, params)
    raw_input()
except Exception, e:
    print 'exception:', e
    raw_input()

