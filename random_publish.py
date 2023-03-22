from random import randint
from time import sleep
# importing the requests library
import requests
  
# defining the api-endpoint
MINIKUBEURL = "http://127.0.0.1:50693" # Change this line after running minikube url
URI = "/publish"
API_ENDPOINT = MINIKUBEURL + URI
  
# data to be sent to api
data = {"deviceid": "kenny", "lat": "13.141191", "lon": "-59.624129", "sarcolour": "brown", "sarlength": "20", "sarwidth": "1", "sardirection": "N", "saramount": "medium"}
  

while True:
    delay = randint(1,10)
    sleep(delay)
    # sending post request and saving response as response object
    r = requests.post(url = API_ENDPOINT, data = data)