import requests
import datetime as dt
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

def check_stock_price(company):
    api_key_stock = "Y8788UQ7ZSX6USB9"
    api_stock = "https://www.alphavantage.co/query"
    parameters_stock = {
        "function": "TIME_SERIES_DAILY",
        "symbol": company,
        # "interval": "60min",
        "outputsize": "compact",
        "apikey": api_key_stock,
    }
    response_stock = requests.get(api_stock, params=parameters_stock)
    return response_stock


def check_news(company):
    newsapi_key = "9d5a3f7ca4024fc1adec1092b15541eb"
    api_news = "http://newsapi.org/v2/top-headlines?"
    # api_news = "http://newsapi.org/v2/everything"
    parameters_news = {
        "country": "us",
        "q": company,
        "category": "business",
        "apiKey": newsapi_key,
    }

    response_news = requests.get(api_news, params=parameters_news)
    news_titles = []
    try:
        for n in range(2):
            news_titles.append(response_news.json()["articles"][n]["title"])

    except IndexError:
        for n in range(len(response_news.json()["articles"])):
            news_titles.append(response_news.json()["articles"][n]["title"])

    finally:
        return "\nNEWS: ".join(tuple(news_titles))


def create_message(company, change, text):
    body = f"{company}: {change}%\nNEWS: {text}"
    # print(body)
    return body

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
change = False
## STEP 1: Use https://newsapi.org
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get date time
time_day = dt.datetime.now()
if time_day.isoweekday() == 7:
    time_yestarday = str((dt.datetime.now() - dt.timedelta(days=2)).date())
    time_bf_time_yestarday = str((dt.datetime.now() - dt.timedelta(days=3)).date())
elif time_day.isoweekday() == 1:
    time_yestarday = str((dt.datetime.now() - dt.timedelta(days=3)).date())
    time_bf_time_yestarday = str((dt.datetime.now() - dt.timedelta(days=4)).date())
elif time_day.isoweekday() == 2:
    time_yestarday = str((dt.datetime.now() - dt.timedelta(days=1)).date())
    time_bf_time_yestarday = str((dt.datetime.now() - dt.timedelta(days=4)).date())
else:
    time_yestarday = str((dt.datetime.now() - dt.timedelta(days=1)).date())
    time_bf_time_yestarday = str((dt.datetime.now() - dt.timedelta(days=2)).date())

response_stock = check_stock_price(STOCK)

yd_price = float(response_stock.json()['Time Series (Daily)'][time_yestarday]["4. close"])
byd_price = float(response_stock.json()['Time Series (Daily)'][time_bf_time_yestarday]["4. close"])
diff_p = round((yd_price/byd_price - 1)*100, 2)

if (diff_p >= 5) or (diff_p <= -5):
    # print("GetNews")
    change = True
    # print(yd_price)
    # print(byd_price)
    # print(diff_p)

## STEP 2: Use https://www.alphavantage.co
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news_titles = check_news(COMPANY_NAME)
# print(news_titles)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
account_sid = "YOUR ACCOUNT SID"
auth_token = "YOUR AUTH TOKEN"

api_phone_number = "+12526426998"
my_phone_number = "+48662817633"
# change = True
if change:
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    #
    # client = Client(account_sid, auth_token, http_client=proxy_client)
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                         body=create_message(COMPANY_NAME, diff_p, news_titles),
                         from_=api_phone_number,
                         to=my_phone_number
                 )
    print(message.status)
print(create_message(COMPANY_NAME, diff_p, news_titles))
#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
