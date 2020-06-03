import requests
import time
import threading, json
 
# This Function will upload Latitude and Longitude values to the Thingspeak channel
def read_data_thingspeak():
    
    URL = 'https://api.thingspeak.com/channels/1069873/fields/3/last?key=ZZQI71B73Q3FCOEP'
    KEY = 'ZZQI71B73Q3FCOEP'  # Thingspeak Read API Key
    get_data=requests.get(URL).json()
    time.sleep(10)
    return get_data
    
    
if __name__ == "__main__":

        while True:
                print(read_data_thingspeak())
