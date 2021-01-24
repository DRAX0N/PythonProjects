import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

api_key = "e4975bddbf50db5673c17bb8dc6895f2"
API = "https://api.openweathermap.org/data/2.5/onecall"

account_sid = "YOUR ACCOUNT SID"
auth_token = "YOUR AUTH TOKEN"

api_phone_number = "+12526426998"
my_phone_number = "+48662817633"

parameters={
    "lat": 50.028345,
    "lon": 19.929532,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response = requests.get(API, params=parameters)
response.raise_for_status()
weather_data = response.json()
hour = 0
# print(weather_data["hourly"][hour]["weather"][0]["id"])
will_rain = False
for h in range(12):
    rain = weather_data["hourly"][h]["weather"][0]["id"]
    if rain < 700:
        will_rain = True

if will_rain:
    print("Bedzie dzisiaj padac!")

    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)

    message = client.messages \
                    .create(
                         body="Będzie dzisiaj padać",
                         from_=api_phone_number,
                         to=my_phone_number
                 )
    print(message.status)
else:
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body="Nie będzie dzisiaj padać",
                         from_=api_phone_number,
                         to=my_phone_number
                 )
    print(message.status)
# print("Pada na zewnątrz")