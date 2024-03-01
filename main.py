# Framework that will link the Frontend of the site
# to the Backend
from flask import Flask, render_template, request, jsonify
import stock as sk
import ML_Predictions as ml

app = Flask(__name__)

# Closing Price
@app.route('/current_closing_price/<string:stock_symbol>', methods=['GET'])
def get_current_closing_price(stock_symbol):
    stock = sk.Stock(stock_symbol)
    historical_data = sk.historyCall()
    
    # Creating an instance of the Predict class
    predictor = ml.Predict(historical_data)

    # Getting the current closing price
    current_closing_price = sk.currentPrice()
    
    return jsonify({'symbol': stock_symbol, 'current_closing_price': current_closing_price})

# MarketCap
@app.route('/market_cap/<string:stock_symbol>', methods=['GET'])
def get_market_cap(stock_symbol):
    stock = sk.Stock(stock_symbol)
    
    # Get the market cap using the Stock class
    market_cap = stock.marketCap()

    return jsonify({'symbol': stock_symbol, 'market_cap': market_cap})

# Stock Count
@app.route('/stock_count/<string:stock_symbol>', methods=['GET'])
def get_stock_count(stock_symbol):
    stock = sk.Stock(stock_symbol)
    stock_count = sk.stockCount()
    return jsonify({'symbol': stock_symbol, 'stock_count': stock_count})

# Predict Closing
@app.route('/predict_closing/<string:stock_symbol>', methods=['GET'])
def make_closing_predictions(stock_symbol):
    stock = sk.Stock(stock_symbol)
    historical_data = sk.historyCall()
    
    # Creating an instance of the Predict class
    predictor = ml.Predict(historical_data)

    # Example: Predict closing price for the next 2 days
    predicted_closing_prices = predictor.predictClosing(days=2)

    return jsonify({'symbol': stock_symbol, 'predicted_closing_prices': predicted_closing_prices.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
