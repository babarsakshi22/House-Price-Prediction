from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

HousePricePredictionModel = pickle.load(open("house-price-prediction.pkl", "rb"))


@app.route("/")
def home():
    return render_template("index.html")

    

@app.route("/predict", methods=["GET","POST"])
def predict():

    if request.method == "POST":

        data = request.form
    
        sqftarea = float(data.get("sqftarea"))
        bedrooms = float(data.get("bedrooms"))
        grade = float(data.get("grade"))

        price = HousePricePredictionModel.predict([[sqftarea,bedrooms,grade]])
 
        return render_template("index.html", price=round(price[0][0], 2))

    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)