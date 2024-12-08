import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "S263JZ31EQGP4BU2"
NEWS_API_KEY = ""

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
print(difference)

# percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = (difference / float(yesterday_closing_price)) * 100
print(diff_percent)

# Using the News API to get articles related to the COMPANY_NAME.
if diff_percent > 5:
    new_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(url=NEWS_ENDPOINT, params=new_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    print(articles)

    #  Creating a list using slice operator that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]
    print(three_articles)



 # Create a new list of the first 3 article's headline and description using list comprehension.

# O 9. - Send each article as a separate message via Twilio.



# OptODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

