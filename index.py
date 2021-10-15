from flask import Flask
import requests
import time

start_time = time.time()

btc = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
current_price = btc.json()['bpi']['USD']['rate']
total = 0
counter = 0

btc_to_usd = '<h1><center><p style = "font-family:georgia,garamond,serif;font-size:16px;font-style:italic;">' + time.asctime() + '<br>' + 'Current Bitcoin Price is equal to ' + current_price.replace(",", "") + ' $' + '<br>' + '</h1></center></p>'


def avg_ten_minutes_price():
    global total, counter
    while time.time() < start_time + 2:
        counter = counter + 1
        total = total + float(current_price.replace(",", ""))

    avg = total / counter
    return avg


avg_btc = '<h2><center><center><p style = "font-family:georgia,garamond,serif;font-size:16px;font-style:italic;">' + ' Average Bitcoin Price for the last 10 minutes is equal to ' + format(avg_ten_minutes_price(), ".4f") + ' $' + '</h2></center></p>'

app = Flask(__name__)


@app.route("/")
def pythonApp():
    return btc_to_usd + avg_btc


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
