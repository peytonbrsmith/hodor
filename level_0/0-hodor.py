#!/usr/bin/python3
import requests

url = "http://158.69.76.135/level0.php"

for i in range(0, 1024):
    requests.post(url, allow_redirects=False, data = {
        'id': 1884,
        'holdthedoor': 'Submit'
    })
