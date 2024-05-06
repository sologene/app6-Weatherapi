from flask import Flask, render_template
import pandas as pd

app = Flask("__name__")

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station,date):
    df = pd.read_csv("data_small/TG_STAID"+str(station).zfill(6)+".txt", skiprows=20, parse_dates=["    DATE"])
    temprature = df.loc[df["    DATE"] == date]["   TG"].squeeze()/10
    return {"station": station,
            "date":date,
            "temprature":temprature}

if __name__ == "__main__":
    app.run(debug=True)