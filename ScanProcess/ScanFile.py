import os
import sys
import requests
import json
import time
from ScanProcess.GetAPIkey import *

class FileScan:
    def __init__(self, Link ):

        self.Link = Link
        self.proxies=None
        self.base_url ='https://www.virustotal.com/api/v3/files'
        self.url_analys = 'https://www.virustotal.com/api/v3/analyses/'
        self.api_key = Get_API()
        self.headers = {'x-apikey': self.api_key,'Accept': 'application/json'}
        self.count = 0
        self.upload()
    def upload(self):
        file_size = os.path.getsize(self.Link)
        if file_size < 33554432:
            print('File size < 33554432')
            with open(self.Link, 'rb') as f:
                data={'file': f.read()}

            response = requests.post(self.base_url, headers = self.headers, files=data, proxies=self.proxies)
            print(response.status_code)
            self.id =response.json()['data']['id']
            print('The ID is: ', end='')
            print(self.id)
            #time.sleep(10)

            self.GetAnalys()


        if file_size >= 33554432:
            print('sorry please try again ')
    def GetAnalys(self):
        r = requests.get(self.url_analys+ self.id, headers=self.headers, proxies=self.proxies)
        #print(r.status_code)
        self.result = r.json()['data']['attributes']['results']
        #print(self.result)
