import json
import pickle
import numpy as np

__Companies = None
__Countries = None
__data_columns = None
__model = None

def get_predicted_stock(company, country, year, market_cap, expenses, revenue, market_share):
    # Ensure __data_columns is loaded before proceeding
    if __data_columns is None or __model is None:
        raise ValueError("Model or data columns are not loaded. Call load_saved_artifacts() first.")

    # Find the index of the provided company and country
    loc_index = __data_columns.index("company_" + company) if "company_" + company in __data_columns else -1
    loc_index1 = __data_columns.index("country_" + country) if "country_" + country in __data_columns else -1

    # Prepare the input array
    x = np.zeros(len(__data_columns))
    x[0] = market_cap
    x[1] = year
    x[2] = expenses
    x[3] = revenue
    x[4] = market_share

    # Update the input array based on the indices found
    if loc_index >= 0:
        x[loc_index] = 1
    if loc_index1 >= 0:
        x[loc_index1] = 1

    # Return the predicted stock price
    return "$" + str(round(__model.predict([x])[0], 2)) + "M"

def get_company_names():
    return __Companies

def get_country_names():
    return __Countries

def load_saved_artifacts():
    print("Loading saved artifacts...start")
    global __data_columns
    global __Companies
    global __Countries
    global __model

    # Load data columns
    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __Companies = __data_columns[5:360]  # Adjust this as necessary based on your data
        __Countries = __data_columns[360:]  # Adjust this as necessary based on your data

    # Load the model
    with open("./artifacts/Stock_price_model.pkl", "rb") as f:
        __model = pickle.load(f)

    print("Loading saved artifacts...done")

if __name__ == '__main__':
    load_saved_artifacts()
    # Example test (remove or comment out in production)
    print(get_predicted_stock("zooxo", "ukraine", 2015, 2340, 25, 11, 30))
