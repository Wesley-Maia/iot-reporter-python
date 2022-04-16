# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 09:59:00 2022

@author: maiaw
"""

import urllib.request as urllibTS
import json

CHANNEL_ID      = '1358487'
READ_API_KEY    = 'GVDKMPZXU3RK3ZD3'


def import_data(samples):
    url_base = 'https://api.thingspeak.com/channels/'+str(CHANNEL_ID)+'/feeds.json?api_key='+str(READ_API_KEY)+'&results='+str(samples)

    ts          = urllibTS.urlopen(url_base)
    response    = ts.read()
    data        = json.loads(response)
   
    ts.close()	
    
    return data
