from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/')
def hello():
    return "HI"


@app.route('/predict_stock_price', methods=['POST'])
def predict_stock_price():
    company= request.form['company']
    country= request.form['country']
    year= float(request.form['year'])
    market_cap = float(request.form['market_cap'])
    expenses = float(request.form['expenses'])
    revenue = float(request.form['revenue'])
    market_share = float(request.form['market_share'])

    response = jsonify({
        'estimated_stock_price': util.get_predicted_stock(company,country,year,market_cap,expenses,revenue,market_share)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(host='0.0.0.0', port=5000)

# >> # Create a new virtual environment
# >> virtualenv venv
# >>
# >> # Activate the environment
# >> # On Windows
# >> venv\Scripts\activate
# pip install flask numpy pandas   
# pip install gunicorn pickle json
