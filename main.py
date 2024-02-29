# Framework that will link the Frontend of the site
# to the Backend
from flask import Flask, render_template, request, jsonify
import stock as sk
import ML_Predictions as ml

app = Flask(__name__)

# Sample route to get the current stock closing price
@app.route('/current_closing_price/<string:stock_symbol>', methods=['GET'])
def get_current_closing_price(stock_symbol):
    stock = sk.Stock(stock_symbol)
    historical_data = sk.historyCall()
    
    # Creating an instance of the Predict class
    predictor = ml.Predict(historical_data)

    # Getting the current closing price
    current_closing_price = sk.currentPrice()
    
    return jsonify({'symbol': stock_symbol, 'current_closing_price': current_closing_price})

# Sample route to get the stock count
@app.route('/stock_count/<string:stock_symbol>', methods=['GET'])
def get_stock_count(stock_symbol):
    stock = sk.Stock(stock_symbol)
    stock_count = sk.stockCount()
    return jsonify({'symbol': stock_symbol, 'stock_count': stock_count})

# Sample route to make predictions for closing prices
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
