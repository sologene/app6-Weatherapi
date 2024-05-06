from flask import Flask, render_template
import pandas as pd

app = Flask("__name__")
stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME"]]
@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    df = pd.read_csv("data_small/TG_STAID"+str(station).zfill(6)+".txt", skiprows=20, parse_dates=["    DATE"])
    temprature = df.loc[df["    DATE"] == date]["   TG"].squeeze()/10
    return {"station": station,
            "date":date,
            "temprature":temprature}

@app.route("/api/v1/<station>")
def all_data(station):
    df = pd.read_csv("data_small/TG_STAID"+str(station).zfill(6)+".txt", skiprows=20, parse_dates=["    DATE"])
    return df.to_dict(orient="records")

@app.route("/api/yearly/v1/<station>/<year>")
def all_year(station,year):
    df = pd.read_csv("data_small/TG_STAID"+str(station).zfill(6)+".txt", skiprows=20)
    df["    DATE"]= df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    return result



if __name__ == "__main__":
    app.run(debug=True)