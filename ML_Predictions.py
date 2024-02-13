import pandas as pd
# ML for prediction
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import train_test_split

class predict():

    def __init__(self, historical_data):
        self.historical_data = historical_data

    # Does the prediction 
    # Returns: Predicted Price based on the days
    def predict(self, data, days):
        return
    
    # Calls the predict function on data of only Opening Prices
    # Returns: Predicted Opening Price based on the days
    def predictOpening(self, days):
        OpenData = self.historical_data['Open']
        return self.predict(OpenData, days)

    # Calls the predict function on data of only Closing Prices
    # Returns: Predicted Closing Price based on the days
    def predictClosing(self, days):
        ClosingData = self.historical_data['Close']
        return self.predict(ClosingData, days)
