import wiotp.sdk.device
import time
import random
import json
with open("C:/Users/NEW PC/Desktop/data.json") as f:
        data=json.load(f)
myConfig = { 
    "identity": {
        "orgId": "x4umcs",#place you're crednetials 
        "typeId": "iotdevice",
        "deviceId":"1001"
    },
    "auth": {
        "token": "1234567890"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    print("enter vehicle number")
    n=int(input())

    for i in range(len(data)):
        if n==i:
            myData={'location':data[i]['Location'],'latitude':data[i]['Venue Latitude'], 'longitude':data[i]['Venue Longitude']}
            client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
            print("Published data Successfully: %s", myData)
            client.commandCallback = myCommandCallback
            time.sleep(5)
                
    
client.disconnect()
   

