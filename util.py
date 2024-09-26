import json
import pickle
import numpy as np


__Companies=None
__Countries=None
__data_columns =None
__model=None

def get_predicted_stock(company,country,year,market_cap,expenses,revenue,market_share):
    try:
        loc_index= __data_columns.index("company_" + company)
    except:
        loc_index=-1
    try:
        loc_index1= __data_columns.index("country_" + country)
    except:
        loc_index1=-1
    
    x=np.zeros(len(__data_columns))
    x[0] = market_cap
    x[1] = year
    x[2] = expenses
    x[3] = revenue
    x[4] = market_share
    if loc_index >=0:
        x[loc_index] = 1
    if loc_index1 >=0:
        x[loc_index1] = 1
    return "$"+ str(round(__model.predict([x])[0],2)) + "M"
        

def get_company_names():
    return __Companies
def get_country_names():
    return __Countries

def load_saved_artifacts():
    print("loading saved srtifacts...start")
    global __data_columns
    global __Companies
    global __Countries
    global __model

    with open("./artifacts/columns.json","r") as f:
        __data_columns =json.load(f)['data_columns']
        __Companies = __data_columns[5:360]
        __Countries=__data_columns[360:]
    
    with open("./artifacts/Stock_price_model.pkl","rb") as f:
        __model = pickle.load(f)
    print("Loading saved artifacts")

if __name__ =='__main__':
    load_saved_artifacts()
    # print(get_company_names())
    print(get_predicted_stock("zooxo","ukraine",2015,2340,25,11,30))
