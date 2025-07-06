import requests
import time
from datetime import datetime

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.RequestException:
        return False    
    
with open('sites.txt') as file:
    sites = [line.strip() for line in file.readlines()]
    
for site in sites:
    result = check_website(site)
    print(f"{datetime.now()} {site} is {'up' if result else 'down'}")