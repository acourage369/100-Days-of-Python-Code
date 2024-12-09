import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "S263JZ31EQGP4BU2"
NEWS_API_KEY = "989edd3fcca44dc7b0e290ecc94e7cfb"
ACCOUNT_SID = "AC60f81974f8ce1730b21f41af40128476"
AUTH_TOKEN = "3b7bb5314ec6e8ad3563f5a9f0c4f746"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get yesterday's closing stock price.
## API call to Alphavantage
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]

stock_list_data = [value for (key, value) in stock_data.items()]

## Get yesterday's closing stock price
yesterday_date = stock_list_data[0]
yesterday_closing_price = yesterday_date["4. close"]
print(yesterday_closing_price)

day_before_yesterday_date = stock_list_data[1]
day_before_yesterday_closing_price = yesterday_date["4. close"]
print(day_before_yesterday_closing_price)

# Find the positive difference between yesterday_closing price and day_before_yesterday_closing_price.
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)

# Using the News API to get articles related to the COMPANY_NAME.
if abs(diff_percent) < 5:
    new_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(url=NEWS_ENDPOINT, params=new_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]

    #  Creating a list using slice operator that contains the first 3 articles.
    three_articles = articles[:3]
    print(three_articles)



    # Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}% \nHeadline: {article['title']}, \nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)

    # Send each article as a separate message via Twilio.
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+17752615744",
            to="+233552233328",
        )

        print(message.sid)


