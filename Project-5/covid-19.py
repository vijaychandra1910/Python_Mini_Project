import requests
from win10toast import ToastNotifier
import json
import time

def update():
    r=requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data=r.json() # Convert the response to JSON
    text = f'Confirmed Cases : {data["cases"]} \nDeaths : {data["deaths"]} \nRecovered : {data["recovered"]}'

    while True:
        toaster = ToastNotifier()
        toaster.show_toast("COVID-19 Update", text, duration=10)  # Display the notification for 10 seconds
        time.sleep(60)
update()  # Call the update function to start the notifications
