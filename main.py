from flask import Flask, request, jsonify
import stock as sk
import ML_Predictions as ml

app = Flask(__name__)

@app.route('/stock_details', methods=['GET'])
def get_stock_details():
    stock_symbol = request.args.get('symbol')
    days_to_predict = int(request.args.get('days', 2))  # Default to 2 days if days param not provided
    if not stock_symbol:
        return jsonify({'error': 'Stock symbol is required'}), 400

    # No need to validate days_to_predict if it's restricted on the client side

    stock = sk.Stock(stock_symbol)
    historical_data = stock.historyCall()
    predict_model = ml.predict(historical_data)
    predicted_prices = predict_model.predictClosing(days_to_predict)
    # Reshaping the predicted prices into 2D format
    predicted_prices = predicted_prices.tolist()
    current_price, shares_outstanding, market_cap = stock.stockDetails()

    return jsonify({
        'symbol': stock_symbol,
        'current_price': current_price,
        'shares_outstanding': shares_outstanding,
        'market_cap': market_cap,
        'predicted_closing_prices_2d': predicted_prices,
        'days_predicted': days_to_predict
    })

if __name__ == '__main__':
    app.run(debug=True)
