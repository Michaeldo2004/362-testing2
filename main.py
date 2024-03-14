from flask import Flask, render_template, request, jsonify
import stock as sk
import ML_Predictions as ml

from flask import Flask, request, jsonify
from main import Stock

app = Flask(__name__)

@app.route('/stock_details', methods=['GET'])
def get_stock_details():
    stock_symbol = request.args.get('symbol')
    if not stock_symbol:
        return jsonify({'error': 'Stock symbol is required'}), 400
    
    stock = Stock(stock_symbol)
    current_price, shares_outstanding, market_cap = stock.stockDetails()
    
    return jsonify({
        'symbol': stock_symbol,
        'current_price': current_price,
        'shares_outstanding': shares_outstanding,
        'market_cap': market_cap
    })

if __name__ == '__main__':
    app.run(debug=True)
