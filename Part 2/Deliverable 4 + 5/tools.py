import requests
from ratelimit import limits, sleep_and_retry

#limits rate to 1 request every second. 
@sleep_and_retry
@limits(3, 3)
def get(url):
    print ("Requested: " + url)
    return requests.get(url).text  