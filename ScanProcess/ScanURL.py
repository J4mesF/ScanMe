

import base64
import json
import requests
from ScanProcess.GetAPIkey import *

class ScanURL:
    def __init__(self, url):
        self.url = url
        self.api_key =Get_API()
        self.base_url = 'https://www.virustotal.com/api/v3/urls'
        self.proxies = None
        self.headers = {'x-apikey': self.api_key,
                        'Accept': 'application/json'}
        self.status_code='I Hate Bugs'
        try:
            response = requests.post(self.base_url,headers=self.headers,data={'url': self.url},proxies=self.proxies)
            self.status_code =response.status_code
            #print(self.status_code)
        except:
            self.status_code ='I Hate Bugs'
    def Scan(self):
        # global data
        try:
            encoded_url = base64.b64encode(self.url.encode())
            response = requests.get(self.base_url + '/{}'.format(encoded_url.decode().replace('=', '')), headers=self.headers, proxies=self.proxies)
            self.dat = response.json()['data']['attributes']['last_analysis_results']
            #print(self.dat)
        except:
            self.dat={}

