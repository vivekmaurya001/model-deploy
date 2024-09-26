from flask import Flask, request, jsonify
import util  # Make sure this is imported correctly

app = Flask(__name__)

# Load saved artifacts when the app starts
util.load_saved_artifacts()

@app.route('/hello')
def hello():
    return "HI"

@app.route('/predict_stock_price', methods=['POST'])
def predict_stock_price():
    company = request.form['company']
    country = request.form['country']
    year = float(request.form['year'])
    market_cap = float(request.form['market_cap'])
    expenses = float(request.form['expenses'])
    revenue = float(request.form['revenue'])
    market_share = float(request.form['market_share'])

    response = jsonify({
        'estimated_stock_price': util.get_predicted_stock(company, country, year, market_cap, expenses, revenue, market_share)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Stock Price Prediction...")
    app.run()
